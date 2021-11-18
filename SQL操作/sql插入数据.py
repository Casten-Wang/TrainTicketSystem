import pymysql
import random
import os

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='989007', database='trainsystemdatabase', charset='utf8')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 插入车次
sql = "LOAD DATA INFILE 'SQL操作/数据csv/changedTrain.csv' INTO TABLE trainticketdb_traintable"
cursor.execute(sql)

# # 插入座位
# sql = "BULK INSERT SeatTable FROM 'SQL操作/数据csv/SeatTable.csv' WITH(FIELDTERMINATOR = ',',ROWTERMINATOR = '\r\n',FIRE_TRIGGERS)"
# cursor.execute(sql)

db.commit()
# 关闭数据库连接
db.close()
