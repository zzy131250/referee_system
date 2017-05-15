# encoding=utf-8
import sys
import cPickle as pickle

sys.path.append('../')
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('instrument')

case_list_nlpir = pickle.load(open('nlpir/participle_case_cleaned.pkl', 'r'))
law_list_nlpir = pickle.load(open('nlpir/participle_law_cleaned.pkl', 'r'))

# 显示案件、适用法条、不适用法条及其词性
for case in case_list_nlpir:
    print ' '.join([tuple[0] for tuple in case['participle']])
    for ins in mongo.find_data({'case_id': case['case_id'], 'applicable': 'yes'}):
        for law in law_list_nlpir:
            if law['law_id'] == ins['law_id']:
                print ' '.join([tuple[0] for tuple in law['participle']])
                break
        break
    for ins in mongo.find_data({'case_id': case['case_id'], 'applicable': 'no'}):
        for law in law_list_nlpir:
            if law['law_id'] == ins['law_id']:
                print ' '.join([tuple[0] for tuple in law['participle']])
                break
        break
    print