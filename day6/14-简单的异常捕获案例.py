import test_exception_module
import traceback
import sys


def use_exception1():

    try:
        # 提示用户输入一个数字
        num = int(input('请输入一个数字'))
        print(num)
    except:
        print('输入的必须是整型数字')

def use_exception2():
    """
    掌握不同的异常类型
    :return:
    """
    try:
        num = int(input('请输入一个整数:'))
        result = 8/num
        print(result)
    except ValueError:
        print('请输入正确的整数')
    except ZeroDivisionError:
        print("除0错误")

def use_exception3():
    """
    捕获未知错误
    :return:
    """
    try:
        num = int(input('请输入一个整数:'))
        result = 8 // num
        print(result)
    except ValueError:
        print('请输入正确的整数')
    except Exception as e:#代表异常对象的别名
        print(e)

def use_exception4():
    try:
        num = int(input('请输入整数'))
        result = 8/num
        print(result)
    except ValueError:
        print('请输入正确的整数')
    except ZeroDivisionError():
        print('除0错误')
    except Exception as e:
        print(e)
    else:
        print('正常执行')
    finally:
        print('执行完成，但是不保证正确')

def use_exception5():
    """
    如何捕获异常发生的文件和具体行数
    :return:
    """
    try:
        test_exception_module.test()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])
        print(e.__traceback__.tb_lineno)

def use_exception6():
    try:
        test_exception_module.test()
    except Exception as e:
        # 打印详细的错误信息
        exc_type, exc_value, exc_tb = sys.exc_info()
        # 获取异常发生的文件名、行号和错误类型
        tb = traceback.extract_tb(exc_tb)[-1]
        print(f"Error occurred in file: {tb.filename}")
        print(f"Line number: {tb.lineno}")
        print(f"Error message: {str(e)}")

if __name__ == '__main__':
    # use_exception1()
    # use_exception2()
    # use_exception3()
    # use_exception4()
    # use_exception5()
    use_exception6()