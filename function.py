def test():
    color = "red"
    print(color)

test()
color = 'blue'
print(color)

def test2(para, para2):
    print(para)
    print(para2)

test2(para = 2, para2 = 1)
def test3(a,b):
    return a+b
v_test3 = test3(1,2)
print(v_test3)

def id(first_name, last_name, age):
    dic = {
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }
    return dic
print(id(first_name = 'John', last_name = 'Doe', age= 20))
for i,o in id(first_name = 'John', last_name = 'Doe', age= 20).items():
    print(i + ": " + o)