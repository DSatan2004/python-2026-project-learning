
def test(num):
    print(f'num={num},num的地址{id(num)}')
    num=5
    print(f'修改num后num={num},num的地址{id(num)}')


a = 10
print(f'调用函数前a的地址{id(a)}')
test(a)
print(a)


def change(new_list):
    print(f'赋值前，new_list的地址{id(new_list)}')
    new_list[0] = 10
    print(f'赋值后，new_list的地址{id(new_list)}')


my_list = [1, 2, 3]  # 可变数据类型
print(f'调用change之前{my_list}, 地址{id(my_list)}')
change(my_list)
print(f'调用change之后{my_list}, 地址{id(my_list)}')
