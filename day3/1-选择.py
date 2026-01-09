import random


def use_if():
    # 1.定义年龄变量
    age = 20

    # 2.使用if语句判断年龄是否大于18
    if age > 18:
        print("你已经成年了！")
    else:
        print("你还未成年！")


def use_elseif():
    holiday_name = "平安夜"

    if holiday_name == "情人节":
        print("买玫瑰")
        print("看电影")
    elif holiday_name == "平安夜":
        print("买苹果")
        print("吃大餐")
    elif holiday_name == "生日":
        print("买蛋糕")
    else:
        print("每天都是节日啊")


# 定义布尔型变量 has_ticket 表示是否有车票
has_ticket = True
# 定义整数型变量 knife_length 表示刀的长度，单位：厘米
knife_length = 20


def use_two_if():
    # 定义布尔型变量 has_ticket 表示是否有车票
    has_ticket = True
    # 定义整数型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = 20
    # 首先检查是否有车票，如果有，才允许进行 安检
    if has_ticket:
        print("有车票，可以开始安检...")
        # 安检时，需要检查刀的长度，判断是否超过 20 厘米
        # 如果超过 20 厘米，提示刀的长度，不允许上车
        if knife_length >= 21:
            print("不允许携带 %d 厘米长的刀上车" % knife_length)
        # 如果不超过 20 厘米，安检通过
        else:
            print("安检通过，祝您旅途愉快……")
    # 如果没有车票，不允许进门
    else:
        print("大哥，您要先买票啊")


def use_random():
    # 从控制台输入要出的拳 —— 石头（1）／剪刀（2）／布（3）
    player = int(input("请出拳 石头（1）／剪刀（2）／布（3）："))
    # 电脑 随机 出拳 - 假定电脑永远出石头
    computer = random.randint(1, 3)
    # 比较胜负
    # 如果条件判断的内容太长，可以在最外侧的条件增加一对大括号
    # 再在每一个条件之间，使用回车，PyCharm 可以自动增加 8 个空格
    if ((player == 1 and computer == 2) or
            (player == 2 and computer == 3) or
            (player == 3 and computer == 1)):
        print("噢耶！！！电脑弱爆了！！！")
    elif player == computer:
        print("心有灵犀，再来一盘！")
    else:
        print("不行，我要和你决战到天亮！")

# 3.调用函数
# use_if()
# use_elseif()
# use_two_if()


use_random()
