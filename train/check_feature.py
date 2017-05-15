# encoding=utf-8
import cPickle as pickle

feature_list = pickle.load(open('features_small.pkl', 'r'))
label_list = pickle.load(open('labels_small.pkl', 'r'))


for i in range(0, 100):
    print feature_list[i]
    print label_list[i]