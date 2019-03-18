import os
import csv
import requests

location = "/Volumes/insignary/home/insignary/maven2/"
file_list = []
url_list = []
for root, dirs, files in os.walk('/Volumes/insignary/home/insignary/maven2/'):
    for file in files:
        if ".csv" in file:
            file_list.append(file)
            f = open(location+file, 'r')
            rdr = csv.reader(f)
            try:
                for line in rdr:
                    # find_string = "application"
                    exception = len(line)
                    if exception < 2:
                        pass
                    elif "application" in line[1]:
                        url_list.append(line[0])
            f.close()
            except:
                pass
        else:
            pass
print(url_list)
print(file_list)
f.close()