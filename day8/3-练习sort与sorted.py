
my_list = "This is a test string from Andrew".split()
print(my_list)

def change_lower(str_name: str):
    return str_name.lower()

# 可以传递一个比较故规则的函数
# print(sorted(my_list,key=change_lower))

my_list.sort(key=change_lower)
print(my_list)

student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
]

def func(x):
    return x[2]

print(sorted(student_tuples ,key = lambda x:x[2]))

class Student:
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        """
        相对于__str__来说更方便，可以返回非字符串类型
        """
        return repr((self.name,self.grade,self.age))

student = Student('john','A',15)
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
print('-'*50)
print(sorted(student_objects,key=lambda student:student.grade))

from operator import itemgetter,attrgetter
print('使用operator系列')
print(sorted(student_tuples, key=itemgetter(0)))
print(sorted(student_objects,key=attrgetter('age')))
print('使用operator系列，多列排序')
print(sorted(student_tuples, key=itemgetter(1,2)))
print(sorted(student_tuples, key=lambda x: (x[1],-x[2])))
print(sorted(student_objects, key=attrgetter('grade','age'),reverse=True))

print('查看排序稳定性')
data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
print(sorted(data,key=itemgetter(0)))

mydict = { 'Li' : ['M',7],
           'Zhang': ['E',2],
           'Wang' : ['P',3],
           'Du' : ['C',2],
           'Ma' : ['C',9],
           'Zhe' : ['H',7] }
print(sorted(mydict.items(),key=lambda x:x[1][1]))