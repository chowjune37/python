store：
CREATE DATABASE store CHARACTER SET = "utf8";
USE store;

表：代理(proxy)
编码(id)，IP地址(ip)，端口(port)，国家(country)，省份(state)，城市(city)，匿名(alpha)，类型(type)，速度(speed)，连接时间(ctime)，创建时间(created_at)，验证时间(updated_at),生存(live)
CREATE TABLE proxy(
id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
ip INT UNSIGNED,
port SMALLINT UNSIGNED,
country VARCHAR(16),
state VARCHAR(16),
city VARCHAR(16),
alpha TINYINT UNSIGNED,
type VARCHAR(16),
speed FLOAT(4,3),
ctime FLOAT(4,3),
created_at DATETIME,
updated_at DATETIME,
live TINYINT
)ENGINE=InnoDB CHARSET="utf8";


