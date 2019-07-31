# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv1174&productId=100003150357&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1']


    def parse(self, response):
        text = response.text
        print(text)
