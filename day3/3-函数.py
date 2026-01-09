def say_hello():
    print("hello 1")
    print("hello 2")
    print("hello 3")


def sum_2_num(num1,num2):
    """
    num1和num2是形参，类似于局部变量
    :param num1:
    :param num2:
    :return:
    """
    result = num1+num2
    print(f'求和结果{result}')
    return result

# print("执行函数前")
# say_hello()
# print("执行函数后")


ret = sum_2_num('abc', 'efg')
print(ret)

