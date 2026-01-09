
class Person:
    """人类"""
    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def run(self):
        self.weight -= 0.5
        print(f'{self.name}跑步了，体重减去0.5公斤,现有体重{self.weight}')

    def eat(self):
        self.weight += 1
        print(f'{self.name}吃了东西，体重增加1公斤,现有体重{self.weight}')

    def __str__(self):
        return f'我的名字叫{self.name} 体重{self.weight}公斤'

if __name__ == '__main__':
    elephant = Person('大象', 80)
    elephant.run()
    elephant.eat()
    print(elephant)

    tiger = Person('老虎', 45)
    tiger.eat()
    tiger.run()