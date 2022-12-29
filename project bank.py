import mysql.connector
con = mysql.connector.connect(host="localhost" , user ="root" , password = "2004@goushal",database='bank')
mycursor=con.cursor()
con.commit()
while True:
    print("1.create account")
    print("2.deposit or account")
    print("3.loan")
    print("4.display account")
    print("5 exit")
    ch= int(input("enter your choice:"))
    if ch==1:
        acno= input("enter acno:")
        name = input("enter name:")
        city= input("enter city:")
        mobileno = input("enter the mobiel number:")
        balance=input('enter your bank balance:')
        values=(acno,name,city,mobileno,balance)
        a="insert into bank_master(acno,name,city,mobileno,balance) values(%S,%S,%s,%s,%s)" %values
        mycursor.execute(a)
        con.commit()
        print("account is sucessfully created")
    elif ch == 2:
        acno = input("enter acno:")
        dp= input("enter the amount to deposited or withdrawled:")
        dot = input("enter the date of transaction:")
        ttype = input("enter deposited or withdrawled:")
        mycursor.execute("insert into bank_trans(acno,amount,DOT,Ttype) values('{}','{}','{}','{}')").format(acno,dp,dot,ttype)
        con.commit() 
        
        if ttype == "deposited":
            print("money has been deposited sucessfully")
        elif ttype == 'withdrawled':
            print("money has withdrawled sucessfully")
        else:
            print("invalid")
    elif ch ==3:
        acno = input("enter the acno:")
        la=input("enter the loan amount:")
        mycursor.execute("insert into loan_b(acno,loan_amount) values('{}','{}')").format(acno,la)
        con.commit()
        print("loan approval")
    elif ch == 4:
        acno= input("enter acno:")
        mycursor.execute("select * from bank_master where acno="+acno+")")
        for i in mycursor:
            print(i)
        else:
            break
    
        
