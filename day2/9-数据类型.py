# 作者: 王道 龙哥
# 2024年12月25日14时54分43秒
# xxx@qq.com


def use_hex():
    a = 123
    print(bin(a))  # 功能 将整数转换为二进制
    print(hex(a))  # 功能 将整数转换为十六进制
    print(oct(a))  # 功能 将整数转换为八进制

    b = -5

    print(bin(b))


def use_float():
    f = 1.234567891234567891
    print(f)


def use_bool():
    print(True+1)
    print(False+1)


def use_complex():
    c = complex(3, 4)
    print("c is %d+%dj" % (c.real, c.imag))

# use_hex()
# use_float()
# use_bool()
use_complex()