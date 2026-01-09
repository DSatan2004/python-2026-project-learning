
def measure():
    # 返回当前的温度

    print("开始测量...")
    temp = 39
    wetness = 10
    print('测量结束...')

    return temp,wetness

ret1,ret2 = measure()
print(ret1,ret2)
print(type(ret1),type(ret2))

# 交换两个值
a = 1
b = 2
a,b = b,a
print(a,b)
