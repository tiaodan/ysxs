import requests,time
from bs4 import BeautifulSoup


VioceID = 6207

url = 'http://m.ysxs8.com/playdata/63/%d.js'%VioceID
html = requests.get(url).text
html = html.replace(']','')
html = html.replace('[','')
html = html.replace("'",'')
VoiceList = html.split(',')

for Voice in VoiceList:
    try:
        Voice = Voice.split('$')
        Name = Voice[0]
        Name = Name.encode('utf-8').decode('unicode_escape')
        DownloadUrl = Voice[1]
        with open('download.bat','a') as f:
            f.writelines(['aria2c -o '+Name +'.m4a '+ DownloadUrl +'\n'])
    except:
        pass

