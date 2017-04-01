# encoding=utf-8
from db_operation import Mongo

law_id = u'中华人民共和国继承法第十条'

mongo = Mongo()
mongo.set_collection('law')

print law_id + ': '
print mongo.find_data({'law_id': law_id})[0]['law_content']