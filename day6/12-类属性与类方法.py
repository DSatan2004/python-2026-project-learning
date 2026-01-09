
class Tool:
    count = 0 # 类属性
    def __init__(self,name):
        self.name = name
        Tool.count += 1

    def func(self):
        print(f'{self.name}可以做很多事情')

    def __del__(self):
        Tool.count -= 1

    @classmethod
    def show_tool_count(cls):
        """
        当你不使用对象属性，只使用类属性,类方法
        :return:
        """
        print(cls.count)

    @staticmethod
    def help():
        """
        不使用对象属性，也不使用类属性
        :return:
        """
        print("这是一个工具类，作用是实例化各种工具对象")

if __name__ == '__main__':
    tool1 = Tool('斧子')
    print(Tool.count)
    tool2 = Tool('锤子')
    print(Tool.count)
    del tool1
    print(Tool.count)
    print('-'*50)
    Tool.show_tool_count()
    Tool.help()
