#!/usr/bin/env/python
# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy as np
import glob
import os
import sys
import tarfile
import string
from random import randint
from tqdm import tqdm

# load hyper-paras
n_words, embed_size = 400001, 50 # embeddings.shape # 400001, 50
rnn_layers = 1
rnn_size = 64
learning_rate = 0.0001
batch_size = 128
attention_size = 64

def load_glove_embeddings():
    data = open("glove.6B.50d.txt",'r')
    embeddings = [[0] * 50] # for 'UNK'
    word_index_dict = {'UNK' : 0}
    index = 1
    for line in data:
        line = line.split()
        word, vector = line[0], line[1:]
        embeddings.append(vector)
        word_index_dict[word] = index
        index += 1
    embeddings = np.array(embeddings, dtype = np.float32)
    return embeddings, word_index_dict

def unzip_data(filename):
    """Extract data from tarball and store as list of strings"""
    if not os.path.exists('unzipped_reviews/'):
        with tarfile.open(filename, "r", encoding="utf-8") as tarball:
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
            
                tar.extractall(path, members, numeric_owner) 
                
            
            safe_extract(tarball, "unzipped_reviews/")
    return

stop_words = {'secondly': 1, 'all': 1, 'consider': 1, 'pointing': 1, 'whoever': 1, 'results': 1, 'felt': 1, 'four': 1, 'edu': 1, 'go': 1, 'oldest': 1, 'causes': 1, 'poorly': 1, 'whose': 1, 'certainly': 1, 'biol': 1, 'everywhere': 1, 'vs': 1, 'young': 1, 'containing': 1, 'presents': 1, 'to': 1, 'does': 1, 'present': 1, 'th': 1, 'under': 1, 'sorry': 1, 'include': 1, "a's": 1, 'sent': 1, 'insofar': 1, 'consequently': 1, 'far': 1, 'none': 1, 'every': 1, 'yourselves': 1, 'associated': 1, "we'll": 1, 'immediately': 1, 'presented': 1, 'did': 1, 'turns': 1, 'having': 1, "they've": 1, 'large': 1, 'p': 1, 'small': 1, 'thereupon': 1, 'noted': 1, "it'll": 1, "i'll": 1, 'parted': 1, 'smaller': 1, 'says': 1, "you'd": 1, 'd': 1, 'past': 1, 'likely': 1, 'invention': 1, 'zz': 1, 'zt': 1, 'further': 1, 'even': 1, 'index': 1, 'what': 1, 'appear': 1, 'giving': 1, 'section': 1, 'brief': 1, 'fifth': 1, 'goes': 1, 'sup': 1, 'new': 1, 'seemed': 1, 'ever': 1, 'full': 1, "c'mon": 1, 'respectively': 1, 'men': 1, 'here': 1, 'youngest': 1, 'let': 1, 'groups': 1, 'others': 1, "hadn't": 1, 'along': 1, "aren't": 1, 'obtained': 1, 'great': 1, 'ref': 1, 'k': 1, 'allows': 1, 'proud': 1, "i'd": 1, 'resulting': 1, 'arent': 1, 'usually': 1, 'que': 1, "i'm": 1, 'changes': 1, 'thats': 1, 'hither': 1, 'via': 1, 'followed': 1, 'members': 1, 'merely': 1, 'ts': 1, 'ask': 1, 'ninety': 1, 'vols': 1, 'viz': 1, 'ord': 1, 'readily': 1, 'everybody': 1, 'use': 1, 'from': 1, 'working': 1, 'contains': 1, 'two': 1, 'next': 1, 'few': 1, 'therefore': 1, 'taken': 1, 'themselves': 1, 'thru': 1, 'until': 1, 'today': 1, 'more': 1, 'knows': 1, 'clearly': 1, 'becomes': 1, 'hereby': 1, 'herein': 1, 'downing': 1, "ain't": 1, 'particular': 1, 'known': 1, "who'll": 1, 'cases': 1, 'given': 1, 'must': 1, 'me': 1, 'states': 1, 'mg': 1, 'room': 1, 'f': 1, 'this': 1, 'ml': 1, 'when': 1, 'anywhere': 1, 'nine': 1, 'can': 1, 'mr': 1, 'following': 1, 'making': 1, 'my': 1, 'example': 1, 'something': 1, 'indicated': 1, 'give': 1, "didn't": 1, 'near': 1, 'high': 1, 'indicates': 1, 'numbers': 1, 'want': 1, 'arise': 1, 'longest': 1, 'information': 1, 'needs': 1, 'end': 1, 'thing': 1, 'rather': 1, 'ie': 1, 'get': 1, 'how': 1, 'instead': 1, "doesn't": 1, 'okay': 1, 'tried': 1, 'may': 1, 'overall': 1, 'after': 1, 'eighty': 1, 'them': 1, 'tries': 1, 'ff': 1, 'date': 1, 'such': 1, 'man': 1, 'a': 1, 'thered': 1, 'third': 1, 'whenever': 1, 'maybe': 1, 'appreciate': 1, 'q': 1, 'cannot': 1, 'so': 1, 'specifying': 1, 'allow': 1, 'keeps': 1, 'looking': 1, 'order': 1, "that's": 1, 'six': 1, 'help': 1, "don't": 1, 'furthering': 1, 'indeed': 1, 'itd': 1, 'mainly': 1, 'soon': 1, 'years': 1, 'course': 1, 'through': 1, 'looks': 1, 'still': 1, 'its': 1, 'before': 1, 'beside': 1, 'group': 1, 'thank': 1, "he's": 1, 'selves': 1, 'inward': 1, 'fix': 1, 'actually': 1, 'better': 1, 'willing': 1, 'differently': 1, 'thanx': 1, 'somethan': 1, 'ours': 1, "'re": 1, 'might': 1, "haven't": 1, 'then': 1, 'non': 1, 'good': 1, 'affected': 1, 'greater': 1, 'thereby': 1, 'downs': 1, 'auth': 1, "you've": 1, 'they': 1, 'not': 1, 'now': 1, 'discuss': 1, 'nor': 1, 'nos': 1, 'down': 1, 'gets': 1, 'hereafter': 1, 'always': 1, 'reasonably': 1, 'whither': 1, 'l': 1, 'sufficiently': 1, 'each': 1, 'found': 1, 'went': 1, 'higher': 1, 'side': 1, "isn't": 1, 'mean': 1, 'everyone': 1, 'significantly': 1, 'doing': 1, 'ed': 1, 'eg': 1, 'related': 1, 'owing': 1, 'ex': 1, 'year': 1, 'substantially': 1, 'et': 1, 'beyond': 1, "c's": 1, 'puts': 1, 'out': 1, 'try': 1, 'shown': 1, 'opened': 1, 'miss': 1, 'furthermore': 1, 'since': 1, 'research': 1, 'rd': 1, 're': 1, 'seriously': 1, "shouldn't": 1, "they'll": 1, 'got': 1, 'forth': 1, 'shows': 1, 'turning': 1, 'state': 1, 'million': 1, 'little': 1, 'quite': 1, "what'll": 1, 'whereupon': 1, 'besides': 1, 'put': 1, 'anyhow': 1, 'wanted': 1, 'beginning': 1, 'g': 1, 'could': 1, 'needing': 1, 'hereupon': 1, 'keep': 1, 'turn': 1, 'place': 1, 'w': 1, 'ltd': 1, 'hence': 1, 'onto': 1, 'think': 1, 'first': 1, 'already': 1, 'seeming': 1, 'omitted': 1, 'thereafter': 1, 'number': 1, 'thereof': 1, 'yourself': 1, 'done': 1, 'least': 1, 'another': 1, 'open': 1, 'awfully': 1, "you're": 1, 'differ': 1, 'necessarily': 1, 'indicate': 1, 'ordering': 1, 'inasmuch': 1, 'approximately': 1, 'anyone': 1, 'needed': 1, 'too': 1, 'hundred': 1, 'gives': 1, 'interests': 1, 'mostly': 1, 'that': 1, 'exactly': 1, 'took': 1, 'immediate': 1, 'part': 1, 'somewhat': 1, "that'll": 1, 'believe': 1, 'herself': 1, 'than': 1, "here's": 1, 'begins': 1, 'kind': 1, 'b': 1, 'unfortunately': 1, 'showed': 1, 'accordance': 1, 'gotten': 1, 'largely': 1, 'second': 1, 'i': 1, 'r': 1, 'were': 1, 'toward': 1, 'anyways': 1, 'and': 1, 'sees': 1, 'ran': 1, 'thoughh': 1, 'turned': 1, 'anybody': 1, 'say': 1, 'unlikely': 1, 'have': 1, 'need': 1, 'seen': 1, 'seem': 1, 'saw': 1, 'any': 1, 'relatively': 1, 'smallest': 1, 'zero': 1, 'thoroughly': 1, 'latter': 1, "i've": 1, 'downwards': 1, 'aside': 1, 'thorough': 1, 'predominantly': 1, 'also': 1, 'take': 1, 'which': 1, 'wanting': 1, 'greatest': 1, 'begin': 1, 'added': 1, 'unless': 1, 'shall': 1, 'knew': 1, 'wells': 1, "where's": 1, 'most': 1, 'eight': 1, 'amongst': 1, 'significant': 1, 'nothing': 1, 'pages': 1, 'parting': 1, 'sub': 1, 'cause': 1, 'kg': 1, 'especially': 1, 'nobody': 1, 'clear': 1, 'later': 1, 'm': 1, 'km': 1, 'face': 1, 'heres': 1, "you'll": 1, 'regards': 1, "weren't": 1, 'normally': 1, 'fact': 1, 'saying': 1, 'particularly': 1, 'et-al': 1, 'show': 1, 'able': 1, 'anyway': 1, 'ending': 1, 'find': 1, 'promptly': 1, 'one': 1, 'specifically': 1, 'mug': 1, "won't": 1, 'should': 1, 'only': 1, 'going': 1, 'specify': 1, 'announce': 1, 'pointed': 1, "there've": 1, 'do': 1, 'over': 1, 'his': 1, 'above': 1, 'means': 1, 'between': 1, 'stop': 1, 'sensible': 1, 'truly': 1, "they'd": 1, 'ones': 1, 'hid': 1, 'nearly': 1, 'words': 1, 'despite': 1, 'during': 1, 'beings': 1, 'him': 1, 'is': 1, 'areas': 1, 'regarding': 1, 'qv': 1, 'h': 1, 'generally': 1, 'twice': 1, 'she': 1, 'contain': 1, 'x': 1, 'where': 1, 'rooms': 1, 'ignored': 1, 'their': 1, 'ends': 1, "hasn't": 1, 'namely': 1, 'sec': 1, 'are': 1, "that've": 1, 'best': 1, 'wonder': 1, 'said': 1, 'ways': 1, 'away': 1, 'currently': 1, 'please': 1, 'ups': 1, "wasn't": 1, 'outside': 1, "there's": 1, 'various': 1, 'hopefully': 1, 'affecting': 1, 'probably': 1, 'neither': 1, 'across': 1, 'available': 1, 'we': 1, 'never': 1, 'recently': 1, 'opening': 1, 'importance': 1, 'points': 1, 'however': 1, 'by': 1, 'no': 1, 'come': 1, 'both': 1, 'c': 1, 'last': 1, 'thou': 1, 'many': 1, 'taking': 1, 'thence': 1, 'according': 1, 'against': 1, 'etc': 1, 's': 1, 'became': 1, 'interesting': 1, 'com': 1, 'asked': 1, 'comes': 1, 'otherwise': 1, 'among': 1, 'presumably': 1, 'co': 1, 'ZZ': 1, 'point': 1, 'within': 1, 'had': 1, 'ca': 1, 'whatever': 1, 'furthered': 1, 'ZT': 1, "couldn't": 1, 'moreover': 1, 'throughout': 1, 'considering': 1, 'meantime': 1, 'pp': 1, 'described': 1, 'asks': 1, "it's": 1, 'due': 1, 'been': 1, 'quickly': 1, 'whom': 1, 'much': 1, 'interest': 1, 'certain': 1, 'whod': 1, 'hardly': 1, "it'd": 1, 'wants': 1, 'adopted': 1, 'corresponding': 1, 'beforehand': 1, "what's": 1, 'else': 1, 'finds': 1, 'worked': 1, 'an': 1, 'hers': 1, 'former': 1, 'those': 1, 'case': 1, 'myself': 1, 'novel': 1, 'look': 1, 'unlike': 1, 'these': 1, 'thereto': 1, 'value': 1, 'n': 1, 'will': 1, 'while': 1, "wouldn't": 1, 'theres': 1, 'seven': 1, 'whereafter': 1, 'almost': 1, 'wherever': 1, 'refs': 1, 'thus': 1, 'it': 1, 'cant': 1, 'someone': 1, 'im': 1, 'in': 1, 'somebody': 1, 'alone': 1, 'id': 1, 'if': 1, 'different': 1, 'anymore': 1, 'perhaps': 1, 'suggest': 1, 'make': 1, 'same': 1, 'wherein': 1, 'member': 1, 'parts': 1, 'potentially': 1, 'widely': 1, 'several': 1, 'howbeit': 1, 'used': 1, 'see': 1, 'somewhere': 1, 'keys': 1, 'faces': 1, 'upon': 1, 'effect': 1, 'uses': 1, 'interested': 1, 'thoughts': 1, 'recent': 1, 'off': 1, 'whereby': 1, 'older': 1, 'nevertheless': 1, 'makes': 1, 'youre': 1, 'well': 1, 'kept': 1, 'obviously': 1, 'thought': 1, 'without': 1, "can't": 1, 'y': 1, 'the': 1, 'yours': 1, 'latest': 1, 'lest': 1, 'things': 1, "she'll": 1, 'newest': 1, 'just': 1, 'less': 1, 'being': 1, 'nd': 1, 'therere': 1, 'liked': 1, 'beginnings': 1, 'thanks': 1, 'behind': 1, 'facts': 1, 'useful': 1, 'yes': 1, 'lately': 1, 'yet': 1, 'unto': 1, 'afterwards': 1, 'wed': 1, "we've": 1, 'seems': 1, 'except': 1, 'thousand': 1, 'lets': 1, 'other': 1, 'inner': 1, 'tell': 1, 'has': 1, 'adj': 1, 'ought': 1, 'gave': 1, "t's": 1, 'around': 1, 'big': 1, 'showing': 1, "who's": 1, 'possible': 1, 'usefully': 1, 'early': 1, 'possibly': 1, 'five': 1, 'know': 1, 'similarly': 1, 'world': 1, 'apart': 1, 'name': 1, 'abst': 1, 'nay': 1, 'necessary': 1, 'like': 1, 'follows': 1, 'theyre': 1, 'either': 1, 'fully': 1, 'become': 1, 'works': 1, 'page': 1, 'grouping': 1, 'therein': 1, 'shed': 1, 'because': 1, 'old': 1, 'often': 1, 'successfully': 1, 'some': 1, 'back': 1, 'self': 1, 'towards': 1, 'shes': 1, 'specified': 1, 'home': 1, "'ve": 1, 'thinks': 1, 'happens': 1, 'vol': 1, "there'll": 1, 'for': 1, 'affects': 1, 'highest': 1, 'though': 1, 'per': 1, 'whole': 1, 'everything': 1, 'asking': 1, 'provides': 1, 'tends': 1, 'three': 1, 't': 1, 'be': 1, 'who': 1, 'run': 1, 'furthers': 1, 'seconds': 1, 'of': 1, 'obtain': 1, 'nowhere': 1, 'although': 1, 'entirely': 1, 'on': 1, 'about': 1, 'goods': 1, 'ok': 1, 'would': 1, 'anything': 1, 'oh': 1, 'theirs': 1, 'v': 1, 'o': 1, 'whomever': 1, 'whence': 1, 'important': 1, 'plus': 1, 'act': 1, 'slightly': 1, 'or': 1, 'seeing': 1, 'own': 1, 'whats': 1, 'formerly': 1, 'previously': 1, "n't": 1, 'into': 1, 'youd': 1, 'www': 1, 'getting': 1, 'backing': 1, 'hes': 1, 'appropriate': 1, 'very': 1, 'primarily': 1, 'theyd': 1, 'couldnt': 1, 'whos': 1, 'your': 1, 'her': 1, 'area': 1, 'aren': 1, 'downed': 1, 'apparently': 1, 'there': 1, 'long': 1, 'why': 1, 'hed': 1, 'accordingly': 1, "we're": 1, 'way': 1, 'resulted': 1, 'was': 1, 'opens': 1, 'himself': 1, 'elsewhere': 1, 'enough': 1, 'becoming': 1, 'but': 1, 'somehow': 1, 'hi': 1, 'ended': 1, 'newer': 1, 'line': 1, 'trying': 1, 'with': 1, 'he': 1, 'usefulness': 1, "they're": 1, 'made': 1, 'places': 1, 'mrs': 1, 'whether': 1, 'wish': 1, 'j': 1, 'up': 1, 'us': 1, 'throug': 1, 'placed': 1, 'below': 1, 'un': 1, 'whim': 1, 'problem': 1, 'z': 1, 'similar': 1, 'noone': 1, "we'd": 1, 'strongly': 1, 'gone': 1, 'sometimes': 1, 'ordered': 1, 'ah': 1, 'describe': 1, 'am': 1, 'general': 1, 'meanwhile': 1, 'as': 1, 'sometime': 1, 'right': 1, 'at': 1, 'our': 1, 'work': 1, 'inc': 1, 'again': 1, 'uucp': 1, "'ll": 1, 'nonetheless': 1, 'greetings': 1, 'na': 1, 'whereas': 1, 'tip': 1, 'backs': 1, 'ourselves': 1, 'til': 1, 'grouped': 1, 'definitely': 1, 'latterly': 1, 'wheres': 1, 'you': 1, 'really': 1, 'concerning': 1, 'showns': 1, 'briefly': 1, "'t": 1, "'s": 1, 'regardless': 1, 'welcome': 1, 'problems': 1, "let's": 1, 'sure': 1, "'d": 1, "'m": 1, 'sides': 1, 'began': 1, 'younger': 1, 'e': 1, 'longer': 1, 'using': 1, 'came': 1, 'backed': 1, 'together': 1, 'hello': 1, 'itself': 1, 'u': 1, 'presenting': 1, 'serious': 1, 'evenly': 1, 'orders': 1, 'once': 1}
def remove_stop_words(curr_line, stop_words):
    refined = []
    splitted = curr_line.split()
    for word in splitted:
        if word not in stop_words:
            refined.append(word)
    return ' '.join(refined)

