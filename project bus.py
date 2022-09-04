import mysql.connector
try:
    conn = mysql.connector.connect(host='localhost',user='root',passwd='')
    print('connected...')
        
except:
    print('connection failed....')
def init(dbname,conn):
    cur=conn.cursor()
    sql='show databases;'
    cur.execute(sql)
    result=cur.fetchall()
    for row in result:
        if row[0]==dbname:
            print('database found')
            sql = 'use booking'
            cur.execute(sql)
            cur.close()
            break
    else:
        print('database not found..')
        print('creating database')
        sql = 'create database booking;'
        cur.execute(sql)
        sql = 'use booking'
        cur.execute(sql)
        #sql = 'create table  ();'
        #cur.execute(sql)
        sql = 'create table users (userID int unique not null auto_increment primary key ,email varchar(25) unique not null ,bus_name varchar(25) not null,phone_no int not null unique);'
        cur.execute(sql)
        sql = 'create table businfo (bus_name varchar(25) not null unique,busNO int not null unique auto_increment,starting_and_ending varchar(25) not null,starting_time varchar(25) not null);'
        cur.execute(sql)
        print('tables created..')

init('booking',conn)






