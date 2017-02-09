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
import urllib
import urllib2
import cookielib
import requests

def test():
    cookie = cookielib.MozillaCookieJar('cookie.txt')
    hanlder = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(hanlder)
    url = "http://www.baidu.com"
    data = opener.open(url).read()
    print data
    print cookie._cookies.values()
    cookie.save(ignore_discard=True, ignore_expires=True)
    datas = requests.utils.dict_from_cookiejar(cookie)
    print cookie.get_dict()

if __name__ == "__main__":
    test()

