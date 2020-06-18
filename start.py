# coding: utf-8
"""
@File    : start.py
@Time    : 2020/5/16 12:55
@Author  : Cao.Yong
"""
#执行start.py 启动爬虫 或在cmd命令行执行 scrapy crawl suning_spider
from scrapy import cmdline

cmdline.execute("scrapy crawl suning_spider".split())

