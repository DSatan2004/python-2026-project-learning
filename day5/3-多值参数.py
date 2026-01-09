
def demo2(*args,**kwargs):
    print(f'demo2{args}')
    print(f'demo2{kwargs}')

# 多值参数就是参数个数不确定，必须是下面的写法
def demo(*args, **kwargs):
    # 参数名前增加一个 * 可以接收元组
    # 参数名前增加两个 * 可以接收字典
    # print(num)
    print(args) # 元组
    print(kwargs) # 字典
    demo2(*args,**kwargs)

demo(1,2,[1,2,3],4,5,name = '小明',age = 19)