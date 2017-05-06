# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys

class DemoPipeline(object):
	r = "text"

	def process_item(self,item,spider):
		print('\n\n\n************\n\n\n')
		print(sys.getdefaultencoding())
		co = item['co'].replace('/','-')
		if not co or co == " ":
			if not os.path.exists(self.r + '/' + item['year']):
				os.makedirs(self.r + '/' + item['year'])
			f = open(self.r + '/' + item['year'] + '/' + item['name'] + '.txt','w')
			f.write(item['idn'])
			f.close()
			print('\n\n\n************\n\n\n')
			return item
		if not os.path.exists(self.r + '/' + item['year'] + '/' + co):
			os.makedirs(self.r + '/' + item['year'] + '/' + co)
		f = open(self.r + '/' + item['year'] + '/' + co + '/' + item['name'] + '.txt','w')
		f.write(item['idn'])
		f.close()
		print('\n\n\n***********\n\n\n')
		return item


	def open_spider(self,spider):
		print('\n\n\n^^^^^^^^^^^^^\n\n\n')
		reload(sys)
		print(sys.setdefaultencoding('utf-8'))
		if not os.path.exists(self.r):
			os.mkdir(self.r)
		print('\n\n\n^^^^^^^^^^^^^\n\n\n')

	def close_spider(self,spider):
		print('\n\n\n$$$$$$$$$$$ bye $$$$$$$$\n\n\n')
