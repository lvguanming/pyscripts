# ecoding=utf-8
import sys
import time
import random
import urllib
import urllib2
import datetime

from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os

url = "http://api.xxxxx.com/v2/day?date=ddddddd&version=4"
root = "/root/.ttt/articles/"

headers = ['Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/MOB30M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/50.0.2661.86 Mobile Safari/537.36'
           ,'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            ,'Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'
            ,'Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ,'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
            ]

access_key = '1lKyl7NnxxxxxxxxxxxxxxxxxogbXFbmr6W2zXYy'
secret_key = 'aReElmu0g0ZJgBi1-1Z42AbKxxxxxxxxxxxxxxx'
q = Auth(access_key, secret_key)
bucket_name = 'lvgm'


def loadData(time):
    try:
        req = urllib2.Request(url=url.replace('ddddddd', time))
        req.add_header( 'Accept', 'application/json')
        req.add_header( 'Accept-Language', 'zh-CN,en-US;q=0.8')
        req.add_header( 'X-Requested-With', 'com.meiriyiwen.app')
        req.add_header( 'User-Agent', headers[random.randint(0,headers.__len__()-1)])
        #print req.get_full_url()
        response = urllib2.urlopen(req)
        result = response.read()
        return result
    except Exception, e:
        print e
        return 'Error : ' + e.message

def saveToFile(time,content):
    print content

if __name__ == "__main__":
    current_tiem = datetime.datetime.now()
    print current_tiem
    d = current_tiem.strftime('%Y%m%d')
    if sys.argv != None and len(sys.argv) == 2:
	d = sys.argv[1]
	print "usage: {}".format(sys.argv[1])
    data = loadData(d)
    if(data.__contains__('"status":1') ):
        file = open(root + d + ".json", "a+")
        file.write(data)
        file.close()
        print "Ok... : {}".format(d)

        f = root + d + ".json"
        token = q.upload_token(bucket_name, f.replace('/root/.ttt/',''), 3600)
        ret, info = put_file(token, f.replace('/root/.ttt/',''), f)
        if ret is not None:
		print "Put Ok : {}".format(f)
	else:
		print "Error: {}".format(f)
		print(info)
    else:
        print "Error : {}".format(d)


