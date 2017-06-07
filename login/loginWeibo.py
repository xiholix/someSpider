# -*-coding:utf8-*-
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永无BUG
#
#
import re
import execjs
import urllib2
import urllib
import cookielib
from PIL import Image
import requests

def test():
    username = raw_input("输入用户名:")
    password = raw_input("输入密码:")
    login(username, password)

def login(username, password):
    myname = getName(username)
    # print len(password)
    # print len(username)
    nonce, servertime, pubkey, showpin, rsakv = getSomeInfo(myname)
    mypass = getPassword(password, nonce, servertime, pubkey)
    pincode = ''
    cj = ''
    cookievalue=''
    showpin='1'
    if showpin=='1':
        cj, cookievalue = getPinCode('')
        pincode = raw_input("输入验证码")
    print pincode
    postdata = {'nonce':nonce, 'servertime':servertime, 'su':myname, 'sp':mypass, 'pagerefer':'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',
                'entry':"weibo", 'gateway':"1"}
    if showpin=='1':
        return pinLogin(myname,servertime, nonce, rsakv, mypass, cookievalue, pincode)
    else:
        return noPinLogin(myname, servertime, nonce, rsakv, mypass)
    #     data = {
    #         'entry': 'weibo',
    #         'gateway': '1',
    #         'from': '',
    #         'savestate': '7',
    #         'useticket': '1',
    #         'pagerefer': "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl",
    #         'vsnf': '1',
    #         'su': myname,
    #         'service': 'miniblog',
    #         'servertime': servertime,
    #         'nonce': nonce,
    #         'pwencode': 'rsa2',
    #         'rsakv': rsakv,
    #         'sp': mypass,
    #         'sr': '1366*768',
    #         'encoding': 'UTF-8',
    #         'prelt': '115',
    #         'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    #         'returntype': 'META',
    #         'pcid':cookievalue,
    #         'door':pincode,
    #     }
    # else:
    #     data = {
    #         'entry': 'weibo',
    #         'gateway': '1',
    #         'from': '',
    #         'savestate': '7',
    #         'useticket': '1',
    #         'pagerefer': "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl",
    #         'vsnf': '1',
    #         'su': myname,
    #         'service': 'miniblog',
    #         'servertime': servertime,
    #         'nonce': nonce,
    #         'pwencode': 'rsa2',
    #         'rsakv': rsakv,
    #         'sp': mypass,
    #         'sr': '1366*768',
    #         'encoding': 'UTF-8',
    #         'prelt': '115',
    #         'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    #         'returntype': 'META',
    #     }
    # postdata = urllib.urlencode(data)
    # login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    # data = urllib2.Request(login_url, postdata)
    # if cj!='':
    #     cj = cookielib.CookieJar()
    #     opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # #     opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
    # #     opener.addheaders.append(('Cookie', 'ULOGIN_IMG='+cookievalue))
    #     urllib2.install_opener(opener)
    # datas = urllib2.urlopen(data).read().decode('gb2312')
    # print datas
    # pattern = "replace\('(.*?)'"
    # new_url = re.findall(pattern, datas, re.DOTALL)[0]
    # print new_url
    #
    # infos = urllib2.urlopen(new_url).read()
    # print infos.decode('gb2312')
    # cookies = requests.utils.dict_from_cookiejar(cj)
    # return cookies


def pinLogin(myname, servertime, nonce, rsakv, mypass, cookievalue, pincode):
    data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'useticket': '1',
        'pagerefer': "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl",
        'vsnf': '1',
        'su': myname,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': rsakv,
        'sp': mypass,
        'sr': '1366*768',
        'encoding': 'UTF-8',
        'prelt': '115',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
        'pcid': cookievalue,
        'door': pincode,
    }
    postdata = urllib.urlencode(data)
    login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    data = urllib2.Request(login_url, postdata)

    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #     opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)')]
        #     opener.addheaders.append(('Cookie', 'ULOGIN_IMG='+cookievalue))
    urllib2.install_opener(opener)
    datas = urllib2.urlopen(data).read().decode('gb2312')
    print datas
    pattern = "replace\('(.*?)'"
    try:
        new_url = re.findall(pattern, datas, re.DOTALL)[0]
        print new_url

        infos = urllib2.urlopen(new_url).read()
        print infos.decode('gb2312')
        cookies = requests.utils.dict_from_cookiejar(cj)
        path = 'img/'+pincode+'.png'
        print path
        with open(path, 'wb') as f:
            im = open('pin.png')
            f.write(im.read())
        return cookies
    except Exception:
        # cj, cookievalue = getPinCode('')
        # pincode=raw_input('验证码错误，请重新输入验证码：')
        # print pincode
        # return pinLogin(myname, servertime, nonce, rsakv, mypass, cookievalue, pincode)
        return 1

