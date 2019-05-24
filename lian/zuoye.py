import pymysql
import settings
import hashlib
import time

conn = pymysql.Connect(**settings.parameters)

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

sql = " create database bbs default charset=utf8"
res =cursor.execute(sql)

#print(res)

conn=pymysql.Connect(cursor=pymysql.cursors.DictCursor)

sql="""
create table if not exists user(uid int primary key auto_increment,
username varchar(30) not null,usertype enum('0','1'),
password char(48) not null, inserDate datetime,email varchar(50))
"""
while True:
    name=input('输入账号')
    if cursor.execute(name):
        print('用户存在')
        break
    else :
        password=print('输入密码')
        email=input('输入邮箱')
        break

password = str(hashlib.sha1(password.encode('utf8')).hexdigest())
datetime = time.strftime('%Y-%m-%d', time.localtime(time.time()))

res=cursor.execute(sql,name,password)
if res>0:
    print('创建成功')
else:
    print('创建失败')

cursor.close()
conn.close()