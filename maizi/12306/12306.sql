-- train_tickets_office
	-- address:		varchar(128)
	-- addressencode:		varchar(128) urldecode gbk2312
	-- agency_name:	varchar(64)
	-- belong_station:	varchar(16)
	-- bureau_code:	char(1)
	-- city:			varchar(16)
	-- city_code:		varchar(16)
	-- county:			varchar(16)
	-- phone_no:		varchar(16)
	-- province:		char(8)
	-- start_time_am:	char(4)
	-- start_time_pm:	char(4)
	-- station_telecode:char(8)
	-- stop_time_am:	char(4)
	-- stop_time_pm:	char(4)
	-- windows_quantity: char(1)
	CREATE TABLE train_tickets_office(	id 				int PRIMARY KEY AUTO_INCREMENT,
										address 		varchar(128),
										addressencode 	varchar(128),
										agency_name 	varchar(64),
										belong_station 	varchar(16),
										bureau_code 	char(1),
										city 			varchar(16),
										city_code 		varchar(16),
										county 			varchar(16),
										phone_no 		varchar(16),
										province 		char(8),
										start_time_am 	char(4),
										start_time_pm 	char(4),
										station_telecode 	char(8),
										stop_time_am 	char(4),
										stop_time_pm 	char(4),
										windows_quantity 	char(1)) charset=utf8;
-- station_information
	-- id:				int PRIMARY KEY AUTO_INCREMENT
	-- admin:			varchar(16)
	-- attribute:		char(8)
	-- station_name:	varchar(16)
	-- station_address:varchar(128)
	-- ride_surrender:	tinyint(1)
	-- luggage:		tinyint(1)
	-- package:		tinyint(1)
	CREATE TABLE station_information(	id 				int PRIMARY KEY AUTO_INCREMENT,
										admin 			varchar(16),
										attribute 		char(8),
										station_name 	varchar(16),
										station_address varchar(128),
										ride_surrender 	tinyint(1),
										luggage 		tinyint(1),
										package 		tinyint(1)) charset = utf8;
-- station_code
	station_suoxie1:varchar(8)
	station_hanzi:	varchar(16)
	station_code:	varchar(8)
	station_pinyin:	varchar(64)
	station_suoxie2:varchar(8)
	station_num:	smallint
-- train_infomation
	arrive_day_diff:
	arrive_day_str:
	arrive_time:
	end_station_name:
	is_start:
	runnung_time:
	service_type:
	start_station_name:
	start_time:
	station_name:
	station_no:
	station_train_code:
	train_class_name:
	wz_num:
-- train_price_information






insert into train_tickets_office(
	address,
	addresscode,
	agency_name,
	belong_station,
	bureau_code,
	city,
	city_code,
	county,
	phone_no,
	province,
	start_time_am,
	start_time_pm,
	station_telecode,
	stop_time_am,
	stop_time_pm,
	windows_quantity) value('西城区安德路22号楼西侧一层', '%CE%F7%B3%C7%C7%F8%B0%B2%B5%C2%C2%B722%BA%C5%C2%A5%CE%F7%B2%E0%D2%BB%B2%E3', '北京迅而达科技发展有限公司', '', 'P', '北京', '0357', '', '--', '北京', '0800', '1200', '', '1200', '1800', '1')