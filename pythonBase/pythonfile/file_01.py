# file = open('text.txt',mode='w+')

import os
import datetime
from time import time

# os.path.isabs()
# os.path.isdir()
# os.path.isfile()
# os.path.isfile()
# os.path.islink()
# os.path.ismount()


basedir = "data"
print(datetime.date.today().strftime('%Y-%m-%d'))
# with open('text.txt', mode='w+') as file:
#     for i in range(20):
#         file.write(str(i))
#         file.write('\r\n')

print(os.path.isdir(basedir))
print(os.path.exists(basedir))
if not os.path.exists(basedir):
    os.mkdir(basedir)
today = datetime.date.today()
print(today)
for i in range(50):
    today = today + datetime.timedelta(days=1)
    print(today)
