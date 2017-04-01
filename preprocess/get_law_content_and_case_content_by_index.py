# encoding=utf-8
import webbrowser

from db_operation import Mongo

mongo_instrument = Mongo()
mongo_instrument.set_collection('instrument')
mongo_law = Mongo()
mongo_law.set_collection('law')

start = 2666
end = 2670
i = 0
url = u'file://C:/Users/J/Desktop/共享文书/民事一审/'
for instrument in mongo_instrument.find_data({}):
    if i+1 >= start and i+1 <= end:
        webbrowser.open(url + instrument['case_id'], new=2)
        print instrument['case_content']
        print mongo_law.find_data({'law_id': instrument['law_id']})[0]['law_content']
        print
    i += 1
