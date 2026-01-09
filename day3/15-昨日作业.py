

# 实现从1到100的奇数求和
def homework4():
    print(sum([x for x in range(100) if x % 2 == 1]))


# 打印九九乘法表
def homework5():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f'{j}*{i}={j*i:<2}', end=' ')
        print()


# 统计一个整数对应的二进制中1的个数
def homework6():
    s = int(input('请输入一个整数'))
    if s >= 0:
        # 正数补码 = 正数原码
        num = bin(s).count('1')
    else:
        # 对于负数

        num = 64 - bin(-s -1).count('1')
    print(num)


if __name__ == '__main__':
    # homework4()
    homework5()
    homework6()