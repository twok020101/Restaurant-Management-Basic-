import mysql

import table_checker as tc
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="1234",
    database="restaurant"
)
conn = mydb.cursor()


def new_customer(token_no, phone_no):
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="1234",
        database="restaurant"
    )
    conn = mydb.cursor()
    x, y = tc.checker()
    flag = False
    if x == True:
        conn.execute("Select Phone_No from customer")
        for ph in conn.fetchall():
            if str(phone_no) == (str(ph[0])):
                flag=True
                try:
                    conn.execute(f"select C_Name from customer where Phone_No={phone_no}")
                except Exception as e:
                    print("baby")

                name=conn.fetchone()
                table_no=y
                try:
                    conn.execute(f"insert into customer_present values ({phone_no},'{name[0]}',{table_no},{token_no})")
                    mydb.commit()
                    try:
                        conn.execute(f"update table_info set vacancy=0 where table_no={table_no}")
                        mydb.commit()
                    except Exception as e:
                        print(e)
                except mysql.connector.IntegrityError:
                    conn.execute(f"select table_no from customer_present where Phone_No={phone_no}")
                    no=conn.fetchone()
                    print(f"Customer is already is sitting in {no[0]}")

        if flag==False:
            name =input("Enter Name: ")
            table_no=y
            if y!=0:
                try:
                    conn.execute(f"insert into customer_present values ({phone_no},'{name}',{table_no},{token_no})")
                    mydb.commit()
                    conn.execute(f"insert into customer values ({phone_no},'{name}')")
                    mydb.commit()
                    conn.execute(f"update table_info set vacancy=0 where table_no={table_no}")
                    mydb.commit()
                except Exception as e:
                    print("baby 1")
                mydb.commit()
    else:
        try:
            conn.execute(f"insert into reception values ({1},{token_no},{phone_no})")
            mydb.commit()
        except Exception as e:
            print(e)
        mydb.commit()







