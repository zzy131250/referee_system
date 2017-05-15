# encoding=utf-8
from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('instrument')

# 去除案件过短的情况
ins_ids = []
for instrument in mongo.find_data({}):
    if len(instrument['case_content']) <= 50: ins_ids.append(instrument['_id'])

for id in ins_ids:
    mongo.delete_by_id(id)