# -*- coding: utf-8 -*-

import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json






# https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?

train_no=240000G1050H&
from_station_no=01&
to_station_no=10&
seat_types=OM9&
train_date=2017-06-17


# https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?train_no=240000G1050H&from_station_no=01&to_station_no=10&seat_types=OM9&train_date=2017-06-17
