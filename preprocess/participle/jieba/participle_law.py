# encoding=utf-8
import sys
import jieba.posseg as pseg
import cPickle as pickle

sys.path.append('../../')
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('law')

law_list = []
for law in mongo.find_data({}):
    law_item = {}
    law_item['law_id'] = law['law_id']
    law_item['participle'] = []
    for word, flag in pseg.cut(law['law_content']):
        law_item['participle'].append((word, flag))
    law_list.append(law_item)
pickle.dump(law_list, open('participle_law.pkl', 'w'))