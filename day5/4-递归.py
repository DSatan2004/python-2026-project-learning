#
# import sys
# sys.setrecursionlimit(10000000)

# 递归实现的难度比循环低
def sum_numbers(num):
    print(num)

    # 递归的出口（结束条件）很重要，否则会出现死循环
    if num == 1:
        return

    sum_numbers(num - 1)

def f(n):
    if n == 1:
        return 1
    return n + f(n-1)

def step(n):
    if n == 1 or n == 2:
        return n
    return step(n-1) + step(n-2)

if __name__ == '__main__':
    # sum_numbers(3)
    print(f(10))
    # for i in range(1,10):
    #     print(step(i))
