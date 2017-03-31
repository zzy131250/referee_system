# encoding=utf-8
import webbrowser

# 自动打开选定的文书
url = u'file://C:/Users/J/Desktop/共享文书/民事一审/'
start = 1
end = 20
txt = open('C:\\Users\\J\\OneDrive\\Workspace\\PythonWorkspace\\referee_system\\preprocess\\case_list\\traffic_safety_case.txt', 'r')
for i, line in enumerate(txt):
    if i >= start-1 and i < end:
        webbrowser.open(url + line[:-1], new=2)