def remove_punctuations(curr_line):
    return ''.join(c for c in curr_line if c not in string.punctuation)

def get_features(curr_line, glove_dict, seq_length):
    result_line = []
    count = 0
    for word in curr_line.split():
        if word != '': # skip spaces
            if word in glove_dict:
                result_line.append(glove_dict[word])
            else:
                result_line.append(0) # 'UNK
            count += 1
        if count == seq_length:
            break
    if count < seq_length:
        # result_line.extend([0] * (seq_length - count))
        # Another method: put 0s at head
        zeros = [0] * (seq_length - count)
        zeros.extend(result_line)
        return zeros
    return result_line

def load_data(glove_dict):
    data = []

    # unzip and get file list
    unzip_data('reviews.tar.gz')
    file_list = glob.glob('unzipped_reviews/pos/*')
    file_list.extend(glob.glob('unzipped_reviews/neg/*'))

    for f in file_list:
        with open(f, "r") as openf:
            curr_line = openf.read()
            curr_line = curr_line.lower()
            curr_line = remove_stop_words(curr_line, stop_words)
            curr_line = remove_punctuations(curr_line) 
            curr_line = get_features(curr_line, glove_dict, 40)
            data.append(curr_line)
    
    # return np.array(data)
    return np.array(data)

# attention layer
# https://github.com/ilivans/tf-rnn-attention/blob/master/attention.py
# def attention(inputs, attention_size):
#     # check the inputs: for bi-rnn, concat the outputs
#     if isinstance(inputs, tuple):
#         inputs = tf.concat(inputs, 2)
#     sequence_length = inputs.shape[1].value
#     hidden_size = inputs.shape[2].value
#     # Attention mechanism
#     W_omega = tf.Variable(tf.random_normal([hidden_size, attention_size], stddev=0.1))
#     b_omega = tf.Variable(tf.random_normal([attention_size], stddev=0.1))
#     u_omega = tf.Variable(tf.random_normal([attention_size], stddev=0.1))
#     v = tf.tanh(tf.matmul(tf.reshape(inputs, [-1, hidden_size]), W_omega) + tf.reshape(b_omega, [1, -1]))
#     vu = tf.matmul(v, tf.reshape(u_omega, [-1, 1]))
#     exps = tf.reshape(tf.exp(vu), [-1, sequence_length])
#     alphas = exps / tf.reshape(tf.reduce_sum(exps, 1), [-1, 1])
#     # Output of Bi-RNN is reduced with attention vector
#     output = tf.reduce_sum(inputs * tf.reshape(alphas, [-1, sequence_length, 1]), 1)
#     return output

