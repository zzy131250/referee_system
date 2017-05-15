# encoding=utf-8
import cPickle as pickle

case_keyword_list = pickle.load(open('../word2vec/keyword_case.pkl', 'r'))
law_keyword_list = pickle.load(open('../word2vec/keyword_law.pkl', 'r'))

# 词性参考
case_participle_list = pickle.load(open('../participle/jieba/participle_case.pkl', 'r'))
law_participle_list= pickle.load(open('../participle/jieba/participle_law.pkl', 'r'))

# 从案件关键词中提取动词
case_verb_list = []
for case in case_keyword_list:
    case_item = {}
    case_item['case_id'] = case['case_id']
    case_item['verb'] = []
    case_participle = []
    case_keyword = []
    for case_p in case_participle_list:
        if case['case_id'] == case_p['case_id']: case_participle = case_p['participle']
    for case_k in case_keyword_list:
        if case['case_id'] == case_k['case_id']: case_keyword = case_k['keyword']
    for keyword in case_keyword:
        for tup in case_participle:
            if tup[0] == keyword:
                if tup[1].startswith('v'): case_item['verb'].append(tup[0])
                break
    if len(case_item['verb']) < 3: continue
    else: case_item['verb'] = [case_item['verb'][0], case_item['verb'][1], case_item['verb'][2]]
    case_verb_list.append(case_item)

print len(case_verb_list) # 6490

# 从法条关键词中提取名词
law_noun_list = []
for law in law_keyword_list:
    law_item = {}
    law_item['law_id'] = law['law_id']
    law_item['noun'] = []
    law_participle = []
    law_keyword = []
    for law_p in law_participle_list:
        if law['law_id'] == law_p['law_id']: law_participle = law_p['participle']
    for law_k in law_keyword_list:
        if law['law_id'] == law_k['law_id']: law_keyword = law_k['keyword']
    for keyword in law_keyword:
        for tup in law_participle:
            if tup[0] == keyword:
                if tup[1].startswith('n'): law_item['noun'].append(tup[0])
                break
    if len(law_item['noun']) < 3: continue
    else: law_item['noun'] = [law_item['noun'][0], law_item['noun'][1], law_item['noun'][2]]
    law_noun_list.append(law_item)

print len(law_noun_list) # 4498

pickle.dump(case_verb_list, open('case_verb.pkl', 'w'))
pickle.dump(law_noun_list, open('law_noun.pkl', 'w'))