# encoding=utf-8
import sys
import pynlpir
import cPickle as pickle

sys.path.append('../../')
from db_operation import Mongo

file_list = '../../case_list/not_withdrawal_case.txt'
mongo = Mongo()
mongo.set_collection('instrument')

case_list = []
pynlpir.open()
with open(file_list, 'r') as cases:
    for case_id in cases:
        case_item = {}
        case_item['case_id'] = case_id[:-1]
        for case in mongo.find_data({'case_id': case_id[:-1]}):
            case_item['participle'] = pynlpir.segment(case['case_content'])
            break
        case_list.append(case_item)
pynlpir.close()
print len(case_list) # 8141
pickle.dump(case_list, open('participle_case.pkl', 'w'))