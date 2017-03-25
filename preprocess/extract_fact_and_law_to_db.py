# encoding=utf-8
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import re

from string_process import modify_law_id
from db_operation import Mongo

file_list = 'case_list/not_withdrawal_case.txt'
instrument_dir = u'C:\\Users\\J\\Desktop\\共享文书\\民事一审\\'
mongo = Mongo()
mongo.set_collection('instrument')
with open(file_list, 'r') as files:
    for file in files:
        tree = ET.ElementTree(file=instrument_dir + file[:-1])
        # 提取事实
        for item in tree.iterfind('.//CMSSD'):
            for attr in item.attrib:
                if attr == 'value':
                    fact = item.attrib[attr]
                    instrument_array = []
                    # 提取法条编号
                    for elem in tree.iterfind('.//CUS_FLFT_RY'):
                        for at in elem.attrib:
                            if at == 'value':
                                law_id = elem.attrib[at]
                                law_id = modify_law_id(law_id)
                                # 去除含有数字的法条
                                if law_id != '' and re.findall('[1-9]', law_id) == []:
                                    instrument = {}
                                    instrument['case'] = fact
                                    instrument['law_id'] = law_id
                                    instrument['applicable'] = 'yes'
                                    instrument_array.append(instrument)
                    if instrument_array != []:
                        mongo.insert_data(instrument_array)