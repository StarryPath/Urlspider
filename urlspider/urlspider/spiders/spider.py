import scrapy
from urlspider.items import UrlspiderItem
import re


class UrlSpider(scrapy.Spider):
    name="Url"

    def __init__(self,category=None,*args,**kwargs):
        super(UrlSpider, self).__init__(*args, **kwargs)
        self.start_urls = ["%s" % category]


    def parse(self,response):
        urls_list1 = re.findall(r'href="(https?.*?\..*?)"' ,response.body)
        urls_list2 = re.findall(r'href=\'(https?.*?\..*?)\'', response.body)
        urls_list1.extend(urls_list2)
        s1=set(urls_list1)

        for url in s1:
            item = UrlspiderItem()
            item['url'] = url
            item['flag'] = 0
            yield item




