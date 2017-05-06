import requests

params = "input_keyw1=%D0%C2%BD%AD%C4%CF%BB%A8%D4%B0&city=%CE%DE%CE%FD&district=&purpose=%D7%A1%D5%AC&room=&pricemin=&pricemax=&trackLine=&keyword=%D0%C2%BD%AD%C4%CF%BB%A8%D4%B0&renttype=&strCity=%CE%DE%CE%FD&strDistrict=&Strprice=&StrNameKeyword=%D0%C2%BD%AD%C4%CF%BB%A8%D4%B0&houseType=&isnewhouse=0&isFinder=0&fromdianshang=&fromhouseprom=&fromesfchengjiao="
r = requests.get('http://www.douban.com')
print(dir(r))
print(r.cookies)
