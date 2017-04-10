# encoding=utf-8
import cPickle as pickle

case_list_jieba = pickle.load(open('jieba/participle_case.pkl', 'r'))
case_list_nlpir = pickle.load(open('nlpir/participle_case.pkl', 'r'))

i = 1
line1 = ''
line2 = ''
for tu in case_list_jieba[i]['participle']:
    line1 += '/'.join(tu) + ' '
print line1
for tu in case_list_nlpir[i]['participle']:
    if tu[1]: line2 += tu[0] + '/' + tu[1] + ' '
print line2