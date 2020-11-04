import mysql
import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="1234",
    database="restaurant"
)
conn = mydb.cursor()

def order(table_no):
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="1234",
        database="restaurant"
    )
    conn = mydb.cursor()
    try:
        conn.execute(f"select Phone_No from customer_present where table_no={table_no}")
    except Exception as e:
        print(e)
    phone_no=conn.fetchone()
    conn.execute(f"select Food_name from food")
    avail_list=[]
    for x in conn.fetchall():
        avail_list.append(x[0])
    print(avail_list)
    x=None
    while x!="Done":
        x=input("")
        if(x in avail_list):
            quantity=int(input("Enter quantity"))
            try:
                conn.execute(f"select food_id from food where Food_name='{x}'")
                food_id=conn.fetchone()
                conn.execute(f"insert into current_orders values ({phone_no[0]},{food_id[0]},{quantity})")
                mydb.commit()
            except Exception as e:
                print(e)

