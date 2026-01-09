import os


def read_conf():
    """
    读取配置
    :return:
    """
    file = open('file6','r+',encoding='utf8')
    text_info = file.read()
    print(text_info)
    my_dict = eval(text_info)
    print(type(dict))
    file.close()

if __name__ == '__main__':
    os.system('ls')