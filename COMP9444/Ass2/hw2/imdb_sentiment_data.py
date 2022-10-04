import os
import sys
import tarfile
import glob
import string
import collections
import numpy as np

def check_file(filename, expected_bytes):
    """Download a file if not present, and make sure it's the right size."""
    if not os.path.exists(filename):
        print("please make sure {0} exists in the current directory".format(filename))
    statinfo = os.stat(filename)
    if statinfo.st_size == expected_bytes:
        print('Found and verified', filename)
    else:
        print(statinfo.st_size)
        raise Exception(
            "File {0} didn't have the expected size. Please ensure you have downloaded the assignment files correctly".format(filename))
    return filename


# Read the data into a list of strings.
def extract_data(filename):
    """Extract data from tarball and store as list of strings"""
    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'data2/')):
        with tarfile.open(filename, "r") as tarball:
            dir = os.path.dirname(__file__)
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(tarball, os.path.join(dir,"data2/"))
    return

def read_data():
    print("READING DATA")
    data = []
    dir = os.path.dirname(__file__)
    file_list = glob.glob(os.path.join(dir,
                                        'data2/pos/*'))
    file_list.extend(glob.glob(os.path.join(dir,
                                        'data2/neg/*')))
    print("Parsing %s files" % len(file_list))
    for f in file_list:
        with open(f, "r") as openf:
            s = openf.read()
            no_punct = ''.join(c for c in s if c not in string.punctuation)
            data.extend(no_punct.split())

    print(data[:5])
    return data

def build_dataset(words, n_words):
    """Process raw inputs into a dataset."""
    count = [['UNK', -1]]
    count.extend(collections.Counter(words).most_common(n_words - 1))
    dictionary = dict()
    for word, _ in count:
        dictionary[word] = len(dictionary)
    data = list()
    unk_count = 0
    for word in words:
        if word in dictionary:
            index = dictionary[word]
        else:
            index = 0  # dictionary['UNK']
            unk_count += 1
        data.append(index)
    count[0][1] = unk_count
    reversed_dictionary = dict(zip(dictionary.values(), dictionary.keys()))
    return data, count, dictionary, reversed_dictionary

def get_dataset(vocabulary_size):
    if os.path.exists(os.path.join(os.path.dirname(__file__), "data.npy")):
        print("loading saved parsed data, to reparse, delete 'data.npy'")
        data = np.load("data.npy")
        count = np.load("count.npy")
        dictionary = np.load("Word2Idx.npy").item()
        reverse_dictionary = np.load("Idx2Word.npy").item()
    else:
        filename = check_file('reviews.tar.gz', 14839260)
        extract_data(filename) # unzip
        vocabulary = read_data()
        print('Data size', len(vocabulary))
        # Step 2: Build the dictionary and replace rare words with UNK token.
        data, count, dictionary, reverse_dictionary =\
            build_dataset(vocabulary, vocabulary_size)

        np.save("data", data)
        np.save("count", count)
        np.save("Idx2Word", reverse_dictionary)
        np.save("Word2Idx", dictionary)
        del vocabulary  # Hint to reduce memory.
    return data, count, dictionary, reverse_dictionary
