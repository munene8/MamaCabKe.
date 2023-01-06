import mysql.connector

mydb = mysql.connector.connect ( host = "local host", user = "Munene", password = "Kel7808mun")
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, FNAME VARCHAR(255),Lname VARCHAR(255), Location VARCHAR(255), destination VARCHAR (255)"
mycursor.execute( " INSERT INTO Customers VALUE ( "Kelvin", "Munene", "Karatina", "Nairobi" )
mycursor.execute ( "ALTER TABLE Customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


         
