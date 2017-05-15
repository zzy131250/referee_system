# encoding=utf-8
import cPickle as pickle

feature_list = pickle.load(open('features.pkl', 'r'))
label_list = pickle.load(open('labels.pkl', 'r'))

small_feature_list = []
small_label_list = []

size = 500

applicable_yes_count = 0
applicable_no_count = 0
for i in range(0, len(feature_list)):
    if applicable_yes_count == size and applicable_no_count == size: break
    if applicable_yes_count < size:
        if label_list[i] == 'yes':
            small_feature_list.append(feature_list[i])
            small_label_list.append(label_list[i])
            applicable_yes_count += 1
            continue
    if applicable_no_count < size:
        if label_list[i] == 'no':
            small_feature_list.append(feature_list[i])
            small_label_list.append(label_list[i])
            applicable_no_count += 1
            continue

print len(feature_list) # 43910
print len(label_list) # 43910
print len(small_feature_list)
print len(small_label_list)

pickle.dump(small_feature_list, open('features_small.pkl', 'w'))
pickle.dump(small_label_list, open('labels_small.pkl', 'w'))