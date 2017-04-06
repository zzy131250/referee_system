# encoding=utf-8
import sys
import cPickle as pickle
from jieba import analyse

sys.path.append('../')
from db_operation import Mongo

tr = analyse.textrank
mongo = Mongo()
mongo.set_collection('law')

law_list = []
for law in mongo.find_data({}):
    law_item = {}
    law_item['law_id'] = law['law_id']
    law_item['keyword'] = tr(law['law_content'])
    law_list.append(law_item)
pickle.dump(law_list, open('keyword_law.pkl', 'w'))