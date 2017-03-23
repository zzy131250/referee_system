# encoding=utf-8
from os import listdir
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

# 根据文书涉及的法律对文书进行分类
root_dir = u'C:\\Users\\J\\Desktop\\共享文书\\民事一审\\'
dest_dir = 'C:\\Users\\J\\OneDrive\\Workspace\\PythonWorkspace\\referee_system\\preprocess\\case_list\\'
files = listdir(root_dir)
case_txt = open(dest_dir + 'civil_law_case.txt', 'wb')

# 婚姻法、合同法、民法通则
for file in files:
    tree = ET.ElementTree(file=root_dir + file)
    for elem in tree.iterfind('.//QW'):
        for attr in elem.attrib:
            if attr == 'value':
                content = elem.attrib[attr]
                if content.find(u'民法通则') != -1:
                    case_txt.write(file + '\n')

case_txt.close()
