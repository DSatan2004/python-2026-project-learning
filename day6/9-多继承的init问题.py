
class Son1:
    def __init__(self,age,*args):
        self.age = age
        super().__init__(*args)
        
class Son2:
    def __init__(self,score):
        self.score = score

class Grandson(Son1,Son2):
     
     def __init__(self,name,*args):
         self.name = name
         super().__init__(*args)

if __name__ == '__main__':
    xiaoming = Grandson('小明',18,98.5)
    print(xiaoming.name)
    print(xiaoming.age)
    print(xiaoming.score)