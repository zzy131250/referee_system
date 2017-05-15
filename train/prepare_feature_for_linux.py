# encoding=utf-8
import cPickle as pickle

small_feature_list = pickle.load(open('features_small.pkl', 'r'))
small_label_list = pickle.load(open('labels_small.pkl', 'r'))

pickle.dump(small_feature_list, open('features_small_b.pkl', 'wb'))
pickle.dump(small_label_list, open('labels_small_b.pkl', 'wb'))