# Attention layer for single RNN
# Yang, Zichao, et al. "Hierarchical Attention Networks for Document Classification." HLT-NAACL. 2016.
def attention(inputs, attention_size):
    # Get parameters for RNN 
    sequence_length = inputs.shape[1].value
    hidden_size = inputs.shape[2].value
    # Implement attention mechanism
    W = tf.Variable(tf.random_normal([hidden_size, attention_size], stddev=0.1))
    b = tf.Variable(tf.random_normal([attention_size], stddev=0.1))
    u = tf.Variable(tf.random_normal([attention_size], stddev=0.1))
    v = tf.tanh(tf.matmul(tf.reshape(inputs, [-1, hidden_size]), W) + tf.reshape(b, [1, -1]))
    vu = tf.matmul(v, tf.reshape(u, [-1, 1]))
    exps = tf.reshape(tf.exp(vu), [-1, sequence_length])
    alphas = exps / tf.reshape(tf.reduce_sum(exps, 1), [-1, 1])
    # compute the output
    output = tf.reduce_sum(inputs * tf.reshape(alphas, [-1, sequence_length, 1]), 1)
    return output



def define_graph(glove_embeddings_arr):

    # Input data
    input_data = tf.placeholder(tf.int32,(batch_size, 40),name='input_data') # 50 * 40
    labels = tf.placeholder(tf.float32,(batch_size, 2),name='labels') # 50 * 2
    keep_prob = tf.placeholder(tf.float32,name='keep_prob')

    # Embedding
    embedding = tf.Variable(tf.convert_to_tensor(glove_embeddings_arr, dtype=tf.float32)) # 注意这里的数据结构
    embed = tf.nn.embedding_lookup(embedding,input_data)

    # lstm_cell: here is GRU
    # def lstm_cell():
    #     lstm = tf.contrib.rnn.GRUCell(lstm_size)
    #     drop = tf.contrib.rnn.DropoutWrapper(lstm, output_keep_prob = keep_prob) # YUNQIUXU
    #     return drop
    def rnn_cell():
        gru = tf.contrib.rnn.GRUCell(rnn_size)
        drop = tf.contrib.rnn.DropoutWrapper(gru, output_keep_prob = keep_prob) # YUNQIUXU
        return drop

    with tf.variable_scope('init_name', initializer=tf.orthogonal_initializer()):
        cell = tf.contrib.rnn.MultiRNNCell([rnn_cell() for _ in range(rnn_layers)])
        outputs, final_state = tf.nn.dynamic_rnn(cell, embed, dtype = "float32")
    
    # single GRU
    # with tf.variable_scope('init_name', initializer=tf.orthogonal_initializer()):
    #     cell = tf.contrib.rnn.MultiRNNCell([lstm_cell() for _ in range(lstm_layers)])
    #     outputs, final_state = tf.nn.dynamic_rnn(cell, embed, dtype = "float32")

    # Attention layer
    attention_output = attention(outputs, attention_size)
    
    # Full connected layer
    W = tf.Variable(tf.truncated_normal([attention_output.get_shape()[1].value, 2], stddev=0.1)) # 128,2
    b = tf.Variable(tf.constant(0., shape=[2])) # 2,
    logits = tf.nn.xw_plus_b(attention_output, W, b)
    logits = tf.squeeze(logits)

    # compute cross entropy
    loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=logits, labels=labels), name = "loss")
    optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.round(tf.sigmoid(logits)), labels), tf.float32), name = "accuracy")

    return input_data, labels, keep_prob, optimizer, accuracy, loss


