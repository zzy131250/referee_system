# encoding=utf-8
import sys
import cPickle as pickle
from gensim.models import word2vec

sys.path.append('../')
from db_operation import Mongo

case_list = pickle.load(open('keyword_case.pkl', 'r'))
law_list = pickle.load(open('keyword_law.pkl', 'r'))

model = word2vec.Word2Vec.load('w2v.model')

mongo = Mongo()
mongo.set_collection('instrument')

# 数据结构：case_id, law_id, similarity
keyword_similarity_list = []
for case in case_list:
    for instrument in mongo.find_data({'case_id': case['case_id']}):
        for law in law_list:
            if instrument['law_id'] == law['law_id']:
                # 计算案件关键词和法条关键词的关联度
                similarity_item = {}
                similarity_item['case_id'] = case['case_id']
                similarity_item['law_id'] = law['law_id']
                similarity_item['similarity'] = []
                # 增加平均值特征
                similarity_all = []
                for keyword_case in case['keyword']:
                    for keyword_law in law['keyword']:
                        # 会有不在模型的词汇表中的情况
                        if keyword_case in model.wv.vocab and keyword_law in model.wv.vocab:
                            similarity_all.append(model.similarity(keyword_case, keyword_law))
                if len(similarity_all) == 0: continue
                similarity_item['similarity'].append(sum(similarity_all) / len(similarity_all))
                case['keyword'] = [case['keyword'][0], case['keyword'][1], case['keyword'][2]]
                law['keyword'] = [law['keyword'][0], law['keyword'][1], law['keyword'][2]]
                for keyword_case in case['keyword']:
                    for keyword_law in law['keyword']:
                        # 会有不在模型的词汇表中的情况
                        if keyword_case in model.wv.vocab and keyword_law in model.wv.vocab:
                            similarity_item['similarity'].append(model.similarity(keyword_case, keyword_law))
                # similarity_item['similarity'].sort(reverse=True)
                if len(similarity_item['similarity']) >= 9: keyword_similarity_list.append(similarity_item)
print len(keyword_similarity_list) # 49569
pickle.dump(keyword_similarity_list, open('keyword_similarity.pkl', 'w'))