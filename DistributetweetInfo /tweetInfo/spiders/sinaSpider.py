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

from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.http import Request
import codecs
import re
from tweetInfo.items import TweetinfoItem

class SinaSpider(RedisCrawlSpider):
    name = "sinaSpider"
    ids = [2342539633, ]
    redis_key = "distritue:start_urls"
    start_urls = ['http://weibo.com/u/2342539633',]
    base_url = 'http://weibo.com/u/'

    def start_requests(self):
        for id in self.ids:
            url = self.base_url +str(id)
            yield Request(url=url, callback=self.parse)
            # url = 'http://weibo.com/p/1005052342539633/follow?pids=Pl_Official_HisRelation__60&page=2&ajaxpagelet=1&ajaxpagelet_v6=1&__ref=/p/1005052342539633/follow?from=page_100505&wvr=6&mod=headfollow#place&_t=FM_148655543680534'
            # url = 'http://weibo.com/p/1005051497035431/follow?page=1'
            # url = 'http://weibo.com/p/1005053585184995/follow?page=1'
            # yield Request(url=url, callback=self.parse2)

    def parse(self, response):
        text = response.text
        pattern = r'page_id.*?(\d+)'
        id = re.findall(pattern, text, re.DOTALL)[0]
        url = 'http://weibo.com/p/'+id+'/follow?page=1'
        yield Request(url=url, callback=self.parse2)

    def parse2(self, response):
        text = response.text
        _url = response.request._url
        idPattern = 'page=(\d+)'
        id = re.findall(idPattern, _url, re.DOTALL)[0]
        id = int(id)
        nextPage = r'page next S_txt1 S_line1(.*?)<span>下一页'
        is_next = re.findall(nextPage, text.encode('utf8'), re.DOTALL)
        if len(is_next) > 0:
            is_next = is_next[0]
        if 'href' in is_next:
            is_next = True
        else:
            is_next = False
        pattern = r'<li class(.*?)t<\\/li>'
        pattern = r'<li class(.*?)<\\/dl>\\r\\n\\t<\\/li>'
        pattern2 = r'uid=(\d+)'
        pattern3 = r'fnick=(.*?)&'
        datas = re.findall(pattern, text, re.DOTALL)
        id_list = []
        print len(datas)
        for data in datas:
                item = TweetinfoItem()
                self.oprInfos(data.encode('utf8'), item, _url)     #一定要加这个encode('utf8')否则无法识别中文的模式
                id_list.append(item['id'])
                yield item
        for url_id in id_list:
            url = self.base_url+url_id
            yield Request(url, callback=self.parse)
        print is_next
        if is_next and (id<5):
            id += 1
            _url = re.sub(idPattern, 'page='+str(id), _url, re.DOTALL)
            yield Request(_url, callback=self.parse2)

    def oprInfos(self, text, item, _url):
        pattern2 = r'uid=(\d+)'
        pattern3 = r'fnick=(.*?)&'
        followNum = r'follow\\" >(.\d+?)<'
        sexStr = r'W_icon icon_(male|female)'
        addressPattern = r'地址<\\/em><span>(.*?)<'
        fansNumPattern = r'=fans\\" >(.\d+?)<'
        tweetNumPattern = r'微博<.*?(\d+?)<'
        introPattern = r'info_intro\\">(.*?)<\\/div>'
        meansPattern = r'通过<.*?>(.*?)<'
        uid = re.findall(pattern2, text, re.DOTALL)
        nick = re.findall(pattern3, text, re.DOTALL)
        follow_num = re.findall(followNum, text, re.DOTALL)
        sex = re.findall(sexStr, text, re.DOTALL)
        address = re.findall(addressPattern, text, re.DOTALL)
        fans_num = re.findall(fansNumPattern, text, re.DOTALL)
        tweet_num = re.findall(tweetNumPattern, text, re.DOTALL)
        intro = re.findall(introPattern, text, re.DOTALL)
        means = re.findall(meansPattern, text, re.DOTALL)
        if len(uid)>0:
            uid = uid[0]
        else:
            uid=''
        if len(nick)>0:
            nick=nick[0]
        else:
            nick=''
        if len(follow_num)>0:
            follow_num = follow_num[0]
        else:
            follow_num=''
        if len(sex)>0:
            sex=sex[0]
        else:
            sex=''
        if len(address)>0:
            address=address[0]
        else:
            address=''
        if len(fans_num)>0:
            fans_num=fans_num[0]
        else:
            fans_num=''
        if len(tweet_num)>0:
            tweet_num=tweet_num[0]
        else:
            tweet_num=''
        if len(intro)>0:
            intro=intro[0]
        else:
            intro=''
        if len(means)>0:
            means = means[0]
        else:
            means=''
        print uid+'\t'+nick+'\t'+follow_num+'\t'+fans_num+'\t'+tweet_num+'\t'+means+'\t'+sex+'\t'+address+'\t'+intro
        if fans_num==''and tweet_num=='':
            fans_num = _url
        item["id"] = uid
        item["name"] = nick
        item["follow_num"] = follow_num
        item['fans_num'] = fans_num
        item['tweet_num'] = tweet_num
        item['means'] = means
        item['sex'] = sex
        item['address'] = address
        item['intro'] = intro
        return item