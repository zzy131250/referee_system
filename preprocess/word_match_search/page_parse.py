# encoding=utf-8
import random
import urllib2
from bs4 import BeautifulSoup

baidu_ip_list = [
    '119.75.213.50',
    '119.75.213.51',
    '119.75.213.61',
    '119.75.216.20',
    '119.75.217.56',
    '119.75.218.70',
    '202.108.22.142',
    '202.108.22.5',
    '220.181.111.148',
    '220.181.37.55',
    '220.181.6.175',
    '61.135.169.105',
    '61.135.169.125'
]


def get_correlation(verb, noun):
    """
    获取动词与名词的距离
    """
    url = 'http://' + random.choice(baidu_ip_list) + '/s?wd=' + verb.encode('gbk') + '+' + noun.encode('gbk')
    content_list = get_content(url)
    return calculate_correlation(content_list, verb, noun)


def get_content(url):
    """
    获取百度搜索页前10个标题
    """
    # proxy_handler = urllib2.ProxyHandler({'http': random.choice(proxy_ip_list)})
    # opener = urllib2.build_opener(proxy_handler)
    # urllib2.install_opener(opener)

    request = urllib2.Request(url)
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')

    response = urllib2.urlopen(request, timeout=10)
    dom = BeautifulSoup(response.read(), 'lxml')
    content_list = [content.a.get_text() for content in dom.find_all('h3', class_='t')]
    return content_list


def calculate_correlation(content_list, verb, noun):
    """
    计算距离平均值
    """
    distance = []
    for content in content_list:
        # 规则：-1, -1 —— len(content)
        #     -1, other —— len(content)-len(word)
        #     other, -1 —— len(content)-len(word)
        #     other, other —— 中间词语的个数
        #     最后计算平均数，这样把没全出现的也考虑了进去
        verb_index = content.find(verb)
        noun_index = content.find(noun)
        if verb_index == -1 and noun_index == -1: distance.append(len(content))
        elif verb_index == -1 and noun_index != -1: distance.append(len(content)-len(noun))
        elif verb_index != -1 and noun_index == -1: distance.append(len(content)-len(verb))
        else:
            if verb_index < noun_index: distance.append(noun_index-verb_index-len(verb))
            else: distance.append(verb_index-noun_index-len(noun))
    return sum(distance) / len(distance)