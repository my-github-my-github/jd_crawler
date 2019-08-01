# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://passport.jd.com/new/login.aspx']

    base_url = 'https://search.jd.com/Search?'


    def parse(self, response):
        formdata = {
            'loginname':'18735417848',
            'nloginpwd':'ZFE.014789'
        }
        yield scrapy.FormRequest.from_response(response,formdata=formdata,formid='formlogin',callback=self.parse_page)

    def parse_page(self,response):
        data = {
            'keyword':'电脑台式',
            'enc':'utf-8',
            'wd':'电脑台式'
        }
        search = parse.urlencode(data)
        url = self.base_url + search
        request = scrapy.Request(url=url,callback=self.parse_profile)
        yield request

    def parse_profile(self,response):
        ul = response.xpath("//ul[@class='gl-warp clearfix']")
        lis = ul.xpath(".//li")
        for li in lis:
            a = li.xpath(".//a/@href").get()
            url = response.urljoin(a)
            yield scrapy.Request(url=url,callback=self.parse_comment_url)

    def parse_comment_url(self,response):
        base_comment_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&productId=%s&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'

        text = response.text
        skuid = response.url.split("/")[-1].replace('.html','')
        commentVersion = re.findall(r'commentVersion:\'(\d+)\'',text)[0]
        url = base_comment_url%(commentVersion,skuid)
        yield scrapy.Request(url=url,callback=self.save_json_data)

    def save_json_data(self,response):
        text = response.text
        json_data = re.findall(r'fetchJSON_comment98vv\d+\((.*)\);',text)[0]
        print(json_data)

