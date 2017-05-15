# encoding=utf-8
import cPickle as pickle
import numpy as np
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

feature_list = pickle.load(open('features.pkl', 'r'))
label_list = pickle.load(open('labels.pkl', 'r'))

# 可使用k折交叉验证
features_train, features_test, labels_train, labels_test = \
    cross_validation.train_test_split(np.array(feature_list), np.array(label_list), test_size=0.1, random_state=42)

clf = GaussianNB()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print accuracy_score(pred, labels_test)

# word2vec              , 全部数据, 0.569
# word2vec + lda        , 全部数据, 0.597
# word2vec + lda + 重复词, 全部数据, 0.596