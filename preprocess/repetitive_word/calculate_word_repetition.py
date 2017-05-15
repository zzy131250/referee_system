# encoding=utf-8
import sys
import cPickle as pickle

sys.path.append('../')
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('instrument')

case_list = pickle.load(open('../participle/nlpir/participle_case_cleaned.pkl', 'r'))
law_list = pickle.load(open('../participle/nlpir/participle_law_cleaned.pkl', 'r'))

repetitive_word_list = []
cursor = mongo.find_data({}, no_cursor_timeout=True)
for instrument in cursor:
    repetitive_word_item = {}
    repetitive_word_item['case_id'] = instrument['case_id']
    repetitive_word_item['law_id'] = instrument['law_id']
    repetitive_word_item['repetitive_word_count'] = 0
    case_participle = []
    law_participle = []
    for case_p in case_list:
        if case_p['case_id'] == instrument['case_id']:
            case_participle = case_p['participle']
            break
    for law_p in law_list:
        if law_p['law_id'] == instrument['law_id']:
            law_participle = law_p['participle']
            break
    for tup_c in case_participle:
        for tup_l in law_participle:
            # 去除标点
            if tup_c[0] == tup_l[0] and tup_c[1] != 'punctuation mark':
                repetitive_word_item['repetitive_word_count'] += 1
                continue
    repetitive_word_list.append(repetitive_word_item)

print len(repetitive_word_list) # 65875

pickle.dump(repetitive_word_list, open('repetitive_word.pkl', 'w'))