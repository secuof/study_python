import requests
from urllib.parse import urlparse

print('Beginning file download with requests')

file_name = "jamax-rest-1.3.4-RELEASE.jar"
url = 'http://central.maven.org/maven2/ba/jamax/util/jamax-rest/1.3.4-RELEASE/'+file_name
r = requests.get(url, stream=True)


print(getFilenameFromURL(url))
# headers = {'user-agent': 'test-app/0.0.1'}  
# r = requests.get(url, headers=headers)  

with open('/Users/secuof/Downloads/'+file_name, 'wb') as file:  
	file.write(r.content)

print(url,",", r.status_code,",", r.headers['content-type'])
file.close()