# encoding=utf-8
from db_operation import Mongo
from string_process import find_similar_law

mongo_instrument = Mongo()
mongo_instrument.set_collection('instrument')
mongo_law = Mongo()
mongo_law.set_collection('law')

not_applicable_instrument_array = []
for instrument in mongo_instrument.find_data({'applicable': 'yes'}):
    not_applicable_instrument = {}
    not_applicable_instrument['case'] = instrument['case']
    not_applicable_instrument['applicable'] = 'no'
    result = mongo_law.find_data({'law_id': instrument['law_id']})
    if result.count() == 1:
        similar_law = find_similar_law(result[0]['law_id'])
        law_previous = mongo_law.find_data({'law_id': similar_law['law_id_previous']})
        law_next = mongo_law.find_data({'law_id': similar_law['law_id_next']})
        if law_previous.count() == 0:
            not_applicable_instrument['law_id'] = law_next[0]['law_id']
        elif law_next.count() == 0:
            not_applicable_instrument['law_id'] = law_previous[0]['law_id']
        else:
            if len(law_previous[0]['law_content']) < len(law_next[0]['law_content']):
                not_applicable_instrument['law_id'] = law_next[0]['law_id']
            else:
                not_applicable_instrument['law_id'] = law_previous[0]['law_id']
        not_applicable_instrument_array.append(not_applicable_instrument)
mongo_instrument.insert_many(not_applicable_instrument_array)