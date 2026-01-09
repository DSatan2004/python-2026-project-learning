# 1. 定义重复次数计数器

def use_while1():
    i = 1

    # 2. 使用 while 判断条件
    while i <= 5:
        # 要重复执行的代码
        print("Hello Python")

        # 处理计数器 i
        i = i + 1

    print(f'循环结束，i的值{i}')


def use_continue():
    # 0. 定义最终结果的变量
    result = 0

    # 1. 定义一个整数的变量记录循环的次数
    i = 0

    # 2. 开始循环
    while i <= 100:

        if i % 2 == 1:
            i += 1
            continue
        result += i

        # 处理计数器
        i += 1

    print(f"0~100之间的数字求和结果 = {result} i={i}")


def use_break():
    # 0. 定义最终结果的变量
    result = 0

    # 1. 定义一个整数的变量记录循环的次数
    i = 0

    # 2. 开始循环
    while i <= 100:

        if result > 2000:
            break
        result += i

        # 处理计数器
        i += 1

    print(f"0~100之间的数字求和结果 = {result} i={i}")


def use_print():
    print("Hello", end='')  # 不要换行
    print('world', end=' ')  # 带有一个空格
    print('howareyou', end='')


def use_for():
    my_list = ['ab', 'bd', 'cf', 'haha']  # 列表，类似于C语言的数组
    for i in my_list:
        print(i, end=' ')
    print()
    print('-' * 50)
    print(i)  # for的游标在for循环外可以使用


def use_for_else():
    for i in range(10):  # range是左闭右开
        if i == 15:
            print(f'不会走下面else的内容，找到了{i}')
            break
    else:
        print('没找到')
    for i in range(1, 11):
        if i == 7:
            print(f"已经找到{i}")
            break


# use_while1()
# use_continue()
# use_break()
# use_print()
# use_for()
use_for_else()
