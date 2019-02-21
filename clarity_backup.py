import os, time
import datetime
import shutil
import errno

now = datetime.datetime.now()
#cwd = os.getcwd()
cwd = '/usr/local/insignary/clarity/web/data'
dst = '/tmp/original_files/'

now_m = str(now.month)
#now_d = str(now.day-1)
now_d = str(now.day)
now_md = now_m+now_d

# Create target Directory if don't exist
if not os.path.exists(dst):
    os.mkdir(dst)
    print("Directory " , dst ,  " Created ")
else:
    print("Directory " , dst ,  " already exists")

for path, dirs, files in os.walk(cwd):
        for f in files:
                fullpath = os.path.join(path, f)
                if 'original_files' in fullpath:
                        ctime = os.path.getctime(fullpath)
                        ctime_oneday_ago = ctime
                        strctime_oneday_ago = datetime.datetime.fromtimestamp(ctime_oneday_ago).strftime('%m%d')
                        print(strctime_oneday_ago)
                        if strctime_oneday_ago == now_md:
                                shutil.copy2(fullpath, dst)
                                print("Copy File : ", fullpath)