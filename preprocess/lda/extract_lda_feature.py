# encoding=utf-8
import cPickle as pickle

case_list = pickle.load(open('case_lda.pkl', 'r'))
law_list = pickle.load(open('law_lda.pkl', 'r'))

print case_list[6749]['case_id']
print law_list[0]['law_id']

print case_list[0]['corpus_lda']
print law_list[0]['corpus_lda']