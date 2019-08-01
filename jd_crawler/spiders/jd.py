# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
import re
import json
from jd_crawler.items import JdCrawlerItem


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    start_urls = ['https://passport.jd.com/new/login.aspx']

    base_url = 'https://search.jd.com/Search?'


    def parse(self, response):
        formdata = {
            'loginname':'yourusername',
            'nloginpwd':'yourpassword'
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
        base_comment_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv%s&productId=%s&score=0&sortType=5&page=%d&pageSize=10&isShadowSku=0&fold=1'

        text = response.text
        skuid = response.url.split("/")[-1].replace('.html','')
        commentVersion = re.findall(r'commentVersion:\'(\d+)\'',text)[0]
        for x in range(0,1):
            url = base_comment_url%(commentVersion,skuid,x)
            yield scrapy.Request(url=url,callback=self.save_json_data)

    def save_json_data(self,response):
        text = response.text
        json_data = re.findall(r'fetchJSON_comment98vv\d+\((.*)\);',text)[0]
        comments_dict = json.loads(json_data)
        comments = comments_dict['comments']

        for comment in comments:
            try:
                item = JdCrawlerItem(id=comment['id'], topped=comment['topped'], guid=comment['guid'], content=comment['content'], creationTime=comment['creationTime'], isTop=comment['isTop'], referenceId=comment['referenceId'], referenceImage=comment['referenceImage'], referenceName=comment['referenceName'], referenceTime=comment['referenceTime'], referenceType=comment['referenceType'], referenceTypeId=comment['referenceTypeId'], firstCategory=comment['firstCategory'], secondCategory=comment['secondCategory'], thirdCategory=comment['thirdCategory'], replyCount=comment['replyCount'], replyCount2=comment['replyCount2'], score=comment['score'], status=comment['status'], title=comment['title'], usefulVoteCount=comment['usefulVoteCount'], uselessVoteCount=comment['uselessVoteCount'], userImage=comment['userImage'], userImageUrl=comment['userImageUrl'], userLevelId=comment['userLevelId'], userProvince=comment['userProvince'], viewCount=comment['viewCount'], orderId=comment['orderId'], isReplyGrade=comment['isReplyGrade'], nickname=comment['nickname'], userClient=comment['userClient'], images=comment['images'], showOrderComment=comment['showOrderComment'], mergeOrderStatus=comment['mergeOrderStatus'], discussionId=comment['discussionId'], productColor=comment['productColor'], productSize=comment['productSize'], imageCount=comment['imageCount'], integral=comment['integral'], userImgFlag=comment['userImgFlag'], anonymousFlag=comment['anonymousFlag'], userLevelName=comment['userLevelName'], plusAvailable=comment['plusAvailable'], productSales=comment['productSales'], mobileVersion=comment['mobileVersion'], aesPin=comment['aesPin'], officialsStatus=comment['officialsStatus'], excellent=comment['excellent'], recommend=comment['recommend'], userLevelColor=comment['userLevelColor'], userClientShow=comment['userClientShow'], isMobile=comment['isMobile'], days=comment['days'], afterDays=comment['afterDays']
    )
            except:
                continue
            yield item

