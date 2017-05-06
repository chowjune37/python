import urllib.request
import re
import pymysql.cursors
import json
from scapy.all import *

print(IP())

# from scapy.all import srp, Ether, ARP  
# IpScan = '192.168.114.1/24'  
# try:  
#     ans,unans = srp(Ether(dst="FF:FF:FF:FF:FF:FF")/ARP(pdst=IpScan), timeout=2)  
# except Exception as e:  
#     print(e)  
# else:  
#     for send, rcv in ans:  
#         ListMACAddr = rcv.sprintf("%Ether.src%---%ARP.psrc%")  
#         print(ListMACAddr) 

# f = open('dj.json','r')
# r = f.read()
# r = json.loads(r)
# f.close()
# y = [(x['Shape'],x['Size'],x['Color'],x['Clarity'],x['Cut'],x['Polish'],x['Sym'],x['Flour'],x['M2'],x['M3'],x['Depth'],x['Table'],x['Ref'],x['ReportNo'],x['Cert'],x['los'],x['Rate'],x['Disc'],x['CertNo'],x['Girdle'],x['Natts'],x['TableInclusion'],x['Milky'],x['EyeClean'],x['Browness'],x['MD5'],x['HH'],x['Rap'],x['pic'],x['video'],x['fast'],x['sys_status']) for x in r]
# print(y[0])

# con = pymysql.connect(host = '52.38.255.237', port = 3306, user = 'root', password = '6JunYan9', db = 'store', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)
# a = 0
# with con.cursor() as f:
# 	sql = 'INSERT INTO ex(Shape,Size,Color,Clarity,Cut,Polish,Sym,Flour,M2,M3,Depth,Tble,Ref,ReportNo,Cert,los,Rate,Disc,CertNo,Girdle,Natts,TableInclusion,Milky,EyeClean,Browness,MD5,HH,Rap,pic,video,fast,sys_status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
# 	sql1 = 'SELECT * FROM ex where Size >= 0.1 and Size <=0.15'
#  	f.execute(sql1)
# 	r = f.fetchall()
# 	print(len(r))
# 	print(r)
# con.commit()
# con.close()

# (x['Shape'],x['Size'],x['Color'],x['Clarity'],x['Cut'],x['Polish'],x['Sym'],x['Flour'],x['M2'],x['M3'],x['Depth'],x['Tble'],x['Ref'],x['ReportNo'],x['Cert'],x['los'],x['Rate'],x['Disc'],x['CertNo'],x['Girdle'],x['Natts'],x['TableInclusion'],x['Milky'],x['EyeClean'],x['Browness'],x['MD5'],x['HH'],x['Rap'],x['pic'],x['video'],x['fast'],x['sys_status'])

# Shape,Size,Color,Clarity,Cut,Polish,Sym,Flour,M2,M3,Depth,Tble,Ref,ReportNo,Cert,los,Rate,Disc,CertNo,Girdle,Natts,TableInclusion,Milky,EyeClean,Browness,MD5,HH,Rap,pic,video,fast,sys_status

