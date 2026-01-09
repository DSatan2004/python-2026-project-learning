name_list = ['zhangsan', 'lisi', 'wangwu']

# 1 取值
print(name_list[0])
# 查找元素
print(name_list.index('wangwu'))

# 2 修改
name_list[1] = '李四'
print(name_list)

# 3 添加
name_list.append('王五')  # 长度变长地址有没有改变   答：没有
print(name_list)

name_list.insert(1, '王小美')
print(name_list)
# extend可以把其他列表中的完整内容，追加到当前列表的末尾
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)
print(name_list)

# 4 删除
# remove方法可以从列表中删除指定的数据
# name_list.remove("wangwu")
# # pop方法默认可以把列表中最后一个元素删除
# name_list.pop()
# # pop方法可以指定要删除元素的索引
# name_list.pop(3)
# # clear方法可以清空列表
name_list.clear()
print(name_list)
name_list.append(3)
print(name_list)
