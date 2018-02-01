#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 下午7:58
# @Author  : Aries
# @Site    : 
# @File    : test.py
# @Software: PyCharm



import requests

headers = {
    'Referer': 'http://www.mzitu.com/11887/2'
}
with open('/Users/hukezhu/Desktop/scrapy/mzitu/123.jpg', 'wb') as file_writer:
    req = requests.get('http://i.meizitu.net/2013/09/956b8788d9f670b66312fe4b60974cae59df988fff5d-g9K9aN_fw580.jpg',headers=headers)
    file_writer.write(req.content)

file_writer.close()


if __name__ == '__main__':
    print('运行')