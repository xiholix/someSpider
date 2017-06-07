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
'''
@version: ??
@author: xiholix
@contact: x123872842@163.com
@software: PyCharm
@file: crawlOnePerson.py
@time: 17-5-27 上午9:34
'''
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import re
import urllib2
import urllib
import time
import codecs
import json


path = 'data/'

def get_header():
    s = '''Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Cookie:你的cookie
Host:weibo.com
Pragma:no-cache
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'''
    headers = {}
    datas = s.split('\n')
    for d in datas:
        ds = d.split(':')
        key = ds[0]
        value = ':'.join(ds[1:])
        headers[key] = value
    # print(len(headers))
    # print(headers.keys())
    return headers


def parse_firstlayer(_s):
    configPattern = r'domain\']=\'(.*?)\''
    configNum = re.findall(configPattern, _s, re.DOTALL)[0]
    # print(configNum)
    pageIdPattern = r'page_id\']=\'(.*?)\''
    pageId = re.findall(pageIdPattern, _s, re.DOTALL)[0]
    # print(pageId)
    return configNum, pageId


def parse_page(_m, _f=None, _next=False):
    datas = json.loads(_m)
    datas = datas['data']
    h_pattern = "<em class=\"W_ficon ficon_arrow_down S_ficon.*?</em>(.*?)<!--"
    pattern = "(tbinfo=.*?feed_list_repeat)"
    texts = re.findall(pattern, datas, re.DOTALL)
    href = re.findall(h_pattern, datas, re.DOTALL)
    if(len(texts)==0):
        return True
    # print(texts)
    for data in texts:
        pattern = "<.*?feed_list_content.*?>(.*?)</div>"
        tex = re.findall(pattern, data, re.DOTALL)
        time_pattern = "WB_from(.*?)node-type"
        time = re.findall(time_pattern, data, re.DOTALL)[0]
        time_pattern = "title=\"(.*?)\""
        # print time
        times = re.findall(time_pattern, time, re.DOTALL)
        print(times[0] + "\t" + tex[0].strip())
        _f.write(times[0] + "\t" + tex[0].strip()+'\n')


def crawl_one_person(_uid="3195238794"):
    url = 'http://weibo.com/u/'+_uid+'?is_all=1#place'
    fpath = path+_uid
    f = codecs.open(fpath, 'a', 'utf-8')
    # print(url)
    header = get_header()
    # print(header)
    request = urllib2.Request(url, headers=header)
    reader = urllib2.urlopen(request)
    # print(reader)
    data = reader.read()
    # print(data)
    domain, id = parse_firstlayer(data)
    page=1
    pageBar =1
    prePage =1
    for i in xrange(1,10000):
        page = i
        prePage = i-1
        pageBar = 0
        dataUrl = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=' + domain + '&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=' + str(
            page) + '&pagebar=' + str(
            pageBar) + '&id=' + id + '&script_uri=/u/' + _uid + '&feed_type=0&pre_page=' + str(
            prePage) + '&domain_op=' + domain
        print(dataUrl)
        request = urllib2.Request(dataUrl, headers=header)
        reader = urllib2.urlopen(request)
        # print(reader)
        data = reader.read()
        sign = parse_page(data, f)
        if sign:
            break
        time.sleep(2)
        page = i
        prePage = i
        pageBar = 0
        dataUrl = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=' + domain + '&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=' + str(
            page) + '&pagebar=' + str(
            pageBar) + '&id=' + id + '&script_uri=/u/' + _uid + '&feed_type=0&pre_page=' + str(
            prePage) + '&domain_op=' + domain
        print(dataUrl)
        request = urllib2.Request(dataUrl, headers=header)
        reader = urllib2.urlopen(request)
        # print(reader)
        data = reader.read()
        parse_page(data, f)
        if sign:
            break
        time.sleep(2)
        page = i
        prePage = i
        pageBar = 1
        dataUrl = 'http://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=' + domain + '&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=' + str(
            page) + '&pagebar=' + str(
            pageBar) + '&id=' + id + '&script_uri=/u/' + _uid + '&feed_type=0&pre_page=' + str(
            prePage) + '&domain_op=' + domain
        print(dataUrl)
        request = urllib2.Request(dataUrl, headers=header)
        reader = urllib2.urlopen(request)
        # print(reader)
        data = reader.read()
        parse_page(data, f)

        if sign:
            break
        time.sleep(2)
    print('all done')



if __name__ == "__main__":
    crawl_one_person('1654619934')