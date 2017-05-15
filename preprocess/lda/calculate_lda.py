# encoding=utf-8
import cPickle as pickle
from gensim import corpora
from gensim.models import LdaModel, TfidfModel

case_list = pickle.load(open('../participle/nlpir/participle_case_cleaned.pkl', 'r'))
law_list = pickle.load(open('../participle/nlpir/participle_law_cleaned.pkl', 'r'))

# stop_words = []
# with open('../stop_words.txt', 'r') as f:
#     for word in f: stop_words.append(word.strip().decode('utf-8'))

# 准备语料
case_ids = []
law_ids = []
sentences = []
for case in case_list:
    sentence = []
    for tuple in case['participle']:
        # if tuple[0] not in stop_words:
        sentence.append(tuple[0])
    case_ids.append(case['case_id'])
    sentences.append(sentence)

for law in law_list:
    sentence = []
    for tuple in law['participle']:
        # if tuple[0] not in stop_words:
        sentence.append(tuple[0])
    law_ids.append(law['law_id'])
    sentences.append(sentence)

print len(sentences) # 11588
pickle.dump(sentences, open('lda_corpus.pkl', 'w'))

# 构造词典
dic = corpora.Dictionary(sentences)
dic.save('dic')
# 生成语料库
corpus = [ dic.doc2bow(sentence) for sentence in sentences ]
# 计算tfidf
tfidf = TfidfModel(corpus)
tfidf.save('tfidf.model')
corpus_tfidf = tfidf[corpus]
# 训练lda
lda = LdaModel(corpus_tfidf, id2word=dic, num_topics=25)
lda.save('lda.model')
# 得到各篇文档在各个主题上的概率分布
corpus_lda = lda[corpus_tfidf]

case_lda = []
i = 0
while i < len(case_ids):
    lda_item = {}
    lda_item['case_id'] = case_ids[i]
    lda_item['corpus_lda'] = corpus_lda[i]
    case_lda.append(lda_item)
    i += 1
pickle.dump(case_lda, open('case_lda.pkl', 'w'))

print len(case_ids) # 6750

law_lda = []
while i < len(case_ids) + len(law_ids):
    lda_item = {}
    lda_item['law_id'] = law_ids[i-len(case_ids)]
    lda_item['corpus_lda'] = corpus_lda[i]
    law_lda.append(lda_item)
    i += 1
pickle.dump(law_lda, open('law_lda.pkl', 'w'))