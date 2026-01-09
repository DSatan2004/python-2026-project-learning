
def print_info(name, title="", gender = True):

    gender_text = '男生'

    if not gender:
        gender_text = '女生'

    print('%s%s是%s' %(title, name, gender_text))

# 在指定缺省参数的默认值时， 应该使用最常见的值作为默认值
print_info('小明')
print_info('老王', title="班长")
print_info('小美', gender = False)
print('-'*50)
print_info("小美", gender=False, title='学习委员')
