import pymssql


def init_sql():
    db = pymssql.connect(host='127.0.0.1', port='3306', user='root', password='989007', database='trainsystemdatabase', charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # -------------------------建表---------------------------------
    # --------------------------------------------------------------
    # --------------------------------------------------------------

    # 如果数据表存在使用execute()方法删除表
    cursor.execute("DROP TABLE IF EXISTS Buy")
    cursor.execute("DROP TABLE IF EXISTS BankTable")
    cursor.execute("DROP TABLE IF EXISTS Users")
    cursor.execute("DROP TABLE IF EXISTS SeatTable")
    cursor.execute("DROP TABLE IF EXISTS TrainTable")
    cursor.execute("DROP TABLE IF EXISTS Administrator")

    # 创建用户数据表
    sql = """CREATE TABLE Users (
        id INT identity,
        UserID VARCHAR(10) NOT NULL PRIMARY KEY DEFAULT ('x'),
        UserName VARCHAR(20) NOT NULL,
        AGE INT NOT NULL,
        SEX NVARCHAR(2) NOT NULL,
        Password VARCHAR(20) NOT NULL,
        IDcard VARCHAR(20) NOT NULL)"""
    cursor.execute(sql)

    # 创建管理员数据表
    sql = """CREATE TABLE Administrator (
        id INT identity,
        AID VARCHAR(10) NOT NULL PRIMARY KEY DEFAULT ('x'),
        AName VARCHAR(20) NOT NULL,
        AGE INT NOT NULL,
        SEX NVARCHAR(2) NOT NULL,
        Password VARCHAR(20) NOT NULL,
        IDcard VARCHAR(20) NOT NULL)"""
    cursor.execute(sql)

    # 创建银行卡数据表
    sql = """CREATE TABLE BankTable (
        BankCard VARCHAR(20) NOT NULL PRIMARY KEY,
        Balance INT NOT NULL,
        UserID VARCHAR(10) NOT NULL,
        foreign key (UserID) REFERENCES Users(UserID))"""
    cursor.execute(sql)

    # 创建座位数据表
    sql = """CREATE TABLE SeatTable (
        SeatID VARCHAR(20) NOT NULL PRIMARY KEY DEFAULT ('x'),
        Carriage VARCHAR(10) NOT NULL,
        Seat VARCHAR(10) NOT NULL)"""
    cursor.execute(sql)

    # 创建车次数据表
    sql = """CREATE TABLE TrainTable (
        Train VARCHAR(10) NOT NULL,
        MaxPeople INT NOT NULL,
        BeginTime DATETIME NOT NULL,
        EndTime DATETIME NOT NULL,
        Origin NVARCHAR(10) NOT NULL,
        Destination NVARCHAR(10) NOT NULL,
        Price INT NOT NULL,
        AID VARCHAR(10) NOT NULL,
        PRIMARY KEY (Train,BeginTime,EndTime),
        foreign key (AID) REFERENCES Administrator(AID),
    )"""
    cursor.execute(sql)

    # 创建购买表
    sql = """CREATE TABLE Buy (
        SeatID VARCHAR(20) NOT NULL,
        UserID VARCHAR(10) NOT NULL,
        Train VARCHAR(10) NOT NULL,
        BeginTime DATETIME NOT NULL,
        EndTime DATETIME NOT NULL,
        Ticket VARCHAR(30) NOT NULL DEFAULT ('x'),
        BuyTime DATETIME NOT NULL,
        PRIMARY KEY (SeatID,Train,BeginTime,EndTime),
        foreign key (UserID) REFERENCES Users(UserID),
        foreign key (SeatID) REFERENCES SeatTable(SeatID),
        foreign key (Train,BeginTime,EndTime) REFERENCES TrainTable(Train,BeginTime,EndTime))"""
    cursor.execute(sql)

    # -------------------------建立触发器----------------------------
    # --------------------------------------------------------------
    # --------------------------------------------------------------

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS tri_Users_ins")

    # 创建触发器 tri_Users_ins 给用户id编号
    sql = """
    create trigger tri_Users_ins
    on Users after insert
    as
    begin
        update Users set UserID = 'U' + right('0000'+ltrim(id),4)
        where id in (select id from inserted)
    end
    """
    cursor.execute(sql)

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS tri_Administrator_ins")

    # 创建触发器 tri_Administrator_ins 给管理员id编号
    sql = """
    create trigger tri_Administrator_ins
    on Administrator after insert
    as
    begin
        update Administrator set AID = 'A' + right('0000'+ltrim(id),4)
        where id in (select id from inserted)
    end
    """
    cursor.execute(sql)

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS tri_Users_changeAge")

    # 创建触发器 在用户表里根据身份证改变用户年龄
    sql = """
    create trigger tri_Users_changeAge
    on Users after insert
    as
    begin
        UPDATE Users
        SET AGE=FLOOR(DATEDIFF(DY, substring(IDcard,7,4), GETDATE()) / 365.25)
    end
    """
    cursor.execute(sql)

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS tri_Administrator_changeAge")

    # 创建触发器,在管理员表里根据身份证改变管理员年龄
    sql = """
    create trigger tri_Administrator_changeAge
    on Administrator after insert
    as
    begin
        UPDATE Administrator
        SET AGE=FLOOR(DATEDIFF(DY, substring(IDcard,7,4), GETDATE()) / 365.25)
    end
    """
    cursor.execute(sql)

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS tri_SeatTable_ins")

    # 创建触发器 SeatTable_ins 给座位编号
    sql = """
    create trigger tri_SeatTable_ins
    on SeatTable after insert
    as
    begin
        update SeatTable set SeatID = Carriage + Seat
        where Carriage in (select Carriage from inserted) AND Seat in (select Seat from inserted)
    end
    """
    cursor.execute(sql)

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS tri_Buy_ins")

    # 创建触发器,生成车票编号
    sql = """
    create trigger tri_Buy_ins
    on Buy after insert
    as
    begin
        update Buy set Ticket = UserID + '-' + Train + '-' + SeatID
        select UserID,Train,SeatID from inserted
    end
    """
    cursor.execute(sql)

    # 如果触发器存在删除触发器
    cursor.execute("DROP trigger IF EXISTS after_insert_buy")

    # 创建触发器,修改余额
    sql = """
    CREATE TRIGGER after_insert_buy
    On Buy after insert
    AS
    Begin
        UPDATE BankTable
        SET Balance = Balance - (
            SELECT Price FROM TrainTable WHERE Train = 
            (SELECT Train FROM inserted) 
            AND BeginTime = (SELECT BeginTime FROM inserted) 
            AND EndTime = (SELECT EndTime FROM inserted))
    END
    """
    cursor.execute(sql)

    db.commit()
    # 关闭数据库连接
    db.close()
    print(">>>>>>>>>>>>>")
