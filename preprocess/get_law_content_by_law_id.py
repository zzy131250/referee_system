# encoding=utf-8
from db_operation import Mongo

law_id = u'最高人民法院关于审理人身损害赔偿案件适用法律若干问题的解释第十七条'

mongo = Mongo()
mongo.set_collection('law')

print law_id + ': '
print mongo.find_data({'law_id': law_id})[0]['law_content']