# def build_train_val(training_data):
#     train_x_pos = training_data[:10000]
#     test_x_pos = training_data[10000:12500]
#     train_x_neg = training_data[12500:22500]
#     test_x_neg = training_data[22500:]
#     train_x_pos.extend(train_x_neg)
#     test_x_pos.extend(test_x_neg)
#     return np.array(train_x_pos), np.array(test_x_pos)# 

# def getTrainBatch():
#     labels = []
#     arr = np.zeros([batch_size, 40])
#     for i in range(batch_size):
#         if (i % 2 == 0):
#             num = randint(0, 9999)
#             labels.append([1, 0])
#         else:
#             num = randint(10000, 19999)
#             labels.append([0, 1])
#         arr[i] = train_x[num]
#     return arr, labels# 

# def getTestBatch_random():
#     labels = []
#     arr = np.zeros([batch_size, 40])
#     for i in range(batch_size):
#         if (i % 2 == 0):
#             num = randint(0, 2499)
#             labels.append([1, 0])
#         else:
#             num = randint(2500, 4999)
#             labels.append([0, 1])
#         arr[i] = test_x[num]
#     return arr, labels

def getTrainBatch():
    labels = []
    arr = np.zeros([batch_size, seq_length])
    for i in range(batch_size):
        if (i % 2 == 0):
            num = randint(0, 12499)
            labels.append([1, 0])
        else:
            num = randint(12500, 24999)
            labels.append([0, 1])
        arr[i] = training_data[num]
    return arr, labels


