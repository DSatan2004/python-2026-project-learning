def demo1():
    num = int(input("输入整数:"))
    print('I am demo1')
    return num

def demo2():
    num2 = demo1()
    print('I am demo2')
    return num2

try:
    print(demo2())
except Exception as result:
    print('未知错误 %s' % result)