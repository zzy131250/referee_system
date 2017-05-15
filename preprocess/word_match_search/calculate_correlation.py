# encoding=utf-8
import cPickle as pickle
import time
import urllib2
from datetime import datetime

from page_parse import get_correlation


def start_calculate_correlation():
    case_verb_list = pickle.load(open('case_verb.pkl', 'r'))
    law_noun_list = pickle.load(open('law_noun.pkl', 'r'))
    case_law_pair_list = pickle.load(open('../word2vec/keyword_similarity.pkl', 'r'))

    word_match_list = pickle.load(open('word_match.pkl', 'r'))
    num = len(word_match_list)
    i_count = pickle.load(open('i_count.pkl', 'r'))

    # 前3个动词与前3个名词搭配
    for i in range(i_count, 49569):
        if num % 50 == 0:
            pickle.dump(word_match_list, open('word_match.pkl', 'w'))
            pickle.dump(i, open('i_count.pkl', 'w'))
            print str(num) + ' pairs done in ' + str(i) + ' pairs ***********************'
        pair = case_law_pair_list[i]
        print pair['case_id'] + ' ' + str(datetime.now())
        word_match_item = {}
        word_match_item['case_id'] = pair['case_id']
        word_match_item['law_id'] = pair['law_id']
        word_match_item['word_match'] = []
        case_verb = []
        law_noun = []
        for case in case_verb_list:
            if case['case_id'] == pair['case_id']:
                case_verb = case['verb']
                break
        for law in law_noun_list:
            if law['law_id'] == pair['law_id']:
                law_noun = law['noun']
                break
        # 动词和名词的集合中可能不包含关键词的案件法条对
        if case_verb == [] or law_noun == []: continue
        for verb in case_verb:
            for noun in law_noun:
                try:
                    word_match_item['word_match'].append(get_correlation(verb, noun))
                except (urllib2.URLError, Exception) as e:
                    print 'catch error, restarting ...'
                    time.sleep(30)
                    # 可考虑exec替换进程，避免递归占内存
                    start_calculate_correlation()
        word_match_list.append(word_match_item)
        num += 1

start_calculate_correlation()