# -*- coding: utf-8 -*-
import scrapy
import json
import os


class A53Spider(scrapy.Spider):
    name = "53"
    allowed_domains = ["53ex.com","120.24.68.187"]
    start_urls = ['http://53ex.com/user.php']
    userid = 0
    api = ""
    s = 0
    pagejsnum = 1000

    def stod(self,str):
    	new = []
    	for s in str:
    		s = s.split(';')
    		new.extend(s)
    	dic = {}
    	for s in new:
    		s = s.strip()
    		s = s.split('=')
    		dic[s[0]] = s[1]
    	return dic


    def get_new_cookie(self,response):
    	old_cookie = response.request.headers.getlist('cookie')
    	old_cookie = self.stod(old_cookie)
    	new_cookie = response.headers.getlist('set-cookie')
    	new_cookie = self.stod(new_cookie)
    	old_cookie.update(new_cookie)
    	return old_cookie


    def parse(self, response):
        cookies = self.get_new_cookie(response)
        params = {'username':'周宝良',
		'password':'123456',
		'act':'act_login',
		'back_act':'http://53ex.com/',
		'submit':''}
	url = 'http://53ex.com/user.php'
	yield scrapy.FormRequest(url,cookies = cookies,formdata=params,callback=self.login)

    def login(self,response):
	print('--------/n/n/n')
	print(response.status)
        print(response.request.headers.getlist('cookie'))
        print('-----------')
        cookies = self.get_new_cookie(response)
        print(cookies)
	print('/n/n/n---------')
        url = 'http://53ex.com/diamond.html'
        yield scrapy.FormRequest(url,cookies=cookies,callback=self.diamond)

    def diamond(self,response):
        with open('diamond.html','w') as f:
            f.write(response.body)
        print('==========\n\n\n')
        print(response.status)
        print(response.request.headers.getlist('cookie'))
        self.userid = response.css('html').re('var userid="([\d]*?)";')[0]
        print(self.userid)
        print('---------')
        cookies = self.get_new_cookie(response)
        print(cookies)
        print('\n\n\n==========')
        url1 = 'http://53ex.com/js/diamond.js'
        yield scrapy.FormRequest(url1,cookies=cookies,callback=self.diamondjs)

    def diamondjs(self,response):
        print('************\n\n')
        self.api = response.css('html').re('var url_api="([\S]*?)";')[0]
        print(self.api)
        print('\n\n************')
        self.api = self.api.replace('&amp;','&')
        url2 = '%s%s%s%s%s%s%s' %(self.api,'s=',self.s,'&userid=',self.userid,'&pagejsnum=',self.pagejsnum)
        print('++\n')
        print(url2)
        print('\n++')
        yield scrapy.FormRequest(url2,callback=self.diainfo)

    def diainfo(self,response):
        self.s = self.s + 1000
        r = json.loads(response.body)
        with open('diajson.txt','a') as f:
            for i in r[1:]:
                f.write(json.dumps(i))
                f.write(',')
        page = int(r[0]['show_page'])
        print('????\n')
        print(r[0])
        print(self.s)
        print('\n????')
        if self.s <= page:
            url2 = '%s%s%s%s%s%s%s' %(self.api,'s=',self.s,'&userid=',self.userid,'&pagejsnum=',self.pagejsnum)
            yield scrapy.FormRequest(url2,callback=self.diainfo)



