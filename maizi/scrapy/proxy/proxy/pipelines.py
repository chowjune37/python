# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import pymysql.cursors
import socket,struct

class ProxyPipeline(object):
    def process_item(self, item, spider):
        reload(sys)
        sys.setdefaultencoding('utf8')
        # DBKWARGS = spider.settings.get('DBKWARGS')
        print('gggggggggg')
        con = pymysql.connect(host='52.38.255.237',port=3306,user='root',password='6JunYan9',db='store',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
        print(con)
        ip = item['ip']
        ip = socket.inet_aton(ip)
        ip = struct.unpack("!L",ip)[0]
        port = item['port']
        port = int(port)
        type = item['type']
        with con.cursor() as f:
            print(f)
            sql = "INSERT INTO proxy(ip,port,alpha,type) VALUES(%s,%s,%s,%s)"
            a = f.execute(sql,(ip,port,1,type))
            print(a)
        con.commit()
        con.close()
        c = ip + '---' + port + '---' + type + '---\n'
        with open('a.txt','a') as f:
            f.write(c)
        return item    

    def open_spider(self,spider):
    	print('\n\n\n------open------\n\n\n')

    def close_spider(self,spider):
    	print('\n\n\n------close-----\n\n\n')
