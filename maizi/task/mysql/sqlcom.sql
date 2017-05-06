创建数据库school
db: school
CREATE DATABASE IF NOT EXISTS school CHARACTER SET = "utf8";
SHOW CREATE DATABASE school;
USE school;



创建表
学生：学号（SNO）、姓名(SNAME)、性别(SSEX)、生日(SBIRTHDAY )、所属班级(CLASS )
CREATE TABLE IF NOT EXISTS student(
SNO INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
SNAME VARCHAR(12),
SSEX ENUM('男','女'),
SBIRTHDAY DATE,
CLASS MEDIUMINT
) ENGINE = InnoDB CHARSET = 'utf8';

课程：课程编号(CNO)、课程名(CNAME)、授课老师(TNO)
CREATE TABLE IF NOT EXISTS course(
CNO TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
CNAME VARCHAR(24),
TNO TINYINT UNSIGNED,
FOREIGN KEY(TNO) REFERENCES teacher(TNO)
) ENGINE = InnoDB CHARSET = 'utf8';

成绩：学号(SNO)、课程编号(CNO)、得分(DEGREE)
CREATE TABLE IF NOT EXISTS record(
SNO INT UNSIGNED,
CNO TINYINT UNSIGNED,
DEGREE TINYINT UNSIGNED,
FOREIGN KEY(SNO) REFERENCES student(SNO),
FOREIGN KEY(CNO) REFERENCES course(CNO)
) ENGINE = InnoDB CHARSET = 'utf8';

老师：教师编号(TNO)、教师姓名(TNAME)、性别(TSSEX)、生日(TBIRTHDAY)、职称(TITLE)、单位科室（DEPART）
CREATE TABLE IF NOT EXISTS teacher(
TNO TINYINT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
TNAME VARCHAR(12),
TSSEX ENUM('男','女'),
TBIRTHDAY DATE,
TITLE VARCHAR(12),
DEPART VARCHAR(12)
) ENGINE = InnoDB CHARSET = 'utf8';



一、每张表使用SQL语句插入至少10条数据。
学生：学号（SNO）、姓名(SNAME)、性别(SSEX)、生日(SBIRTHDAY )、所属班级(CLASS)
INSERT INTO student VALUES
(1,"王菲","女","1970-08-23",900301),
(2,"李亚鹏","男","1980-01-22",900301),
(3,"谢娜","女","1988-03-23",900301),
(4,"章子怡","女","1978-04-13",900301),
(5,"汪涵","男","1987-05-12",900301),
(6,"邓亚萍","女",	"1988-06-11",900302),
(7,"刘翔","男","1991-02-20",900302),
(8,"郭晶晶","女","1988-04-22",900302),
(9,"鲁宾逊","男","1955-04-04",900303),
(10,"黑寡妇","女"	,"1988-04-13",900303),
(11,"小李子","男"	,"1999-01-01",900304);

老师：教师编号(TNO)、教师姓名(TNAME)、性别(TSSEX)、生日(TBIRTHDAY)、职称(TITLE)、单位科室（DEPART）
INSERT INTO teacher VALUES
(1,"胡八一","男","1978-04-22","教师","小科"),
(2,"余罪","男","1980-11-12","教师","小科"),
(3,"邓布利多","男","1958-03-21","校长","老科"),
(4,"苏妲己","女","1970-02-23","校长秘书","女科"),
(5,"朴槿惠","女","1997-09-30","校防卫","政科"),
(6,"金三胖","男",	"1981-09-01","校娱","政科");

课程：课程编号(CNO)、课程名(CNAME)、授课老师(TNO)
INSERT INTO course VALUES
(1,"倒斗",1),
(2,"间谍",2),
(3,"魔法",3),
(4,"魅术",4),
(5,"萨德",5),
(6,"核弹",6);

成绩：学号(SNO)、课程编号(CNO)、得分(DEGREE)
INSERT INTO record SELECT SNO,CNO,round(rand()*100) FROM student,course;



二、完成以下查询题目：
1、 查询Student表中的所有记录的Sname、Ssex和Class列。
	SELECT SNAME,SSEX,CLASS FROM student;
2、 查询教师所有的单位即不重复的Depart列。
	SELECT DEPART,group_concat(TNAME) from teacher GROUP BY DEPART;
