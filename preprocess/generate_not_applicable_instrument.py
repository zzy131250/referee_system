# encoding=utf-8
from db_operation import Mongo
from string_process import find_similar_law

mongo_instrument = Mongo()
mongo_instrument.set_collection('instrument')
mongo_law = Mongo()
mongo_law.set_collection('law')

not_applicable_instrument_array = []
cursor = mongo_instrument.find_data({'applicable': 'yes'}, no_cursor_timeout=True)
for instrument in cursor:
    not_applicable_instrument = {}
    not_applicable_instrument['case_id'] = instrument['case_id']
    not_applicable_instrument['case_content'] = instrument['case_content']
    not_applicable_instrument['applicable'] = 'no'
    result = mongo_law.find_data({'law_id': instrument['law_id']})
    if result.count() == 1:
        similar_law = find_similar_law(result[0]['law_id'])
        # 查询前一条法条跟后一条法条是否也是适用的
        previous_also_applicable = False
        next_also_applicable = False
        for ins in mongo_instrument.find_data({'case_id': instrument['case_id'], 'applicable': 'yes'}):
            if ins['law_id'] == similar_law['law_id_previous']: previous_also_applicable = True
            if ins['law_id'] == similar_law['law_id_next']: next_also_applicable = True
        law_previous = mongo_law.find_data({'law_id': similar_law['law_id_previous']})
        law_next = mongo_law.find_data({'law_id': similar_law['law_id_next']})
        # 没有前一条
        if law_previous.count() == 0:
            # 后一条不是适用的法条
            if not next_also_applicable:
                not_applicable_instrument['law_id'] = law_next[0]['law_id']
            else: continue
        # 没有后一条
        elif law_next.count() == 0:
            # 前一条不是适用的法条
            if not previous_also_applicable:
                not_applicable_instrument['law_id'] = law_previous[0]['law_id']
            else: continue
        else:
            if previous_also_applicable and not next_also_applicable: not_applicable_instrument['law_id'] = law_next[0]['law_id']
            elif not previous_also_applicable and next_also_applicable: not_applicable_instrument['law_id'] = law_previous[0]['law_id']
            elif not previous_also_applicable and not next_also_applicable:
                if len(law_previous[0]['law_content']) < len(law_next[0]['law_content']):
                    not_applicable_instrument['law_id'] = law_next[0]['law_id']
                else:
                    not_applicable_instrument['law_id'] = law_previous[0]['law_id']
            else: continue
        not_applicable_instrument_array.append(not_applicable_instrument)
cursor.close()
mongo_instrument.insert_many(not_applicable_instrument_array)