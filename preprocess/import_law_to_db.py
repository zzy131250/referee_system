# encoding=utf-8
from os import listdir

from db_operation import Mongo
from string_process import modify_law_name

law_dir = 'C:\\Users\\J\\Desktop\\raw_law\\'
law_list = listdir(law_dir)

mongo = Mongo()
mongo.set_collection('law')

law_array = []
for law_name in law_list:
    file = open(law_dir + law_name, 'r')
    law_name = modify_law_name(law_name.decode('gbk'))
    lines = file.readlines()
    for i in range(0, len(lines)):
        # 寻找法条编号
        line = lines[i].decode('utf-8')
        di_index = line.find(u'第')
        tiao_index = line.find(u'条 ')
        if di_index == 0 and tiao_index != -1 and di_index < tiao_index:
            # 判断下面几行的是否为同一条法条
            j = 1
            while i+j < len(lines) and lines[i+j].decode('utf-8') != '' and not lines[i+j].decode('utf-8').startswith(u'第'):
                line = line[:-1] + lines[i+j].decode('utf-8')
                j += 1
            if line.endswith('\n'): line = line[:-1]
            items = line.split(u'条 ')
            law_id = law_name + items[0] + u'条'
            law_content = items[1]
            law = {}
            law['law_id'] = law_id
            law['law_content'] = law_content
            law_array.append(law)
    file.close()

mongo.insert_many(law_array)