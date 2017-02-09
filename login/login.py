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
# -*-coding:utf8-*-
import urllib2
import codecs
from PIL import Image

def test():
    url = "http://weibo.com/login.php"
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Cache-Control':'max-age=0','Connection':'keep-alive','Cookie':'SINAGLOBAL=2819727573901.8047.1478913100260; wb_g_upvideo_5927363130=1; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; SCF=Ah2wEc7tB-4s3jjtEQ_a0ClRiRzOI0Bsxh5iGjgoWgSGfrWmIi4uorE_UCBxrWQIGSwN6tVgu680F-85Z31iPYg.; SUHB=0cSncTAyerc8ey; YF-V5-G0=73b58b9e32dedf309da5103c77c3af4f; _s_tentry=login.sina.com.cn; Apache=8460915598842.238.1486443268184; ULV=1486443268189:12:1:1:8460915598842.238.1486443268184:1485262861854; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a; SUB=_2AkMvxdw9dcPhrAZYmv8Wymjjb41H-jycELXLAn7uJhMyAxgv7nw_qSVu0VGgjpRPb_ya2eceTHn7OmI-7w..; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whlk2I2pFbMARLcSdf3bEwM5JpVF02NeK.7e0z4So5X; login_sid_t=20b9de3fa65c1bce6cab10b8bad170cc; UOR=,,login.sina.com.cn; WBStorage=ffbf906cea1ff551|undefined','Host':'weibo.com','If-Modified-Since':'Tue, 07 Feb 2017 05:07:10 GMT','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',}
    headers = {'User-Agent':user_agent}
    # headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36',}
    # headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Encoding':'gzip, deflate, sdch','Accept-Language':'zh-CN,zh;q=0.8','Cache-Control':'max-age=0','Connection':'keep-alive', 'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36', 'If-Modified-Since':'Tue, 07 Feb 2017 05:07:10 GMT','Upgrade-Insecure-Requests':'1',}
    request = urllib2.Request(url, headers=headers)
    htmls = urllib2.urlopen(request).read()
    print htmls

def test3():
    url = 'http://login.sina.com.cn/cgi/pin.php?r=46462333&s=0&p=gz-7b400c88cf3cddcfffee6217e0ed381c8814'
    h = urllib2.urlopen(url).read()
    f = open('img.png', 'wb')
    f.write(h)
    f.close()
    im = Image.open('img.png')
    im.show()

def test2():
    f = open('s.html', 'wb')
    f.write('2')
    f.close()



def test4():
    str = u'\u8f93\u5165\u7684\u9a8c\u8bc1\u7801\u4e0d\u6b63\u786e'
    print str


if __name__ == "__main__":
    test4()



