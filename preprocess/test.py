global a
a = 0
def b():
    global a
    a = 1
b()
print a