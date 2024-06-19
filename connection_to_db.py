import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="my_application",
    ssl_disabled=True
)
mycursor = mydb.cursor()
sqlFormula = "INSERT INTO items (product_type, gender, age, color, size) VALUES (%s, %s, %s, %s, %s)"
item = ("shirt", "Male", 3.2, "black", "L")
mycursor.execute(sqlFormula, item)
mydb.commit()

# mycursor.execute("CREATE TABLE items (product_id int NOT NULL AUTO_INCREMENT PRIMARY KEY, product_type VARCHAR(255), "
#                  "gender VARCHAR(50) , "
#                  "age INTEGER(10), color VARCHAR(255))")

