#!/usr/bin/python3

#
# Allow COMP[29]041 students  to enter peer assessments of each other's work
# And see what peer assessment have been entered of them.
#

#
# The reference implementation has a button "See Other Students Assessment of Your Work" which shows a student a summary of how they have been assessed by other students including a median grade. 
# Your task is to add this missing page. Note: calculating the median grade will be a challenge excercise. 

import collections, glob, os,re
from flask import Flask, session, render_template, request

# peer assessments are stored in this directory

ASSESSMENTS_DIRECTORY = 'assessments'

# this file contain one line for each COMP[29]041 student
# each line contains zid:name:password

STUDENT_DETAILS_FILE = 'students.txt'

# # # # # # # # # # # # # # # # # # # # # # # # #
# Flask functions
# # # # # # # # # # # # # # # # # # # # # # # # #

# flask begins
app = Flask(__name__, template_folder='.')

# display initial page request zid/password
# then go to /login
@app.route('/', methods=['GET'])
def start():
	# input zid and password
	return render_template('peer_login.html')


# if zid/password authenticates
# return a page which allows a student to peer assess another student --> go to /enter_grade
# or see other students assessment of them --> go to /assessments
@app.route('/login', methods=['POST'])
def login():
	zid = request.form.get('zid', '')
	password = request.form.get('password', '')
	zid = re.sub(r'\D', '', zid)

	# get all student details
	student_details = read_student_details()

	# Authenticate
	# zid or password is empty or zid is not exist
	if (zid == "") or (password == "") or (zid not in student_details):
		login_error = "unknown zid - are you enrolled in COMP[29]041? "
		return render_template('peer_login.html', error = login_error)
	# password is wrong
	elif password != student_details[zid]['password']:
		login_error = "wrong password "
		return render_template('peer_login.html', error = login_error)
	else:
		# store zid in session cookie
		session['zid'] = zid
		# return peerselect with the id of this student
		return render_template('peer_select_student.html', students=student_details)


# return a page allowing a peer assessment of the selected student to be entered
@app.route('/enter_grade', methods=['POST'])
def enter_grade():

	# check we have previous autheticated zid in session cookie
	# if zid is wrong --> return to login part
	if 'zid' not in session:
		return render_template('peer_login.html')
	
	student_assessed_zid = request.form.get('student_assessed', '')
	
	student_details = read_student_details()
	
	session['student_assessed_zid'] = student_assessed_zid
	student_assessed_name = student_details[student_assessed_zid]['name']
	
	assessment_file = os.path.join(ASSESSMENTS_DIRECTORY, student_assessed_zid + '.' + session['zid'])
	try:
		with open(assessment_file) as f:
			current_grade = f.read()
	# YUNQIU XU change here, do not return error if not exist
	# except OSError:
	except:
		current_grade = ''
		
	return render_template('peer_enter_grade.html',
							name=student_assessed_name,
							number=student_assessed_zid,
							grade_descriptions=possible_grades,
							existing_grade=current_grade)


# save a peer assessment of the selected student
@app.route('/save_grade', methods=['POST'])
def save_grade():
	# check we have a previous authenticated zid in session cookie
	if 'zid' not in session:
		return render_template('peer_login.html')
	
	student_assessed_zid = session.get('student_assessed_zid', '')
	student_details = read_student_details()
	student_assessed_name = student_details[student_assessed_zid]['name']

	# TEST: this is the student you assess
	# print("student_assessed_zid " + student_assessed_zid)
	# print("student_assessed_name " + student_assessed_name)
	# print("-----")

	assessment_file = os.path.join(ASSESSMENTS_DIRECTORY, student_assessed_zid + '.' + session['zid'])
	grade = request.form.get('grade', '')

	
	with open(assessment_file,"w") as f:
			f.write(grade)

	return render_template('peer_select_student.html',
							students=student_details,
							message='A peer assessment of ' + grade + ' has been saved for ' + student_assessed_name)


# get your peer assessments and median assessment
@app.route('/assessments', methods=['POST'])
def collect_assessments():
	# check we have previous autheticated zid in session cookie
	# if zid is wrong --> return to login part
	if 'zid' not in session:
		return render_template('peer_login.html')
	
	# get stugent zid and other details
	my_zid = session['zid']

	# TEST
	# print("My zid is " + my_zid)

	# collect output messages
	student_details = read_student_details()
	my_assessments = get_assessments(my_zid, student_details)
	my_median = get_median_assessment(my_assessments)

	# TEST
	# print("Num of assessments: " + str(len(my_assessments)))
	# print("Median" + my_median)
	# print("-----")
	
	# output rendered page
	return render_template('peer_assessments.html', assessments = my_assessments, median = my_median)


# # # # # # # # # # # # # # # # # # # # # # # # #
# General functions
# # # # # # # # # # # # # # # # # # # # # # # # #

# read the student details file
# return it as a dict (an OrderedDict sorted on name)

def read_student_details():
	with open(STUDENT_DETAILS_FILE) as f:
		students = [line.strip().split(':') for line in f]
	sorted_students = sorted(students, key=lambda student: student[1]) 
	student_details = collections.OrderedDict()
	for (zid, name, password) in sorted_students:
		student_details[zid] = {'name': name, 'password' : password}
	return student_details
	

# read the student details file
# return it as a dict (an OrderedDict sorted on name)

possible_grades = collections.OrderedDict([
	('A', 'working correctly'),
	('B', 'minor problems'),
	('C', 'major problems but significant part works'),
	('D', 'any part works'),
	('E', 'attempted but not working')
	])


# get all assessments have been entered for you
# return it as a dict:
# 	key: zid + name
# 	value: assessment
def get_assessments(my_zid, student_details):
	# the format: 1111111.2222222 --> 1111111 is assessed by 2222222
	assessments = {}
	pattern = re.compile("^assessments/" + my_zid + "\.[0-9]{7}$")
	for path in glob.glob("assessments/*"):
		if re.match(pattern, path):
			other_zid = path[-7:]
			other_name = student_details[other_zid]['name']
			with open(path, 'r') as f:
				other_assessment = f.readline()
			# add into assessments
			assessments[other_zid + " " + other_name] = other_assessment
	return assessments


# get median of assessments
# input: a dict of assessments
# output: median
def get_median_assessment(assessments):
	sorted_values = sorted(assessments.values())
	length = len(sorted_values)
	if length == 0:
		return ""
	elif length % 2 != 0:
		return sorted_values[length / 2]
	else:
		return sorted_values[length / 2 - 1] + '/' + sorted_values[length / 2]
	
		

# start flask as webserver

if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	app.run(debug=True)
