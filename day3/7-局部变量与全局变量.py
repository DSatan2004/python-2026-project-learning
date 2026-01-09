
#1.执行到需要全局变量时，全局变量必须被定义了
def demo1():
    global num
    print(num)
    num = 2
    print(f'demo1函数里面， 修改后{num}')


num = 10
print(f'函数调用前{id(num)}')
demo1()
print(f'函数外面{num}, 函数调用后{id(num)}')
