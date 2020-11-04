import mysql.connector
import Billing
import billing_final
import Order

USERNAME = 'root'
HOSTNAME = 'localhost'
PASSWORD = '1234'
DATABASE = 'restaurant'

db = mysql.connector.connect(user=USERNAME, host=HOSTNAME, passwd=PASSWORD, db=DATABASE)
conn = db.cursor(buffered=True)


def check(b_id):

    try:
        conn.execute('select table_no, vacancy from table_info')
        c = conn.fetchall()

        for i in c:
            if i[1] != 1:
                print('entered')
                conn.execute(f'select C_name from customer_present where table_no={i[0]}')
                C_name = (conn.fetchone())[0]
                print(f"{C_name} is present in table {i[0]}")
                table_no = i[0]
                status,total,order_list = Billing.biller(table_no)

                if status:
                    b_id+=1
                    billing_final.bill(b_id, table_no,total,order_list)
                    print("Thank you pls came again")
                else:
                    Order.order(table_no)
                    return False

            else:
                pass

    except Exception as e:
        print(e)