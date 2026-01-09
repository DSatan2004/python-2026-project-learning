
def use_set():

    set1 = set()# 空集合为字典 要用set()
    print(type(set1))

    set2 = {1,2,3,4,5} # 不支持随机访问

    # 为集合添加元素
    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")
    print(fruits)
    print('-'*50)

    # 拷贝一个集合
    fruits = {"apple", "banana", "cherry"}
    x = fruits.copy()
    print(id(x))
    print(id(fruits))
    print('-'*50)

    # 返回多个集合的差集
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(z)
    print('-'*50)

    #移除集合中的元素，该元素在指定的集合也存在。
    # difference_update()
    # difference_update() 方法与 difference() 方法的区别在于
    # difference() 方法返回一个移除相同元素的新集合，而 difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.difference_update(y)
    print(x)
    print('-'*50)

    # 删除集合中指定的元素
    fruits = {"apple", "banana", "cherry"}
    fruits.discard("banana")
    print(fruits)
    print('-'*50)

    # 返回集合的交集
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)
    print(result)
    print('-'*50)

    # 返回两个集合中不重复的元素集合。
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    print('-'*50)

    # 返回两个集合的并集
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)

    print('apple' in z)

    print(x-y)

def use_generator():
    # 使用生成式
    my_tuple=tuple(x for x in range(10))
    print(my_tuple)
    my_set = {x for x in 'abracadabra' if x not in 'abc'}
    print(my_set)
    print(len(my_set))

if __name__ == '__main__':
    use_generator()