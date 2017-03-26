# encoding=utf-8
from db_operation import Mongo
from string_process import find_similar_law

mongo = Mongo()
mongo.set_collection('instrument')

not_applicable_instrument_array = []
for instrument in mongo.find_data({'applicable': 'yes'}):
    not_applicable_instrument = {}
    not_applicable_instrument['case'] = instrument['case']
    not_applicable_instrument['applicable'] = 'no'
    similar_law = find_similar_law(instrument['law_id'])
    print similar_law['law_id_next']
    # print instrument['law_id'] + ', ' + law_id