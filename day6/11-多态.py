# 多态：统一条指令，不同的对象，产生的行为是不一样的

class Dog(object):

    def __init__(self,name):
        self.name = name

    def game(self):
            print("%s 蹦蹦跳跳的玩耍..." %self.name)

class XiaoTianQuan(Dog):

    def game(self):
        print("%s 飞到天上去玩耍..." %self.name)

class Person():
    def __init__(self,name):
        self.name = name

    def game_with_dog(self,dog:Dog):

        print("%s 和 %s 快乐的玩耍..." % (self.name, dog.name))
        # 让狗玩耍
        dog.game()


if __name__ == '__main__':
    zhangsan = Person("张三")
    wangcai = Dog("旺财")
    zhangsan.game_with_dog(wangcai)
    xiaotianquan = XiaoTianQuan('哮天犬')
    zhangsan.game_with_dog(xiaotianquan)
