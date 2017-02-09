# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
from tweetInfo.items import TweetinfoItem
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class TweetinfoPipeline(object):
    def process_item(self, item, spider):
        f = codecs.open('info.d','a', 'utf8')
        write_str = item['id']+'\t'+item['follow_num']+'\t'+item['fans_num']+'\t'+item['tweet_num'] +'\t'+\
                    item['sex']+'\t'+item['name']+'\t'+item['address']+'\t'+item['intro']+'\n'
        f.write(write_str)
        f.close()
        return item