def noPinLogin(myname, servertime, nonce, rsakv, mypass):
    data = {
        'entry': 'weibo',
        'gateway': '1',
        'from': '',
        'savestate': '7',
        'useticket': '1',
        'pagerefer': "http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl",
        'vsnf': '1',
        'su': myname,
        'service': 'miniblog',
        'servertime': servertime,
        'nonce': nonce,
        'pwencode': 'rsa2',
        'rsakv': rsakv,
        'sp': mypass,
        'sr': '1366*768',
        'encoding': 'UTF-8',
        'prelt': '115',
        'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
        'returntype': 'META',
    }
    postdata = urllib.urlencode(data)
    login_url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'
    data = urllib2.Request(login_url, postdata)
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    datas = urllib2.urlopen(data).read()
    print datas
    # print datas
    # arrURLPattern = r'arrURL":\[(.*?)]'
    # arrURL = re.findall(arrURLPattern, datas, re.DOTALL)
    # print arrURL
    # arrURL = arrURL[0].split(',')
    # urls = []
    # login_url = 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&sudaref=weibo.com'
    # for a in arrURL:
    #     urls.append(re.sub(r'\\','',a.strip('"')) )
    # # for url in urls:
    # extract_info_url_page = urllib2.urlopen(urls[1]).read()
    url_pattern = "replace\('(.*?)'"
    url = re.findall(url_pattern, datas, re.DOTALL)[0]
    infos = urllib2.urlopen(url).read()
    return requests.utils.dict_from_cookiejar(cj)

def getName(name):  #调用js加密用户名
    with open('sslogin.js', 'r') as f:
        source = f.read()
        phantom = execjs.get("PhantomJS")
        getPass = phantom.compile(source)
        myname = getPass.call("get_name", name)
        return myname

def getPassword(password, nonce, servertime, rsakey): #调用js加密密码
    with open('sslogin.js', 'r') as f:
        source = f.read()
        phantom = execjs.get("PhantomJS")
        getPass = phantom.compile(source)
        mypass = getPass.call("get_pass", password, nonce, servertime, rsakey)
        return mypass

def getPinCode(url): #获得验证码
    url = 'http://login.sina.com.cn/cgi/pin.php?r=47335104&s=0&p=gz-616fe88d0c7c51642c0998a2e088f6f7377b'
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    bindatas = urllib2.urlopen(url).read()
    with open("pin.png", 'wb') as f:
        f.write(bindatas)
    im = Image.open('pin.png')
    im.show()
    print 'cookie is '
    cookie_str = cj._cookies.values()[0]
    print str(cookie_str)
    value = re.findall("value='(.*?)',", str(cookie_str), re.DOTALL)[0]
    print value
    return cj, value


def getSomeInfo(name):  #获得预登陆信息
    url = 'https://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su='+name+'&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.18)&_=1486516984909'
    datas = urllib2.urlopen(url).read()
    print datas
    nonce = re.findall('nonce":"(.*?)",', datas, re.DOTALL)[0]
    servertime = re.findall('servertime":(.*?),', datas, re.DOTALL)[0]
    pubkey = re.findall('pubkey":"(.*?)",', datas, re.DOTALL)[0]
    showpin = re.findall('showpin":(.*?),', datas, re.DOTALL)[0]
    rsakv = re.findall('rsakv":"(.*?)",', datas, re.DOTALL)[0]
    return nonce, servertime, pubkey, showpin, rsakv

def loginPass():
    account ={
     'bangchangge674@yeah.net':'a123456',
     'pengpi1429@yeah.net':'a123456',
     'bi15324@yeah.net':'a123456',
     'xuan62893@yeah.net':'a123456',
     'hanlingyi47@yeah.net':'a123456',
     'yabeiqii132177@yeah.net':'a123456',
     'zhuansi515480@yeah.net':'a123456',
     'shen961736@yeah.net':'a123456',
     'yingju21772@yeah.net':'a123456',
     'rongtaicui444@yeah.net':'a123456',
     'jiaoraohui09143@yeah.net':'a123456',
     'fei044646@yeah.net':'a123456',
    }
    cookies_list = []
    error_list = {}
    for acc, password in account.items():
        print acc
        # print login('18604022628', 'huhu0769')
        data = login(acc, password)
        if data!=1:
            cookies_list.append(data)
        else:
            error_list[acc] = password
    while error_list:
        account = error_list
        error_list = {}
        for acc, password in account.items():
            print acc
            # print login('18604022628', 'huhu0769')
            data = login(acc, password)
            if data != 1:
                cookies_list.append(data)
            else:
                error_list[acc] = password
    print cookies_list
    import pickle
    pickle.dump(cookies_list, open('cookies.d','wb'))


def getPicture():
    account =[
     'bangchangge674@yeah.net:a123456',
     'pengpi1429@yeah.net:a123456',
     'bi15324@yeah.net:a123456',
     'xuan62893@yeah.net:a123456',
     'hanlingyi47@yeah.net:a123456',
     'yabeiqii132177@yeah.net:a123456',
     'zhuansi515480@yeah.net:a123456',
     'shen961736@yeah.net:a123456',
     'yingju21772@yeah.net:a123456',
     'rongtaicui444@yeah.net:a123456',
     'jiaoraohui09143@yeah.net:a123456',
     'fei044646@yeah.net:a123456',
    ]
    import random
    while True:
        key,value = random.choice(account).split(':')
        login(key, value)

if __name__ == "__main__":
    # us = u'\u4e3a\u4e86\u60a8\u7684\u5e10\u53f7\u5b89\u5168\uff0c\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801'
    # print us
    pass
    # loginPass()
    getPicture()







































