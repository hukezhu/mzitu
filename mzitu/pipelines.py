# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from mzitu.settings import IMAGES_STORE
import os
import requests

class MzituPipeline(ImagesPipeline):


    def process_item(self, item, spider):
        dir_path = '%s/%s/%s' % (IMAGES_STORE, spider.name,item["mzi_name"])  # 存储路径
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        image_link = item['mzi_image']
        str1 = item['mzi_index']
        if int(str1) == 0 :
            str1 = item['mzi_link']
        else:
            str1 = "%s/%s" % (item['mzi_link'] , item['mzi_index'])
        headers = {
            "Referer": str1,

        }
        list_name = image_link.split('/')
        file_name = list_name[len(list_name) - 1]  # 图片名称
        #print('%s------%s-------%s',image_link,list_name,file_name)
        file_count = file_name.split('.')
        # file_path = ' '
        # if len(file_count) > 2:
        #     tempname = file_count[len(file_count)-2]
        #     file_path = '%s/%s.jpg' % (dir_path, tempname)
        #     print('*************'*4)
        #     print(file_path)
        #     print('*************'*4)
        #
        # else:
        file_path = '%s/%s' % (dir_path, file_name)

        #print(file_path)
        if not os.path.exists(file_name):
            with open(file_path, 'wb') as file_writer:
                req = requests.get(image_link, headers=headers)
                file_writer.write(req.content)

        file_writer.close()

        return item
