# encoding=utf-8
import cPickle as pickle

keyword_similarity_list = pickle.load(open('../preprocess/word2vec/keyword_similarity.pkl', 'r'))

word2vec_feature_list = []
for pair in keyword_similarity_list:
    word2vec_feature = {}
    word2vec_feature['case_id'] = pair['case_id']
    word2vec_feature['law_id'] = pair['law_id']
    # 挑选前10个关联度
    word2vec_feature['w2v_f'] = [pair['similarity'][i] for i in range(0, 10)]
    word2vec_feature_list.append(word2vec_feature)
print len(word2vec_feature_list) # 49569
pickle.dump(word2vec_feature_list, open('w2v_feature.pkl', 'w'))