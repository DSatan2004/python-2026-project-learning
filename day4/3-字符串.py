
def check_type():
    # 判断字符串类型
    s1 = 'abc123*'
    print(s1.isalnum())
    s2 = '123'
    print(s2.isdecimal())

def str_find():
    # 字符串查找与替换
    s1 = 'abcdefgcdef'
    print(s1.find('cd', 4))# 返回找到字符串的起始下标
    s2 = s1.replace('cd', 'CD',1)
    print(s2)

def str_split_join():
    # 分隔与连接
    s1 = 'abc bcd 我很帅'
    print(s1.split())
    s1 = 'abc,bcd,我很帅'
    print(s1.split(','))
    s2= 'abc\nbcd\nefg'
    print(s2.splitlines())
    str_list=['a','b','c','d']
    print(','.join(str_list))

def str_slice():
    # 字符串的切片
    num_str = '0123456789'
    # 1.截取从2~ 5位置的字符串
    print(num_str[2:6]) # 左闭右开

    # 2.截取从2~ 末尾的字符串
    print(num_str[2:])

    # 3.截取从开始~ 5位置的字符串
    print(num_str[:6])

    # 4.截取完整的字符串
    print(num_str[:])

    # 5.从开始位置，每隔一个字符截取字符串
    print(num_str[::2])

    # 6.从索引1开始，每隔一个取一个
    print(num_str[1::2])

    # 7.截取从2~末尾 - 1的字符串
    print(num_str[2:-1])

    # 8.截取字符串末尾两个字符
    print(num_str[-2:])

    # 9.字符串的逆序（面试题）
    print(num_str[::-1])

def list_slice():
    # 列表的切片
    my_list = list('0123456789')
    print(my_list)
    print(my_list[2:6])

def index_count():
    hello_str = "hello hello"
    # 1. 统计字符串长度
    print(len(hello_str))
    # 2. 统计某一个小（子）字符串出现的次数
    print(hello_str.count("llo"))
    print(hello_str.count("abc"))
    # 3. 某一个子字符串出现的位置
    print(hello_str.index("llo"))
    # 注意：如果使用 index 方法传递的子字符串不存在，程序会报错！
    # print(hello_str.index("abc"))


if __name__ == '__main__':
    # check_type()
    # str_find()
    # str_split_join()
    # str_slice()
    # list_slice()
    index_count()