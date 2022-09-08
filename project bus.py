import mysql.connector
try:
    conn = mysql.connector.connect(host='localhost',user='root',passwd='2004@goushal')
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
        sql = 'create table users (userID int unique not null auto_increment primary key ,email varchar(25) unique not null ,bus_name varchar(25) not null,phone_no int not null unique,fare int not null);'
        cur.execute(sql)
        sql = 'create table businfo (bus_name varchar(25) not null unique,busNO int not null unique auto_increment,starting_and_ending varchar(25) not null,starting_time varchar(25) not null);'
        cur.execute(sql)
        print('tables created..')

init('booking',conn)
def user ():
    cur = conn.cursor()
    print('''             =====================================
             |                                   |
             |       WELCOME TO BOOKMYBUS        |
             |                                   |
             =====================================''')

    print('''list of bus we have:
+-------------------+-------+--------------------------+---------------+------+
| bus_name          | busNO | starting_and_ending      | starting_time | fare |
+-------------------+-------+--------------------------+---------------+------+
|  travels          |     7 | kanchipuram-thoothukudi  | 10pm          |  200 |
| ajith travels     |     4 | kovai-thoothukudi        | 6pm           |  200 |
| naciyar travels   |     1 | chennai-thoothukudi      | 6pm           |  200 |
| shanmugam travels |     2 | kanayakumari-thoothukudi | 7pm           |  200 |
| srm travels       |     6 | salem-thoothukudi        | 9pm           |  200 |
| srs travels       |     5 | thirunalveli-thoothukudi | 7pm           |  200 |       
| sutharam travels  |     8 | dharmapuri-thoothukudi   | 3pm           |  200 |
| vivegam travels   |     3 | madurai-thoothukudi      | 8:30pm        |  200 |
+-------------------+-------+--------------------------+---------------+------+''')
    print('please fill the details' )

    email=input('enter your email:')
    bus=input('enter the bus name you want to book:')
    phone=int(input('enter your phone number:'))
    fare=int(input('enter the fare of bus:'))
    sql= 'insert into users (email,bus_name,phone_no,fare) values("{}","{}",{},{});'.format(email,bus,phone,fare)
    cur.execute(sql)

user()
             






