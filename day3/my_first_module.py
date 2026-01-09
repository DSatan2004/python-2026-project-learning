
def print_line(char, times):
    print(char * times)
    # print(num)  不合理的写法


def main():
    a = '*'
    times = 50
    num = 100
    print_line(a, times)


name = 'abc'


if __name__ == '__main__':  # python一切皆模块
    main()
