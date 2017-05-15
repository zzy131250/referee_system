# encoding=utf-8
import cPickle as pickle

# 去除词性为None的分词结果
case_list_nlpir = pickle.load(open('participle_case.pkl', 'r'))
law_list_nlpir = pickle.load(open('participle_law.pkl', 'r'))

for case in case_list_nlpir:
    case['participle'] = [tup for tup in case['participle'] if tup[1] != None]

for law in law_list_nlpir:
    law['participle'] = [tup for tup in law['participle'] if tup[1] != None]

pickle.dump(case_list_nlpir, open('participle_case_cleaned.pkl', 'w'))
pickle.dump(law_list_nlpir, open('participle_law_cleaned.pkl', 'w'))