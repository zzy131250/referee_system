# encoding=utf-8
import sys
import jieba.posseg as pseg
import cPickle as pickle

sys.path.append('../../')
from db_operation import Mongo

file_list = '../../case_list/not_withdrawal_case.txt'
mongo = Mongo()
mongo.set_collection('instrument')

case_list = []
with open(file_list, 'r') as cases:
    for case_id in cases:
        case_item = {}
        case_item['case_id'] = case_id[:-1]
        case_item['participle'] = []
        for case in mongo.find_data({'case_id': case_id[:-1]}):
            for word, flag in pseg.cut(case['case_content']):
                case_item['participle'].append((word, flag))
            break
        case_list.append(case_item)
print len(case_list) # 8141
pickle.dump(case_list, open('participle_case.pkl', 'w'))