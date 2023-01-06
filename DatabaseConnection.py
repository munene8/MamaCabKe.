import mysql.connector

mydb = mysql.connector.connect ( host = "local host", user = "Munene", password = "Kel7808mun")
mycursor = mydb.cursor()
connection.execute(''' CREATE TABLE Customers
         (Cust_Id INT PRIMARY KEY     NOT NULL,
         FNAME           TEXT    NOT NULL,
         LNAME           INT     NOT NULL,
         Destination       INT);
         ''')
#populating the database 
mycursor = connect.execute(INSERT INTO Customers Value( "kelvin", "munene" "Nairobi"))
#function for retrieving a record from the database
def Retrieve_a_record():
    x = connect.execute(SELECT FROM Customers WHERE Name= "kelvin")
    print(x)


         
