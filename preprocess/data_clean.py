# encoding=utf-8
from textrank4zh import TextRank4Sentence

from db_operation import Mongo

mongo = Mongo()
mongo.set_collection('instrument')

# 去除案件过短的情况
ins_ids = []
for instrument in mongo.find_data({}):
    if len(instrument['case_content']) <= 50: ins_ids.append(instrument['_id'])

for id in ins_ids:
    mongo.delete_by_id(id)

# 对于过长的案件，提取案件摘要作为训练对象
# long_text = ''
# for instrument in mongo.find_data({}):
#     if len(instrument['case']) >= 500:
#         long_text = instrument['case']
#         break
# print long_text
# tr4s = TextRank4Sentence()
# tr4s.analyze(text=long_text, lower=True, source='all_filters')
# for item in tr4s.get_key_sentences(num=5):
#     print item.sentence