# encoding=utf-8


def modify_law_id(law):
    '''
    去除法条书名号，去除款号和项号
    '''
    law = law.replace(u'《', '')
    law = law.replace(u'》', '')
    law = law.replace(u'〈', '')
    law = law.replace(u'〉', '')
    law = law.replace(u'﹤', '')
    law = law.replace(u'﹥', '')
    index = law.rfind(u'条')
    law = law[:index+1]
    return law