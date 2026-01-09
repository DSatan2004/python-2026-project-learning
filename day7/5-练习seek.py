import os


def seek_start():
    """
    相对于开头（文件起始位置）进行偏移
    :return:
    """
    file = open('file1',mode='r+',encoding='utf8')
    file.seek(3,os.SEEK_SET)# 相当于移动光标到5个字节以后
    text = file.read(5)
    print(text)
    file.close()

def seek_end():
    """
    相对于文件尾部进行偏移
    :return:
    """
    file = open('file1',mode='r+',encoding='utf8')
    file.seek(0 ,os.SEEK_END)# 相当于移动光标到5个字节以后
    text = file.read(5)
    print(text)
    file.close()

def seek_cur():
    """
    相对于文件尾部进行偏移
    :return:
    """
    file = open('file1',mode='r+',encoding='utf8')
    file.seek(0 ,os.SEEK_CUR)# 相当于移动光标到5个字节以后
    text = file.read(5)
    print(text)
    file.close()

def seek_b_cur():
    """
    在b模式下，读取到的是字节流,读取图片音频视频
    :return:
    """
    file = open('file1',mode='rb+')
    file.seek(5,os.SEEK_CUR)
    file.seek(-2,os.SEEK_CUR)
    file.seek(-3,os.SEEK_END)
    b = file.read()
    print(b)
    file.close()

def copy_file():
    file1 = open('baidu.png',mode='rb+')
    file2 = open('baidu_copy.png',mode='wb')
    b = file1.read()
    file2.write(b)
    file1.close()
    file2.close()

def modify_movie():
    with open('baidu.png', mode='rb+') as file1:
        file1.seek(10, os.SEEK_SET)

        b = file1.read(1)
        print("原字节:", b)

        # bytes -> int
        value = b[0]

        # 按位取反（8 位）
        inverted = (~value) & 0xFF

        # 指针回退 1 个字节
        file1.seek(-1, os.SEEK_CUR)

        # 写回取反后的字节
        file1.write(bytes([inverted]))

        print("取反后:", bytes([inverted]))

if __name__ == '__main__':
    # seek_start()
    # seek_end()
    # seek_cur()
    # seek_b_cur()
    # copy_file()
    modify_movie()