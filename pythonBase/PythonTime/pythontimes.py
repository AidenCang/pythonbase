# https://www.cnblogs.com/sunshine-blog/p/8477893.html
import datetime
import time
import os
import shutil

start_date = datetime.date(year=2019, month=6, day=1)
basedir = 'data'
if not os.path.isdir(basedir):
    os.mkdir(basedir)

print(os.getcwd())

error = 0


def get_data(url):
    global error
    if error % 5 == 0:
        raise Exception('error')
    time.sleep(2)
    print("获取数据成功!!!!!!!")


# os.chdir(basedir)
# for file in list(os.listdir()):
#     if os.path.isfile(file):
#         os.remove(file)
#     else:
#         shutil.rmtree(file)

while start_date < datetime.date.today():
    path = os.path.join(basedir, start_date.__str__())
    if not os.path.isdir(path):
        error += 1;
        os.mkdir(path)
        # 爬取数据
        try:
            get_data('http://wwwbaidu.com')
            with open(path + "/" + 'aa.txt', mode='w+') as file:
                file.write('aaaaaaa')
                file.flush()
                file.close()
        except Exception as e:
            os.rmdir(path)


    else:
        print('文件已存在！！！')
    start_date = start_date + datetime.timedelta(days=1)
    # print(start_date)


# class DeleteFiles(object):
#     def __init__(self, pathDir):
#         self.pathDir = pathDir
#
#     def delete_files(self):
#         os.chdir(self.pathDir)
#         fileList = list(os.listdir())
#         for file in fileList:
#             if os.path.isfile(file):
#                 os.remove(file)
#                 print("delete successfully")
#             else:
#                 shutil.rmtree(file)
#
#
# dir = DeleteFiles(basedir)
# dir.delete_files()
