
def use_list_set_slice():
    test_list = [1,2,3,4,5,6]
    test_list[3:3] = ['x','y','z']
    print(test_list)

def list_compare():
    a = [1,2,3]
    b = [1,2,3]
    print(a==b)
    # print(id(a)==id(b))
    print(a is b) # 判断地址是否一致

def use_method():
    a = (1,2,3)
    b = ('a','b','c')

    # print(list(zip(a,b)))
    # 如何使用enumerate
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    list2 = list(enumerate(seasons))
    print(list2)
    my_dict = dict(list2)
    print(my_dict.items())
    print({v:k for v,k in my_dict.items()})

if __name__ == '__main__':
    # list_compare()
    use_method()