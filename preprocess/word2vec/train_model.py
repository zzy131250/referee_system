# encoding=utf-8
import cPickle as pickle
from gensim.models import word2vec

case_list = pickle.load(open('../participle/jieba/participle_case.pkl', 'r'))
law_list = pickle.load(open('../participle/jieba/participle_law.pkl', 'r'))

# 准备语料
sentences = []
for case in case_list:
    sentence = []
    for tuple in case['participle']: sentence.append(tuple[0])
    sentences.append(sentence)

for law in law_list:
    sentence = []
    for tuple in law['participle']: sentence.append(tuple[0])
    sentences.append(sentence)

# 后续可考虑参数问题
model = word2vec.Word2Vec(sentences, min_count=10, size=300, iter=15)

for item in model.most_similar(u'借款', topn=10):
    print item[0], item[1]

print

for item in model.most_similar(u'婚姻', topn=10):
    print item[0], item[1]

model.save('w2v.model')