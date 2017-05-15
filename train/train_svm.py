# encoding=utf-8
import cPickle as pickle
import numpy as np

from datetime import datetime
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

feature_list = pickle.load(open('features_small.pkl', 'r'))
label_list = pickle.load(open('labels_small.pkl', 'r'))


class TrainSvm:

    def __init__(self):
        pass

    def train_svm(self, features, labels):
        # 可使用k折交叉验证
        features_train, features_test, labels_train, labels_test = \
            cross_validation.train_test_split(np.array(features), np.array(labels), test_size=0.5, random_state=42)

        count = 0
        for label in labels_train:
            if label == 'yes': count += 1
        print '训练集适用法条：' + str(count)
        count = 0
        for label in labels_test:
            if label == 'yes': count += 1
        print '测试集适用法条：' + str(count)

        clf = SVC(kernel="rbf", C=1)
        print 'start fitting ' + str(datetime.now())
        clf.fit(features_train, labels_train)
        print 'start predicting ' + str(datetime.now())
        pred = clf.predict(features_test)
        print '准确率：' + str(accuracy_score(pred, labels_test))

        # 计算精确率
        precision = 0.0
        for i in range(0, len(pred)):
            if pred[i] == 'yes' and labels_test[i] == 'yes': precision += 1
        positive = 0.0
        for p in pred:
            if p == 'yes': positive += 1
        print '精确率：' + str(precision / positive)

        # 计算召回率
        recall = 0.0
        for i in range(0, len(pred)):
            if pred[i] == 'yes' and labels_test[i] == 'yes': recall += 1
        tr = 0.0
        for t in labels_test:
            if t == 'yes': tr += 1
        print '召回率：' + str(recall / tr)

        pickle.dump(clf, open('svm_model.pkl', 'w'))

TrainSvm().train_svm(feature_list, label_list)

# lda(未去停用词)
# 10000条, kernel="rbf"   , C=1000, 0.621
# 10000条, kernel="rbf"   , C=100,  0.603
# 10000条, kernel="rbf"   , C=10,   0.605
# 10000条, kernel="rbf"   , C=1,    0.567
# 10000条, kernel="linear", C=1000, 0.577
# 10000条, kernel="linear", C=100,  0.576
# 10000条, kernel="linear", C=10,   0.577
# 10000条, kernel="linear", C=1,    0.577
# lda(去停用词)
# 10000条, kernel="rbf"   , C=100000, 0.725
# 10000条, kernel="rbf"   , C=10000, 0.693
# 10000条, kernel="rbf"   , C=1000, 0.668
# 10000条, kernel="rbf"   , C=100,  0.627
# 10000条, kernel="rbf"   , C=10,   0.587
# 10000条, kernel="rbf"   , C=1,    0.561
# 10000条, kernel="linear", C=1000, 0.571
# 10000条, kernel="linear", C=100,  0.572
# 10000条, kernel="linear", C=10,   0.571
# 10000条, kernel="linear", C=1,    0.581
# word2vec, 3 * 3, 相似度未排序, 真正平均数
# 10000条, kernel="rbf"   , C=1000, 0.607
# 10000条, kernel="rbf"   , C=100 , 0.608
# 10000条, kernel="rbf"   , C=10  , 0.59
# 10000条, kernel="rbf"   , C=1   , 0.528
# 10000条, kernel="linear", C=1000, 0.53
# 10000条, kernel="linear", C=100 , 0.53
# 10000条, kernel="linear", C=10  , 0.53
# 10000条, kernel="linear", C=1   , 0.529
# 词语搭配 **********************
# 10000条, kernel="rbf"   , C=1000, 0.621
# 10000条, kernel="rbf"   , C=100 , 0.621
# 10000条, kernel="rbf"   , C=10  , 0.621
# 10000条, kernel="rbf"   , C=1   , 0.62
# 10000条, kernel="linear", C=1000, 0.53
# 10000条, kernel="linear", C=100 , 0.53
# 10000条, kernel="linear", C=10  , 0.53
# 10000条, kernel="linear", C=1   , 0.529
# word2vec + lda
# 10000条, kernel="rbf"   , C=1000, 0.703
# 10000条, kernel="rbf"   , C=100 , 0.661
# 10000条, kernel="rbf"   , C=10  , 0.635
# 10000条, kernel="rbf"   , C=1   , 0.61
# 10000条, kernel="linear", C=1000, 0.623
# 10000条, kernel="linear", C=100 , 0.624
# 10000条, kernel="linear", C=10  , 0.625
# 10000条, kernel="linear", C=1   , 0.622
# word2vec + lda + 重复词  特别慢
# 10000条, kernel="rbf"   , C=1000, 0.649
# 10000条, kernel="rbf"   , C=100 , 0.648
# 10000条, kernel="rbf"   , C=10  , 0.61
# 10000条, kernel="rbf"   , C=1   , 0.559
# 10000条, kernel="linear", C=1000, 0.612
# 10000条, kernel="linear", C=100 , 0.623
# lda + word2vec + 搭配
# 10000条, kernel="rbf"   , C=1000, 0.7
# lda + 搭配
# 10000条, kernel="rbf"   , C=1000, 0.696