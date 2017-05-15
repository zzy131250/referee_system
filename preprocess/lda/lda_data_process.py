# encoding=utf-8
import cPickle as pickle

case_list = pickle.load(open('case_lda.pkl', 'r'))
law_list = pickle.load(open('law_lda.pkl', 'r'))

# 计算主题数范围
max_topic = 0
min_topic = 25
for case in case_list:
    if len(case['corpus_lda']) > max_topic: max_topic = len(case['corpus_lda'])
    if len(case['corpus_lda']) < min_topic: min_topic = len(case['corpus_lda'])
for law in law_list:
    if len(case['corpus_lda']) > max_topic: max_topic = len(case['corpus_lda'])
    if len(case['corpus_lda']) < min_topic: min_topic = len(case['corpus_lda'])

print max_topic
print min_topic

# 为主题数不满的文书和法条添加主题
for case in case_list:
    topic_ids = []
    for tuple in case['corpus_lda']: topic_ids.append(tuple[0])
    for i in range(0, 25):
        if i not in topic_ids: case['corpus_lda'].append((i, 0))
    case['corpus_lda'].sort(key=lambda tup: tup[0])

for law in law_list:
    topic_ids = []
    for tuple in law['corpus_lda']: topic_ids.append(tuple[0])
    for i in range(0, 25):
        if i not in topic_ids: law['corpus_lda'].append((i, 0))
    law['corpus_lda'].sort(key=lambda tup: tup[0])

pickle.dump(case_list, open('case_lda_processed.pkl', 'w'))
pickle.dump(law_list, open('law_lda_processed.pkl', 'w'))