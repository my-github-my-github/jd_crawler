# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt
import xlrd
from xlutils.copy import copy


class JdCrawlerPipeline(object):


    def process_item(self, item, spider):
        fields = ['id', 'topped', 'guid', 'content', 'creationTime', 'isTop', 'referenceId', 'referenceImage',
                'referenceName', 'referenceTime', 'referenceType', 'referenceTypeId', 'firstCategory', 'secondCategory',
                'thirdCategory', 'replyCount', 'replyCount2', 'score', 'status', 'title', 'usefulVoteCount',
                'uselessVoteCount', 'userImage', 'userImageUrl', 'userLevelId', 'userProvince', 'viewCount', 'orderId',
                'isReplyGrade', 'nickname', 'userClient', 'images', 'showOrderComment', 'mergeOrderStatus',
                'discussionId', 'productColor', 'productSize', 'imageCount', 'integral', 'userImgFlag', 'anonymousFlag',
                'userLevelName', 'plusAvailable', 'productSales', 'mobileVersion', 'aesPin', 'officialsStatus',
                'excellent', 'recommend', 'userLevelColor', 'userClientShow', 'isMobile', 'days', 'afterDays']
        workbook = xlrd.open_workbook('comments.xls')
        rsheet = workbook.sheet_by_index(0)
        nrows = rsheet.nrows
        wb = copy(workbook)
        sheet = wb.get_sheet(0)
        for index,field in enumerate(fields):
            sheet.write(nrows,index,label = str(item[field]))
        wb.save('comments.xls')

        return item
