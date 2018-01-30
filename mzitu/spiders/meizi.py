# -*- coding: utf-8 -*-
import scrapy
from mzitu.items import MzituItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://www.mzitu.com/']

    def parse(self, response):
        next_page = response.xpath('//a[@class="next page-numbers"]/text()').extract()[0]
        next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract()[0]
        pagesize = response.xpath('//div[@class="nav-links"]/a/text()').extract()[-2]
        baseURl = "http://www.mzitu.com/page/"
        url = ' '
        for i in range(1,int(pagesize)):
            if i == 1:
                url = "http://www.mzitu.com"
            else:
                url = baseURl + str(i) + '/'
            yield scrapy.Request(url, callback=self.parse_next)


    def parse_next(self,response):

        node_list = response.xpath('//ul[@id="pins"]/li')
        items = []
        for node in node_list:
            item = MzituItem()
            mzi_name = node.xpath('./span[1]/a/text()').extract()[0]
            mzi_link = node.xpath('./span[1]/a/@href').extract()[0]
            mzi_time = node.xpath('./span[2]/text()').extract()[0]
            mzi_view = node.xpath('./span[3]/text()').extract()[0]

            item["mzi_name"] = mzi_name
            item["mzi_link"] = mzi_link
            item["mzi_time"] = mzi_time
            item["mzi_view"] = mzi_view

            items.append(item)

        for item in items:
            yield scrapy.Request(item["mzi_link"], meta={"item": item}, callback=self.parse_detail)

    def parse_detail(self,response):
        item_detail = response.meta["item"]
        imageurl = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract()[0]
        imagelist = response.xpath('//div[@class="pagenavi"]/a/span/text()').extract()[-2]



        baseURl = imageurl.split('01.jpg')[0]
        index = int(imagelist)
        image_src = ''
        for i in range(1,index):
            if i < 10 :
                image_src = baseURl + '0' + str(i) + '.jpg'
            else:
                image_src = baseURl + str(i) + '.jpg'

            item = MzituItem()
            item["mzi_name"] = item_detail["mzi_name"]
            item["mzi_link"] = item_detail["mzi_link"]
            item["mzi_time"] = item_detail["mzi_time"]
            item["mzi_view"] = item_detail["mzi_view"]
            item["mzi_image"] = image_src
            if i == 1:
                item['mzi_index'] = 0
            else:
                item['mzi_index'] = i - 1

            yield item

