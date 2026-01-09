
def open_r():
    """
    读取文件
    :return:
    """
    file = open('file2.txt',mode='r',encoding='utf-8')
    text = file.read() # 读出来的都是字符串
    print(text)
    file.write('world')
    file.close()

def open_wr():
    """
    读取文件,写文件
    :return:
    """
    file = open('file2.txt',mode='r+',encoding='utf-8')
    text = file.read() # 读出来的都是字符串
    print(text)
    file.close()


def open_w():
    """
    练习w模式
    :return:
    """
    file = open('file3',mode='w',encoding='utf-8')# 文件不存在就会创建，文件存在就会清空
    file.write('hello坚持学习')
    file.close()

def open_a():
    """
    练习a模式，每次写的时候写到文件末尾
    :return:
    """
    file = open('file1',mode='a',encoding='utf-8')
    file.write('how')
    file.close()

def use_readline():
    # 打开文件
    file = open("file2.txt",encoding='utf-8')
    while True:
        # 读取一行内容
        text = file.readline()

        # 判断是否读到内容
        if not text:
            break
        # 每读取一行的末尾已经有了一个 `\n`
        print(text, end="")
    # 关闭文件
    file.close()


if __name__ == '__main__':
    # open_r()
    # open_wr()
    # open_w()
    # open_a()
    use_readline()