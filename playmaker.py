# -*- coding: utf-8 -*-
import urllib, json, codecs

url = 'http://91.92.66.82/trash/ttv-list/allfon.json'
aceurl = '192.168.0.111'

def getjson():
    response = urllib.urlopen(url)
    data = response.read()
    with open('ttv.json', 'w') as f:
        f.write(data)

def getstream(channel):
    with open('ttv.json') as f:
        data = json.load(f)
        for i in data[u'channels']:
            if i[u'name'] == channel:
                hash = i[u'url']
                return str(u'#EXTINF:-1,{0}\nhttp://{1}:6878/ace/getstream?id={2}&.mp4\n'.format(channel, aceurl, hash).encode('utf-8'))

def makepl():
    getjson()
    with open('static/playlist.m3u', 'w') as pl:
        pl.write(u'#EXTM3U\n\n')
        with codecs.open('static/channels.txt', encoding='utf-8') as f:
            lines = f.read().splitlines()
            for l in lines:
                pl.write(getstream(l))

if __name__ == "__main__":
    makepl()