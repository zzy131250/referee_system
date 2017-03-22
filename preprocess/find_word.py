# encoding=utf-8
from os import listdir
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

root_dir = u'C:\\Users\\J\\Desktop\\共享文书\\民事一审'
files = listdir(root_dir)

for file in files:
    tree = ET.ElementTree(file=root_dir + '\\' + file)
    for elem in tree.iterfind('.//QW'):
        for attr in elem.attrib:
            if attr == 'value':
                content = elem.attrib[attr]
                if content.find(u'民法通则') != -1:
                    print file