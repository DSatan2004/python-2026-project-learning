# 作者: 王道 龙哥
# 2024年12月27日16时33分09秒
# xxx@qq.com

def homework1():
    """
    有7个整数，其中有3个数出现了两次，1个数出现了一次， 找出出现了一次的那个数
    :return:
    """
    # 异或满足交换律
    my_list = [1, 1, 2, 2, 3, 6, 6]
    result = 0
    for i in my_list:
        result ^= i
    print(result)


def homework6():
    """
    有8个整数，其中有3个数出现了两次，2个数出现了一次， 找出出现了一次的那2个数
    :return:
    """
    # 把9和10分到两堆，对每一堆各自异或
    my_list = [1, 1, 2, 2, 3, 6, 6, 8, 3, 12, 8, 10]
    # 0000 1001   9
    # 0000 1010   10
    result = 0
    for i in my_list:
        result ^= i
    # print(result)
    # 0000 0011   0000 0001
    # 如何使用result对原有列表，遍历1遍分成两堆
    split_flag = result & -result  # 获取result最低位为1的那个数
    list1 = []
    list2 = []
    result1, result2 = 0, 0
    for i in my_list:
        if split_flag & i:
            # list1.append(i)
            result1 ^= i
        else:
            # list2.append(i)
            result2 ^= i
    # print(list1, list2)
    print(result1, result2)


if __name__ == '__main__':
    homework1()
    # homework6()
