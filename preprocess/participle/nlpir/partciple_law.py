# encoding=utf-8
import sys
import pynlpir
import cPickle as pickle

sys.path.append('../../')
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('law')

law_list = []
pynlpir.open()
for law in mongo.find_data({}):
    law_item = {}
    law_item['law_id'] = law['law_id']
    law_item['participle'] = pynlpir.segment(law['law_content'])
    law_list.append(law_item)
pynlpir.close()
pickle.dump(law_list, open('participle_law.pkl', 'w'))