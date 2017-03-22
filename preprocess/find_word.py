# encoding=utf-8
from os import listdir
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

root_dir = '/home/zzy131250/civil/'
dest_dir = '/home/zzy131250/referee_system/preprocess/case_list/'
files = listdir(root_dir)
case_txt = open(dest_dir + 'marriage_law_case.txt', 'wb')

for file in files:
    tree = ET.ElementTree(file=root_dir + file)
    for elem in tree.iterfind('.//QW'):
        for attr in elem.attrib:
            if attr == 'value':
                content = elem.attrib[attr]
                if content.find(u'') != -1:
                    case_txt.write(file)

case_txt.close()
