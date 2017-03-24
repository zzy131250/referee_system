# encoding=utf-8
from os import listdir
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

root_dir = u'C:\\Users\\J\\Desktop\\共享文书\\民事一审\\'
dest_file = 'C:\\Users\\J\\OneDrive\\Workspace\\PythonWorkspace\\referee_system\\data.json'
files = listdir(root_dir)
i = 0
for file in files:
    tree = ET.ElementTree(file=root_dir + file)
    # 提取事实
    for item in tree.iterfind('.//CMSSD'):
        print item
    # 提取法条编号
    # for elem in tree.iterfind('.//CUS_FLFT_RY'):
    #     for attr in elem.attrib:
    #         if attr == 'value':
    #             law_id = elem.attrib[attr]