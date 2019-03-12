import xlsxwriter
import requests
import csv
import re
import smtplib, ssl
from datetime import date, timedelta
from datetime import datetime

log_file = open('/Users/secuof/little-forest/python/study_python/excel_sample_file/logfile.csv', 'a')

today = date.today()
yesterday = date.today() - timedelta(5)
 
today = today.strftime('%Y%m%d')
yesterday = yesterday.strftime('%Y%m%d')

workbook = xlsxwriter.Workbook('/Users/secuof/little-forest/python/study_python/excel_sample_file/'+yesterday+'.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Check date', bold)
worksheet.write('A2', yesterday)
worksheet.write('B1', 'Visit count', bold)
worksheet.write('C1', 'Scan count', bold)
worksheet.write('D1', 'Success', bold)
worksheet.write('E1', 'Fail', bold)
worksheet.write('F1', 'Email count', bold)
worksheet.write('G1', 'Email', bold)

url = 'https://testyourbinary.insignary.com/1/users/trial/csv?start=' + yesterday + '&end=' + yesterday
response = requests.get(url)
req_response = response.text

if response.status_code != 200:
    print('Failed to get data:', response.status_code)
else:
    wrapper = csv.reader(response.text.strip().split('\n'))
    lines = 0
    resultlist = []
    for line in wrapper:
        lines += 1
        search = re.findall(r'[\w\.-]+@[\w\.-]+', str(line))
        if len(search) > 0:
            search_ip = re.findall(r'\d+[.]\d+[.]\d+[.]\d+', str(line))
            resultlist.extend(search_ip)
        if lines == 2:
            data = ""
            row = 1
            col = 1
            for i, flavor in enumerate(line, 1):
                if i == 1 or i == 2 or i == 5 or i == 6:
                    data += flavor + ','
                    worksheet.write(row, col, flavor)
                    col += 1
                elif i == 8:
                    data += flavor
                    worksheet.write(row, col, flavor)
            row += 1
        else:
            pass

result_id_ip = []
for each_ip in set(resultlist):
    wrapper = csv.reader(response.text.strip().split('\n'))
    for line in wrapper:
        search_ip = re.findall(each_ip, str(line))
        search_email = re.findall(r'[\w\.-]+@[\w\.-]+', str(line))
        if len(search_email) > 0:
            pass
        elif len(search_ip) > 0:
            id_ip = line[1]+"/"+line[2]
            result_id_ip.append(id_ip)

email = re.findall(r'[\w\.-]+@[\w\.-]+', req_response)
emails = ','.join(map(str, email))
worksheet.write('G2', emails)
write_log = yesterday+","+data+","+emails+","+str(result_id_ip)+","+url+"\n"
# print(str(set(resultlist)))
# print(url)
# print(result_id_ip)
print(write_log)
log_file.write(write_log)

workbook.close()
log_file.close()