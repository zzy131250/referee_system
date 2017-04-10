# encoding=utf-8
import cPickle as pickle

case_list = pickle.load(open('../keyword_extraction/keyword_case.pkl', 'r'))
law_list = pickle.load(open('../keyword_extraction/keyword_law.pkl', 'r'))

# 清理关键词个数不够的案件和法条
for case in case_list:
    if len(case['keyword']) < 5: case_list.remove(case)
print len(case_list) # 6619
for law in law_list:
    if len(law['keyword']) < 2: law_list.remove(law)
print len(law_list) # 4806

pickle.dump(case_list, open('keyword_case.pkl', 'w'))
pickle.dump(law_list, open('keyword_law.pkl', 'w'))