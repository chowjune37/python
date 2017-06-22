# -*- coding: utf-8 -*-

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
import time
import MySQLdb

def fetch_train_info():
	url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo'
	train_no="240000G1010C"
	from_station_telecode="VNP"
	to_station_telecode="AOH"
	depart_date="2017-06-16"
	params="train_no=" + train_no + "&from_station_telecode=" + from_station_telecode + \
	"&to_station_telecode=" + to_station_telecode + "&depart_date=" + depart_date
	train_info = requests.get(url,params=params,verify=False)
	return(json.loads(train_info.text)['data']['data'])

def fetch_station_code():
	station_name_url = requests.get('https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9015',verify=False)
	station_name = [i.split('|') for i in station_name_url.content.decode('utf8').split("\'")[1].split('@')[1:]]
	return(station_name)

def fetch_train_name():
	params={}
	params['date']='2017-06-17'
	request = requests.get('https://kyfw.12306.cn/otn/queryTrainInfo/getTrainName',params=params,verify=False)
	return(json.loads(request.content.decode('utf8'))['data'])

def fetch_sale_info():
	pro_url = requests.get('https://kyfw.12306.cn/otn/userCommon/allProvince',verify=False)
	pro_names = json.loads(pro_url.content.decode('utf8'))['data']
	params={'province':'','city':'','county':''}
	sale_infos=[]
	for pro_name in pro_names[1:2]:
		params['province']=pro_name['chineseName']
		sale_st_url = requests.get('https://kyfw.12306.cn/otn/queryAgencySellTicket/query',params=params,verify=False)
		sale_st_info = json.loads(sale_st_url.content.decode('utf8'))['data']['datas']
		sale_infos.extend(sale_st_info)
		print(pro_name['chineseName'])
		time.sleep(2)
	return sale_infos

def fetch_station_information():
	html = requests.get("http://www.12306.cn/mormhweb/kyyyz/")
	soup = BeautifulSoup(html.content,'lxml')
	st_names = soup.select('#secTable > tbody > tr > td')
	station_admin_ = [st_name.string for st_name in st_names]
	station_admin = []
	for i in station_admin_:
		station_admin.append(i)
		station_admin.append(i)
	st_urls = soup.select('.submenu_bg > a')
	stations = []
	for (st_url,st_admin) in zip(st_urls,station_admin):
		st_html = requests.get(urljoin('http://www.12306.cn/mormhweb/kyyyz/',st_url.get('href')))
		st_attribute = st_url.get('title')
		st_infos = BeautifulSoup(st_html.content,'lxml').select('.tb tr')
		for st_info in st_infos[2:]:
			st_info_text = st_info.select('td')
			r = 1 if st_info_text[2].string=='√' else 0
			l = 1 if st_info_text[3].string=='√' else 0
			p = 1 if st_info_text[4].string=='√' else 0
			stations.append({	'admin':st_admin,
								'atribute':st_attribute,
								'station_name':st_info_text[0].string,
								'station_address':st_info_text[1].string,
								'ride_surrender':r,
								'luggage':l,
								'package':p})
	return(stations)

def tolist(key,values):
	b = []
	for v in values:
		a = []
		for k in key:
			if(k in v):
				a.append(v[k])
			else:
				a.append('')
		b.append(a)
	return b

def login_sql():
	con = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='6junechow9',db='test',charset='utf8')
	cur = con.cursor()
	return con,cur

def logout_sql(con,cur):
	cur.close()
	con.close()

def insert_sql(table_name,key,values):
	con,cur = login_sql()
	sql = 'insert into ' + table_name + '(' + ','.join(key) + ') values(' + ((len(key)*'%s,').rstrip(',')) + ')'
	print(sql)
	cur.executemany(sql,values)
	con.commit();
	logout_sql(con,cur)

if __name__ == '__main__':
	# sale_infos=fetch_sale_info()
	# sale_infos_key = ['address','addressencode','agency_name','belong_station','bureau_code','city','city_code','county',
	# 'phone_no','province','start_time_am','start_time_pm','station_telecode','stop_time_am','stop_time_pm',
	# 'windows_quantity']
	# sale_infos_ = tolist(sale_infos_key,sale_infos)
	# sale_infos_key[1] = 'addresscode'
	# insert_sql('train_tickets_office',sale_infos_key,sale_infos_)
	# print(len(sale_infos))

	# stations = fetch_station_information()
	# station_information_key = ['admin','attribute','station_name','station_address','ride_surrender','luggage','package']
	# stations_ = tolist(station_information_key,stations)
	# insert_sql('station_information',station_information_key,stations_)
	# print(len(stations_))