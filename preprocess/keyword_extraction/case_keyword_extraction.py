# encoding=utf-8
import sys
import cPickle as pickle
from jieba import analyse

sys.path.append('../')
from db_operation import Mongo

file_list = '../case_list/not_withdrawal_case.txt'
analyse.set_stop_words('../stop_words.txt')
tr = analyse.textrank
mongo = Mongo()
mongo.set_collection('instrument')

case_list = []
with open(file_list, 'r') as cases:
    for case_id in cases:
        case_item = {}
        case_item['case_id'] = case_id[:-1]
        for case in mongo.find_data({'case_id': case_id[:-1]}):
            case_item['keyword'] = tr(case['case_content'])
            break
        if 'keyword' in case_item: case_list.append(case_item)
print len(case_list) # 6750
pickle.dump(case_list, open('keyword_case.pkl', 'w'))
