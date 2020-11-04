import mysql.connector as mc
import New_cust

mydb = mc.connect(
    host="localhost",
    user="root",
    password="1234",
    database="restaurant"
)

conn = mydb.cursor()


def checker():
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="1234",
        database="restaurant"
    )

    conn = mydb.cursor()
    conn.execute(f"select * from reception")
    x = conn.fetchall()
    if x == []:
        pass
    else:
        conn.execute(f"select MIN(token) from reception")
        token = (conn.fetchone())[0]
        conn.execute(f"select Phone_no from reception where token={token}")
        phone_no = (conn.fetchone())[0]
        New_cust.new_customer(token_no=token, phone_no=phone_no)
        conn.execute(f"delete from reception where token={token}")
        mydb.commit()
