import mysql.connector as mc

mydb = mc.connect(
    host="localhost",
    user="root",
    password="1234",
    database="restaurant"
)

conn = mydb.cursor()


def bill(b_id, table_no, total, order_list):
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="1234",
        database="restaurant"
    )

    conn = mydb.cursor()
    try:
        conn.execute(f"select Phone_No from customer_present where table_no={table_no}")
        phone_no = conn.fetchone()
        conn.execute(f"insert into billing values ({b_id},{phone_no[0]},{total})")
        if order_list != []:
            for id in order_list:
                conn.execute(f"insert into billing_ordered values ({b_id},{id})")
        conn.execute(f"insert into billing_info values ({phone_no[0]},{b_id})")
        conn.execute(f"delete from customer_present where Phone_No={phone_no[0]}")
        conn.execute(f"delete from current_orders where phone_no={phone_no[0]}")
        conn.execute(f"update table_info set vacancy=1 where table_no={table_no}")
        mydb.commit()
    except Exception as e:
        print(e)
