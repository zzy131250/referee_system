# encoding=utf-8
import cPickle as pickle

case_list = pickle.load(open('../keyword_extraction/keyword_case.pkl', 'r'))
law_list = pickle.load(open('../keyword_extraction/keyword_law.pkl', 'r'))

# 清理关键词个数不够的案件和法条
case_list = [case for case in case_list if len(case['keyword']) >= 3]
print len(case_list) # 6711
law_list = [law for law in law_list if len(law['keyword']) >= 3]
print len(law_list) # 4786

pickle.dump(case_list, open('keyword_case.pkl', 'w'))
pickle.dump(law_list, open('keyword_law.pkl', 'w'))