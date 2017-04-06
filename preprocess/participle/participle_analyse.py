# encoding=utf-8
import cPickle as pickle

case_list = pickle.load(open('jieba/participle_case.pkl', 'r'))
for case in case_list:
    for item in case['participle']:
        print item[0]