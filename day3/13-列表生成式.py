
my_list = [x for x in range(10)]
print(my_list)

# 两个for循环
a = [j for i in range(10) for j in range(i)]
print(a)

# 二维列表
a = [[col * row for col in range(5)]for row in range(5)]
print(a)
# print(a[1][2])

# 二维转一维
b = [j for x in a for j in x]
print(b)

# 只有if时
c = [x for x in range(10) if x%2==0]
print(c)

# if_else的三元表达式
a = [x if x % 2 == 0 else x**2 for x in range(10)]
print(a)