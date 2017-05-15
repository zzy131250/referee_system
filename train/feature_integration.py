# encoding=utf-8
import sys
import cPickle as pickle

sys.path.append('../preprocess')
from db_operation import Mongo

repetitive_word_list = pickle.load(open('../preprocess/repetitive_word/repetitive_word.pkl', 'r'))
word2vec_feature_list = pickle.load(open('w2v_feature.pkl', 'r'))
lda_feature_list = pickle.load(open('lda_feature.pkl', 'r'))
word_match_feature_list = pickle.load(open('../preprocess/word_match_search/word_match.pkl', 'r'))

mongo = Mongo()
mongo.set_collection('instrument')

integrated_feature_list = []
label_list = []
for w2v_feature in word2vec_feature_list:
    for wm_feature in word_match_feature_list:
        if w2v_feature['case_id'] == wm_feature['case_id'] and w2v_feature['law_id'] == wm_feature['law_id']:
            integrated_feature = []
            # 添加word2vec
            for f in w2v_feature['w2v_f']: integrated_feature.append(f)
            # 添加重复词特征
            # for repetitive_word in repetitive_word_list:
            #     if repetitive_word['case_id'] == w2v_feature['case_id'] and repetitive_word['law_id'] == w2v_feature['law_id']:
            #         integrated_feature.append(repetitive_word['repetitive_word_count'])
            #         break
            # 添加lda特征
            for lda_feature in lda_feature_list:
                if lda_feature['case_id'] == w2v_feature['case_id'] and lda_feature['law_id'] == w2v_feature['law_id']:
                    for f in lda_feature['lda_diff']: integrated_feature.append(f)
                    break
            # 添加词语搭配特征
            for word_match_feature in wm_feature['word_match']:
                integrated_feature.append(word_match_feature)

            integrated_feature_list.append(integrated_feature)
            # 添加label
            instrument = mongo.find_data({'case_id': w2v_feature['case_id'], 'law_id': w2v_feature['law_id']})[0]
            label_list.append(instrument['applicable'])

print len(integrated_feature_list) # 43910

pickle.dump(integrated_feature_list, open('features.pkl', 'w'))
pickle.dump(label_list, open('labels.pkl', 'w'))