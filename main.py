import sqlite3

con = sqlite3.connect("internship-pi.db")

cursor = con.cursor()
"""
cursor.execute("CREATE TABLE IF NOT EXISTS employee(employeeID INT, firstname TEXT, lastname TEXT, city TEXT, state TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS Payments(employeeID INT, Salarydate TEXT,MonthID	 INT, Value INT)")

cursor.execute("INSERT INTO employee VALUES(10330,'john','John','NY','NY')")
cursor.execute("INSERT INTO employee VALUES(10449,'Sarah','lebat','Melbourne','Bourke')")
cursor.execute("INSERT INTO employee VALUES(11012,'Jon','Dallas','NY','NY')")
cursor.execute("INSERT INTO employee VALUES(11013,'Gheorghe','Honey','NY','NY')")
cursor.execute("INSERT INTO employee VALUES(11014,'Anton','Savar','NY','NY')")

cursor.execute("INSERT INTO Payments VALUES(10330,'June',6,128)")
cursor.execute("INSERT INTO Payments VALUES(10330,'July',7,158)")
cursor.execute("INSERT INTO Payments VALUES(10330,'August',8,133)")
cursor.execute("INSERT INTO Payments VALUES(10330,'September',9,120)")
cursor.execute("INSERT INTO Payments VALUES(10330,'October',10,188)")
cursor.execute("INSERT INTO Payments VALUES(10330,'November',11,160)")
cursor.execute("INSERT INTO Payments VALUES(10330,'December',12,105)")
cursor.execute("INSERT INTO Payments VALUES(10449,'September',9,150)")
cursor.execute("INSERT INTO Payments VALUES(10449,'October',10,158)")
cursor.execute("INSERT INTO Payments VALUES(10449,'November',11,160)")
cursor.execute("INSERT INTO Payments VALUES(10449,'December',12,180)")
"""

cursor.execute("SELECT * FROM  employee WHERE firstname LIKE 'J%'")
n = cursor.fetchall()
print("All employees that have their names starting with the J letter.",n)


cursor.execute("SELECT * from employee")
y = cursor.fetchall()



cursor.execute("SELECT * from Payments")
z = cursor.fetchall()
count = 0
count1 = 0
for veri in z:
    if veri[0] == 10330:
        count += veri[3]

    if veri[0] == 10449:
        count1 += veri[3]
print("\n")
print("name = ",y[0][1])
print("surname = ",y[0][2])
print("total amount = ",count)
print("\n")
print("name = ",y[1][1])
print("surname = ",y[1][2])
print("total amount = ",count1)





con.commit()







