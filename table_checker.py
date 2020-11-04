import mysql.connector as mc

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
    conn.execute("select * from table_info")
    for x in conn.fetchall():
        if x[1] == 1:
            return True, x[0]
    return False,0

