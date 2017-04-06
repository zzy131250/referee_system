# encoding=utf-8
import sys
import cPickle as pickle

sys.path.append('../')
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('instrument')

case_list = pickle.load(open('keyword_case.pkl', 'r'))
law_list = pickle.load(open('keyword_law.pkl', 'r'))

for case in case_list:
    print ' '.join(case['keyword'])
    for ins in mongo.find_data({'case_id': case['case_id'], 'applicable': 'yes'}):
        for item in law_list:
            if item['law_id'] == ins['law_id']:
                print ' '.join(item['keyword'])
        break
    print