###########################################################
# Start training
glove_array, glove_dict = load_glove_embeddings()
training_data = load_data(glove_dict)
iterations = 100000
seq_length = 40

input_data, labels, keep_prob, optimizer, accuracy, loss = define_graph(glove_array)
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

for i in tqdm(range(iterations)):
    batch_data, batch_labels = getTrainBatch() # float64
    sess.run(optimizer, {input_data: batch_data, labels: batch_labels, keep_prob: 0.5})
    
    # training
    if (i % 100 == 0):
        loss_value, accuracy_value= sess.run(
            [loss, accuracy],
            {input_data: batch_data, labels: batch_labels, keep_prob: 0.5})
        # writer.add_summary(summary, i)
        print("Iteration: {} , train loss {:.3f}, train acc {:.3f}".format(i, loss_value, accuracy_value))
        with open("024_train_loss.txt", 'a') as f:
            f.write(str(loss_value) + "\n")
        with open("024_train_acc.txt", 'a') as f:
            f.write(str(accuracy_value) + "\n")
    
    # testing
    # if (i % 100 == 0):
    #     test_loss = []
    #     test_acc = []
    #     for t in range(200):
    #         test_data, test_labels = getTestBatch_random()
    #         loss_value, accuracy_value= sess.run(
    #             [loss, accuracy],
    #             {input_data: test_data, labels: test_labels, keep_prob: 1})
    #         test_loss.append(loss_value)
    #         test_acc.append(accuracy_value)
    #     mean_loss = np.mean(test_loss)
    #     mean_acc = np.mean(test_acc)
    #     with open("024_test_loss.txt", 'a') as f:
    #         f.write(str(mean_loss)[:5] + "\n")
    #     with open("024_test_acc.txt", 'a') as f:
    #         f.write(str(mean_acc)[:5] + "\n")
    #     print("Iteration: {} , test loss {:.3f}, test acc {:.3f}".format(i, mean_loss, mean_acc))

sess.close()

