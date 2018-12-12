import requests,time,re
from bs4 import BeautifulSoup


VioceID = 6207


url = 'http://m.ysxs8.com/yousheng/%d_1.html'%VioceID
html = requests.get(url).text
PlayUrl = re.findall('src=\"(.*playdata.*?)\"><',html)[0]
PlayUrl = 'http://m.ysxs8.com'+PlayUrl
html = requests.get(PlayUrl).text
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
