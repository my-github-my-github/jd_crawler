# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt
import xlrd


class JdCrawlerPipeline(object):

    nrows = 1

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
        sheet = workbook.sheet_by_index(0)
        for index,field in enumerate(fields):
            sheet.put_cell(self.nrows,index,xlrd.XL_CELL_TEXT,item[field],None)
        self.nrows += 1

        wwb = xlwt.Workbook(encoding='utf-8')
        wsheet = wwb.add_sheet('comments')
        for row in range(sheet.nrows):
            for col in range(sheet.ncols):
                wsheet.write(row,col,str(sheet.cell_value(row,col)))
        wwb.save('newComments.xls')
        return item
