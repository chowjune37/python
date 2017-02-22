# -*- coding:utf-8 -*- 

import os
import urllib.request
import re

def sphinx():

    url = 'http://www.qiushibaike.com'
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/602.4.8 (KHTML, like Gecko) Version/10.0.3 Safari/602.4.8"}
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read()
    f = open('index.html','w')
    f.write(html.decode("utf-8"))
    f.close()
    response.close()

    page_number_compile = re.compile('<!--<a href="([\S]+)" rel="nofollow">-->\n<span class="page-numbers">\n([\d]{1,2})\n</span>') 
    page_number_findall = page_number_compile.findall(html.decode('utf8'))
    total_page = page_number_findall[-1] 

    page_number_compile = re.compile('<span class="current" >\n([\d]{1,2})\n</span>')
    page_number_findall = page_number_compile.findall(html.decode('utf8'))
    page_now = page_number_findall

    page_number_compile = re.compile('<!--<a href="([\S]+)" rel="nofollow">-->\n<span class="next">\n([\S]+?)\n</span>')
    page_number_findall = page_number_compile.findall(html.decode('utf8'))
    page_next = page_number_findall
 
    page_contants_compile = re.compile('<a href="/article/([\d]+)" target="_blank" class=\'contentHerf\' >\n<div class="content">([\s,\S]*?)</div>')
    page_contants_findall = page_contants_compile.findall(html.decode('utf8'))
    page_contants = page_contants_findall

    print(total_page)
    print(page_now)
    print(page_next)
    print(page_contants)

    for contant in page_contants:
        contant_new = contant[1].replace('\n','').replace('<br/>','\n')
        fn = './qiubai/' + str(contant[0])
        f = open(fn,'w')
        f.write(contant_new)
        f.close

if __name__ == "__main__":
    sphinx()
