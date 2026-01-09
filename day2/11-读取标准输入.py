# 作者: 王道 龙哥
# 2024年12月25日15时46分39秒
# xxx@qq.com

def change_alpha():
    a = input('请输入内容')
    print(a)
    print(type(a))  # 查看a的类型

    #大写转小写
    print(chr(ord(a) + 32))


def change_type():
    a = input('请输入数字')
    print(float(a)+5)


# change_alpha()
change_type()