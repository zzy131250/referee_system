# encoding=utf-8
from db_operation import Mongo
mongo = Mongo()
mongo.set_collection('instrument')


def modify_law_id(law):
    """
    去除法条书名号，去除款号和项号
    """
    law = law.replace(u'《', '')
    law = law.replace(u'》', '')
    law = law.replace(u'〈', '')
    law = law.replace(u'〉', '')
    law = law.replace(u'﹤', '')
    law = law.replace(u'﹥', '')
    index = law.rfind(u'条')
    law = law[:index+1]
    return law


def find_similar_law(law):
    """
    计算前一条和后一条法条的编号 
    """
    # 提取数字
    number_dict = {u'零': 0, u'一': 1, u'二': 2, u'三': 3, u'四': 4, u'五': 5, u'六': 6, u'七': 7, u'八': 8, u'九': 9}
    front_index = law.rfind(u'第')
    behind_index = law.rfind(u'条')
    number_chn = law[front_index+1: behind_index]
    number = 0
    # 中文数字转阿拉伯数字
    for character in number_chn:
        if character == u'十' or character == u'百': continue
        number = number*10 + number_dict[character]
    if number_chn[-1] == u'百': number *= 100
    if number_chn[-1] == u'十': number *= 10
    if number_chn[0] == u'十': number += 10
    return {'law_id_previous': law[:front_index+1] + arabic_number_to_chn(number - 1) + law[behind_index:],
            'law_id_next': law[:front_index+1] + arabic_number_to_chn(number + 1) + law[behind_index:]}


def arabic_number_to_chn(number):
    """
    阿拉伯数字转中文数字
    """
    number_dict = {'0': u'零', '1': u'一', '2': u'二', '3': u'三', '4': u'四', '5': u'五', '6': u'六', '7': u'七', '8': u'八', '9': u'九'}
    number_str = str(number)
    if len(number_str) == 1: return number_dict[number_str]
    if len(number_str) == 2:
        if number_str[0] == '1':
            if number_str[1] == '0': return u'十'
            else: return u'十' + number_dict[number_str[1]]
        if number_str[1] == '0': return number_dict[number_str[0]] + u'十'
        else: return number_dict[number_str[0]] + u'十' + number_dict[number_str[1]]
    if len(number_str) == 3:
        if number_str[1] == '0' and number_str[2] == '0':
            return number_dict[number_str[0]] + u'百'
        if number_str[2] == '0':
            return number_dict[number_str[0]] + u'百' + number_dict[number_str[1]] + u'十'
        if number_str[1] == '0':
            return number_dict[number_str[0]] + u'百零' + number_dict[number_str[2]]
        else:
            return number_dict[number_str[0]] + u'百' + number_dict[number_str[1]] + u'十' + number_dict[number_str[2]]


def modify_law_name(law):
    """
    去除法律名称中的书名号及后缀 
    """
    law = law.replace(u'《', '')
    law = law.replace(u'》', '')
    law = law.replace(u'〈', '')
    law = law.replace(u'〉', '')
    law = law.replace(u'﹤', '')
    law = law.replace(u'﹥', '')
    law = law[:law.find('.')]
    return law


def find_plaintiff_and_defendant_names(tree):
    """
    提取原告与被告名字
    """
    names = {}
    names['plaintiff'] = []
    names['defendant'] = []
    for item in tree.iterfind('.//DSR'):
        for attr in item.attrib:
            if attr == 'value':
                for people in item.attrib[attr].split(' '):
                    # 处理原告
                    if people.find(u'原告') == 0:
                        if people.find(u'原告：') != -1:
                            people = people[people.find(u'原告：')+3:]
                            people = clean_people_name(people)
                            names['plaintiff'].append(people)
                        else:
                            people = people[people.find(u'原告')+2:]
                            people = clean_people_name(people)
                            names['plaintiff'].append(people)
                    # 处理被告
                    if people.find(u'被告') == 0:
                        if people.find(u'被告：') != -1:
                            people = people[people.find(u'被告：')+3:]
                            people = clean_people_name(people)
                            names['defendant'].append(people)
                        else:
                            people = people[people.find(u'被告')+2:]
                            people = clean_people_name(people)
                            names['defendant'].append(people)
    return names


def clean_people_name(people):
    """
    清理人名中的标点
    """
    if people.find(u'，') != -1: people = people[:people.find(u'，')]
    if people.find(u'。') != -1: people = people[:people.find(u'。')]
    if people.find(u'；') != -1: people = people[:people.find(u'；')]
    if people.find(u'（') != -1 and people.endswith(u'）'): people = people[:people.find(u'（')]
    if people.find(u'）') != -1 and people.startswith(u'（'): people = people[people.find(u'）')+1:]
    return people
