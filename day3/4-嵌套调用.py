# 作者: 王道 龙哥
# 2024年12月26日11时15分13秒
# xxx@qq.com
def test1():
    print("*" * 50)
    print("test 1")
    print("*" * 50)


def test2():
    print("-" * 50)
    print("test 2")
    test1()
    print("-" * 50)


test2()
