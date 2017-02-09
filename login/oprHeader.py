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

def getHeader(str):
    lines = str.split('\n')
    dict_str = ''
    i = 0
    for line in lines:
        datas = line.split(':')
        header = datas[0]
        data = ':'.join(datas[1:])
        if i==2:
            continue
        dict_str += "'"+header+"':'"+data+"',"
        print header
        print data
    return dict_str

if __name__ == "__main__":
    str = '''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Cookie:SINAGLOBAL=2819727573901.8047.1478913100260; wb_g_upvideo_5927363130=1; YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; SCF=Ah2wEc7tB-4s3jjtEQ_a0ClRiRzOI0Bsxh5iGjgoWgSGfrWmIi4uorE_UCBxrWQIGSwN6tVgu680F-85Z31iPYg.; SUHB=0cSncTAyerc8ey; YF-V5-G0=73b58b9e32dedf309da5103c77c3af4f; _s_tentry=login.sina.com.cn; Apache=8460915598842.238.1486443268184; ULV=1486443268189:12:1:1:8460915598842.238.1486443268184:1485262861854; YF-Page-G0=b98b45d9bba85e843a07e69c0880151a; SUB=_2AkMvxdw9dcPhrAZYmv8Wymjjb41H-jycELXLAn7uJhMyAxgv7nw_qSVu0VGgjpRPb_ya2eceTHn7OmI-7w..; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whlk2I2pFbMARLcSdf3bEwM5JpVF02NeK.7e0z4So5X; login_sid_t=20b9de3fa65c1bce6cab10b8bad170cc; UOR=,,login.sina.com.cn; WBStorage=ffbf906cea1ff551|undefined
Host:weibo.com
If-Modified-Since:Tue, 07 Feb 2017 05:07:10 GMT
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.100 Safari/537.36'''
    header = getHeader(str)
    print header