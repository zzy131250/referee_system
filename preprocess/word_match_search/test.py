# encoding=utf-8
import cPickle as pickle

word_match_list = pickle.load(open('word_match.pkl', 'r'))
print word_match_list[1000]