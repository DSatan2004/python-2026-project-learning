import os

def use_rename():
    # os.rename('file3','file4')
    os.remove('dir1/file1')

def use_dir_func():
    file_list = os.listdir('.')
    print(file_list)
    # os.mkdir('dir2')
    # os.rmdir('dir1')
    print(os.getcwd())
    os.chdir('dir2')
    file = open('file1','w',encoding='utf-8')
    file.close()

def scan_dir(current_path,width):
    """
    深度优先遍历
    :param current_path:
    :return:
    """
    file_list = os.listdir(current_path)
    for file in file_list:
        print(' '*width,file)# 打印文件名
        new_path = current_path + '/' + file #把当前路径和文件名拼接起来
        if os.path.isdir(file):
            scan_dir(new_path,width+4)

def use_stat(file_path):
    file_info = os.stat(file_path)
    print('size{},uid{},mode{:x},mtime{}'.format(file_info.st_size,file_info.st_uid,file_info.st_mode,file_info.st_mtime))

    from time import strftime
    from time import gmtime
    gm_time = gmtime(file_info.st_mtime)
    # 把秒数转为字符串时间
    print(strftime('%Y-%m-%d %H:%M:%S', gmtime(file_info.st_mtime)))

if __name__ == '__main__':
    # use_rename()
    # use_dir_func()
    # scan_dir('.',0)
    use_stat('file1')