3、 查询Student表的所有记录。
	SELECT * FROM student;
4、 查询Score表中成绩在60到80之间的所有记录。
	SELECT * FROM record WHERE DEGREE BETWEEN 60 AND 80;
5、 查询Score表中成绩为85，86或88的记录。
	SELECT * FROM record WHERE DEGREE in (85,86,88);
6、 查询Student表中“95031”班或性别为“女”的同学记录。
	SELECT * FROM student WHERE SSEX = "女" AND CLASS = 900301;
7、 以Class降序查询Student表的所有记录。
	SELECT * FROM student ORDER BY CLASS DESC;
8、 以Cno升序、Degree降序查询Score表的所有记录。
	SELECT * FROM record ORDER BY CNO ASC, DEGREE DESC;
9、 查询“95031”班的学生人数。
	SELECT CLASS,count(*) FROM student WHERE CLASS = 900302;
10、查询Score表中的最高分的学生学号和课程号。
	SELECT * FROM record WHERE DEGREE in (SELECT max(DEGREE) FROM record);
11、查询‘3-105’号课程的平均分。
	SELECT CNO,avg(DEGREE) FROM record WHERE CNO = 3;
12、查询Score表中至少有5名学生选修的并以3开头的课程的平均分数。
	SELECT CNO FROM record WHERE CNO REGEXP '3$' GROUP BY CNO HAVING sum(SNO) > 3;
13、查询所有学生的Sname、Cno和Degree列。
	SELECT student.SNAME,record.CNO,record.DEGREE FROM student join record on student.SNO = record.SNO;
14、查询“95033”班所选课程的平均分。
	SELECT student.CLASS,avg(record.DEGREE) FROM 
	student join record on student.SNO = record.SNO 
	GROUP BY student.CLASS 
	HAVING student.CLASS = 900301;
15、假设使用如下命令建立了一个grade表：
	create table grade(low int,upp int,rank char(1));
	insert into grade values(90,100,"A");
	insert into grade values(80,89,"B");
	insert into grade values(70,79,"C");
	insert into grade values(60,69,"D");
	insert into grade values(0,59,"E");
	commit;
	现查询所有同学的Sno、Cno和rank列。
	SELECT record.SNO,record.CNO,grade.rank FROM record join grade on record.DEGREE BETWEEN grade.low and grade.upp;
16、查询"张旭"教师任课的学生成绩。
	SELECT teacher.TNAME,student.SNAME,record.DEGREE FROM teacher
	JOIN course ON teacher.TNO=course.TNO
	JOIN record ON record.CNO = course.CNO
	JOIN student ON student.SNO = record.SNO
	WHERE teacher.TNAME = "胡八一";
17、查询选修某课程的同学人数多于5人的教师姓名。
	SELECT course.CNO,teacher.TNAME,count(*),group_concat(student.SNAME) FROM teacher
	JOIN course ON teacher.TNO=course.TNO
	JOIN record ON record.CNO = course.CNO
	JOIN student ON student.SNO = record.SNO
	GROUP BY course.CNO
	HAVING count(*) > 5;
18、查询所有教师和同学的Name、Sex和Birthday.
	SELECT SNAME,SSEX,SBIRTHDAY as name FROM student
	UNION ALL
	SELECT TNAME,TSSEX,TBIRTHDAY AS name FROM teacher;
19、查询所有未讲课的教师的Tname和Depart.
	SELECT * FROM teacher LEFT JOIN course ON teacher.TNO=course.TNO WHERE course.CNAME is NULL;
20、查询至少有2名男生的班号。
	SELECT CLASS,group_concat(SNAME) FROM student WHERE SSEX="男" GROUP BY CLASS HAVING count(*)>=2;
21、查询Student表中不姓“王”的同学记录。
	SELECT * FROM student WHERE SNAME REGEXP "^[^李]";
22、查询所有选修“计算机导论”课程的“男”同学的成绩表。
	SELECT student.SNAME,record.DEGREE FROM course 
	join record on course.CNO = record.CNO 
	join student on record.SNO = student.SNO 
	WHERE course.CNAME = "倒斗" AND student.SSEX = "男";
