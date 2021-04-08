import mysql.connector as mc
import os
import New_cust
import Order
import Billing
import billing_final
import reception
import checker

mydb = mc.connect(
    host="localhost",
    user="root",
    password="1234",
    database="restaurant"
)

conn=mydb.cursor()
def first_time():
    if os.path.exists("first_time.txt"):
        return True
    else:
        with open("first_time.txt",'w') as file:
            file.write("Login in success")
        file.close()
        return False
def tables():
    no_of_tables=int(input("Enter number of tables: "))
    for i in range(no_of_tables):
        try:
            conn.execute(f"insert into table_info values ({i},1)")
            mydb.commit()
        except Exception as e:
            print(e)
if __name__ == '__main__':
    check=first_time()
    if check==False:
        tables()
    token_no=0
    conn.execute(f"select MAX(billing_id) from billing")
    b_id=(conn.fetchone())[0]
    while True:
        print("1. New customer \n 2.Orders \n 3. Billing \n 4. Show all customers \n 5. End game ")
        x=int(input("Enter choice: "))
        if x==1:
            token_no+=1
            ph=int(input("Enter phone no: "))
            while len(str(ph))!=10:
                print("Unacceptable number")
                ph=int(input("Enter phone no: "))
            New_cust.new_customer(token_no,ph)

        elif x==2:
            y=int(input("Enter table number: "))
            Order.order(y)

        elif x==3:
            b_id+=1
            table_no=int(input("Enter table number:"))
            status,total,order_list=Billing.biller(table_no)
            print(order_list)
            if status==True:
                billing_final.bill(b_id,table_no,total,order_list)
                print("Thank you visit again!")
                reception.checker()

            else:
                print("Please check again!")

        elif x==4:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="1234",
                database="restaurant"
            )
            conn=mydb.cursor()
            try:
                conn.execute(f"select * from customer_present")
                for x in conn.fetchall():
                    print(f"Phone No.={x[0]}, Name={x[1]}, Table No.={x[2]}, Token={x[3]}")
            except Exception as e:
                print(e)
        elif x==5:
            if(checker.check(b_id)): 
                break
        else:
            break
