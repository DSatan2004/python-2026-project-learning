# tab往后
# shift+tab往前

str1 = '0123456789'

print(str1[9:5:-1]) #用-1切片，前面比后面大

class Cat(object):
    """这是一个猫类"""

    def __init__(self,new_name):
        print("这是一个初始化方法")
        # self.属性名 = 属性的初始值
        # self.name = "Tom"
        self.name = new_name
    def eat(self):
        print("小猫爱吃鱼")
    def drink(self):
        print("小猫在喝水")

    def __del__(self): # 析构函数，在对象被从内存销毁前会自动调用
        print(f"{self.name}对象被销毁")

    def __str__(self): # 打印对象时调用，返回字符串
        return f"对象{self.name}"

def main():
    tom = Cat('Tom')
    tom.drink()
    tom.eat()

    lazy_cat = Cat('懒猫')
    print(tom is  lazy_cat)
    # tom.name = "Tom" # 不规范的编程，不要在类外面给类添加属性
    print(tom.name)
    print('-'*50)
    # del tom # 销毁tom对象
    print(tom)

if __name__ == '__main__':
    main()
    print('程序结束')