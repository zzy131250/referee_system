# encoding=utf-8
import sys
import cPickle as pickle

sys.path.append('../preprocess/')
from db_operation import Mongo

case_lda_list = pickle.load(open('../preprocess/lda/case_lda_processed.pkl', 'r'))
law_lda_list = pickle.load(open('../preprocess/lda/law_lda_processed.pkl', 'r'))

mongo = Mongo()
mongo.set_collection('instrument')

# 计算案件、法条对的lda主题差值
cursor = mongo.find_data({}, no_cursor_timeout=True)
lda_difference_list = []
for instrument in cursor:
    lda_difference = {}
    lda_difference['case_id'] = instrument['case_id']
    lda_difference['law_id'] = instrument['law_id']
    case_lda = []
    law_lda = []
    for case_l in case_lda_list:
        if instrument['case_id'] == case_l['case_id']: case_lda = case_l['corpus_lda']
    for law_l in law_lda_list:
        if instrument['law_id'] == law_l['law_id']: law_lda = law_l['corpus_lda']
    if len(case_lda) != 0 and len(law_lda) != 0:
        lda_difference['lda_diff'] = [case_lda[i][1]-law_lda[i][1] for i in range(0, len(case_lda))]
        lda_difference_list.append(lda_difference)
print len(lda_difference_list) # 62570
pickle.dump(lda_difference_list, open('lda_feature.pkl', 'w'))