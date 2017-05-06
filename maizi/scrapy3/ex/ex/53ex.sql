CREATE TABLE IF NOT EXISTS ex(
id INT PRIMARY KEY AUTO_INCREMENT,
Shape VARCHAR(12),						# 形状 VARCHAR(12)
Size DECIMAL(4,2),						# 重量 DECIMAL(4,2)
Color CHAR(1),							# 颜色 CHAR(1)
Clarity VARCHAR(6),						# 净度 VARCHAR(6)
Cut VARCHAR(12),						# 切工 VARCHAR(12)
Polish VARCHAR(12),						# 抛光 VARCHAR(12)
Sym VARCHAR(12),						# 对称 VARCHAR(12)
Flour VARCHAR(12),						# 荧光 VARCAHR(12)
M2 DECIMAL(4,2),						# DECIMAL(4,2)
M3 DECIMAL(4,2),						# DECIMAL(4,2)
Depth DECIMAL(4,2),						# 深度 DECIMAL(4,2)
Tble DECIMAL(4,2),						# 台宽 DECIMAL(4,2)
Ref VARCHAR(24),						# 货号 VARCHAR(24)。？？？
ReportNo VARCHAR(24),					# 证书号 VARCHAR(24)
Cert VARCHAR(6),						# 证书类型 VARCHAR(6)
los VARCHAR(12),						# ？？？ VARCHAR(12)
Rate VARCHAR(12),						# ？？？ VARCHAR(12)
Disc VARCHAR(8),						# 扣点 VARCHAR(8)
CertNo VARCHAR(12),						# ？？？ VARCHAR(12)
Girdle VARCHAR(12),						# ？？？ VARCHAR(12)
Natts VARCHAR(12),						# ？？？ VARCHAR(12)
TableInclusion VARCHAR(12),				# ？？？ VARCHAR(12)
Milky VARCHAR(12),						# ？？？ VARCHAR(12)
EyeClean VARCHAR(12),					# ？？？ VARCHAR(12)
Browness VARCHAR(12),					# 咖 VARCHAR(1)
MD5 VARCHAR(50),						# MD5 VARCHAR(50)
HH VARCHAR(24),							# 货号 VARCHAR(24)
Rap VARCHAR(12),						# ？？？ VARCHAR(12)
pic VARCHAR(12),						# 图片 VARCHAR(12)
video VARCHAR(12),						# 视频 VARCHAR(12)
fast VARCHAR(12),						# ？？？ VARCHAR(12)
sys_status VARCHAR(12)					# ？？？ VARCHAR(12)
)ENGINE = InnoDB CHARSET = "utf8";

CREATE TABLE IF NOT EXISTS 53ex(
Shape VARCHAR(12),
Size DECIMAL(4,2),
Color CHAR(1),
Clarity VARCHAR(6),
Cut VARCHAR(12),
Polish VARCHAR(12),
Sym VARCHAR(12),
Flour DECIMAL(3,2),
M2 DECIMAL(3,2),
M3 DECIMAL(3,2),
Depth DECIMAL(4,2),
Tble DECIMAL(4,2),
Ref VARCHAR(24),
ReportNo VARCHAR(24),
Cert VARCHAR(6),
los VARCHAR(12),
Rate VARCHAR(12),
Disc VARCHAR(8),
CertNo VARCHAR(12),
Girdle VARCHAR(12),
Natts VARCHAR(12),
TableInclusion VARCHAR(12),
Milky VARCHAR(12),
EyeClean VARCHAR(12),
Browness VARCHAR(12),
MD5 VARCHAR(50),
HH VARCHAR(24),
Rap VARCHAR(12),
pic VARCHAR(12),
video VARCHAR(12),
fast VARCHAR(12),
sys_status VARCHAR(12)
)ENGINE = InnoDB CHARSET = "utf8";
