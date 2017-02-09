# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

class ChangeUA(object):
    def process_request(self, request, spider):
        agent = 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36'
        request.headers["User-Agent"] = agent

class ChangeCookie(object):
    def process_request(self, request, spider):
        cookie = {"SUHB": "0nlfnjxuMrjLk1", "SRF": "1486537312", "SUB": "_2A251nrIwDeRxGeRN4lQZ-CnOwjuIHXVW7aT4rDV8PUNbmtBeLVf4kW9NCSSHWRkbhLqUrh3RZMb7Y4j36g..", "SUBP": "0033WrSXqPxfM725Ws9jqgMF55529P9D9WF3iYEvxR3zQxuzqZu60I8w5JpX5K2hUgL.Foz01KqR1hME1KM2dJLoI7La9g9QUrLDIcYt", "YF-Ugrow-G0": "ea90f703b7694b74b62d38420b5273df", "ALF": "1518073312", "SCF": "AlSs6TH0jl38SZbTu9b87Z4U-V5AV8nOZmn_-vH7qS2EaPqZddNF9sqPykBPJcssGqTL83EW87vV3WOpbfWbsSk.", "ALC": "ac%3D27%26bt%3D1486537312%26cv%3D5.0%26et%3D1518073312%26scf%3D%26uid%3D2396887297%26vf%3D0%26vs%3D0%26vt%3D0%26es%3D06fb482c09959080e382cdcdc4514729", "sso_info": "v02m6alo5qztKWRk5yljpOQpZCToKWRk5iljoOgpZCjnLKMs6S2joOgt4yjpLeJp5WpmYO0soyzpLaOg6C3jKOktw==", "tgc": "TGT-MjM5Njg4NzI5Nw==-1486537311-gz-3CCE741693C237D91868926BAE1248EC-1", "LT": "1486537312", "SRT": "D.QqHBJZ4oUeHHWrMb4eYGSPHKiFoMd8sDU!y3TePHNEYdPqWYPDMpMERt4EPKRcsrAcPJPcRrTsVuO!iO4rYQ4ck8TmooPQHfJsHTOdz3dOMgJqSeI8t7*B.vAflW-P9Rc0lR-ykTDvnJqiQVbiRVPBtS!r3JZPQVqbgVdWiMZ4siOzu4DbmKPWFJ-bSMQSt4Ziw4QYs5eETWORnNOY3i49ndDPIJcYPSrnlMcywJDEIVPzoTmsEJ4kiJcM1OFyHiroYKdVu4PPpOmMHRsbr", "SSOLoginState": "1486537312"}
        request.cookies = cookie

class TweetinfoSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
