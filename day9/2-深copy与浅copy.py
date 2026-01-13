import copy


def use_list_copy():
    """
    使用列表自身的copy
    """
    a=[1,2,3]
    b = a.copy()
    b[0]=10
    print(a)
    print(b)

def use_copy():
    """
    使用copy包中的copy
    """
    c = [1, 2, 3]
    d = copy.copy(c)
    d[0] = 10
    print(id(c))
    print(id(d))
    print(c)
    print(d)

def use_copy2():
    a = [1, 2]
    b = [3, 4]
    c = [a, b]
    d = copy.deepcopy(c)
    print(id(c))
    print(id(d))
    a[0] = 10
    print(c)
    print(d)
    print('-'*50)
    print(id(c[0]),id(c[1]))
    print(id(d[0]),id(d[1]))

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def use_copy_own_obj():
    s1 = Student('小明',18 )

if __name__ == '__main__':
    # use_list_copy()
    # use_copy()
    use_copy2()

