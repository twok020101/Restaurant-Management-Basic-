import mysql.connector as mc


def biller(table_no):
    mydb = mc.connect(
        host="localhost",
        user="root",
        password="1234",
        database="restaurant"
    )
    conn = mydb.cursor(buffered=True)
    order_list = []
    quantity_list = []
    try:
        conn.execute(f"select Phone_no from customer_present where table_no={table_no}")
        phone_no = conn.fetchone()
    except Exception as e:
        print(e)

    try:
        conn.execute(f"select food_id,quantity from current_orders where phone_no={phone_no[0]}")
        for x in conn.fetchall():
            if x[0] in order_list:
                h = order_list.index(x[0])
                pr = quantity_list[h]
                pr += x[1]
                quantity_list[h] = pr
            else:
                order_list.append(x[0])
                quantity_list.append(x[1])
        total = 0
        for food_id in order_list:
            conn.execute(f"select Food_name,price from food where food_id={food_id}")
            for i in conn.fetchall():
                print(f"{i[0]}                {i[1]}")
                x = order_list.index(food_id)
                quantity = quantity_list[x]
                print(f"Quantity: {quantity}")
                total += (i[1] * quantity)
        print(f"Your total bill is {total}")
    except Exception as e:
        print(e)

    while True:
        confirm = int(input("Confirm payment \n 1. Yes \n 2. No"))
        if confirm == 1:
            return True, total, order_list

        elif confirm == 2:
            return False, 0, order_list

        else:
            print("Invalid input")
