# encoding=utf-8
import sys
import cPickle as pickle

sys.path.append('../')
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('instrument')

# 显示案件、适用法条、不适用法条主题分布差
case_list = pickle.load(open('case_lda_processed.pkl', 'r'))
law_list = pickle.load(open('law_lda_processed.pkl', 'r'))

for case in case_list:
    for ins in mongo.find_data({'case_id': case['case_id'], 'applicable': 'yes'}):
        for law in law_list:
            if law['law_id'] == ins['law_id']:
                print [case['corpus_lda'][i][1]-law['corpus_lda'][i][1] for i in range(0, 25)]
                break
        break
    for ins in mongo.find_data({'case_id': case['case_id'], 'applicable': 'no'}):
        for law in law_list:
            if law['law_id'] == ins['law_id']:
                print [case['corpus_lda'][i][1]-law['corpus_lda'][i][1] for i in range(0, 25)]
                break
        break
    print