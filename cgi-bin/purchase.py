import sqlite3
import datetime
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

d = datetime.date.today()
sumOfpoint = 0
newprice = 0

The_Form = cgi.FieldStorage()
custid = The_Form['custid'].value
custname = The_Form['custname'].value
sumofprice = The_Form['sumofprice'].value
point = The_Form['point'].value
newpoint = The_Form['newpoint'].value
password_v = The_Form['custpw'].value

print("Content-type : text/html \n")
print("<html><head><title>Python bookstore</title> ")
print("<style>body{margin:auto;width:60%;padding:10px;} table { font-size : 13px; color : Maroon; font-weight : bold; }</style></head>")
print("<body><br><img src='/img/bookshelf.png'width=40%><br><br>")


    
print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")

newprice = int(sumofprice)
usedpoint = 0
for att in The_Form.keys():
    if att == "pointcheck" :
        newprice = int(sumofprice) - int(point)
        cursor.execute("UPDATE customer_tbl set points = points - " + point + ", used = used + " + point + " where cust_id = '" + custid + "'")
        usedpoint = int(point)
        connection.commit()

cursor.execute("UPDATE customer_tbl set points = points + " + newpoint  + " where cust_id = '" + custid + "'")
connection.commit()

print(" Total price is " + sumofprice)
print(" <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  You used " + str(usedpoint) + "&nbsp; points. <br> ")
print(" &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Payment is completed !!! <br><br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; You paid " + str(newprice))

print("<form action = 'books.py' method='post'><br>")
print("<input type = 'hidden' name = 'id' value = '" + custid + "'>")
print("<input type = 'hidden' name = 'password' value = '" + password_v + "'>")
print("<input type = 'submit' name = 'submit' value = '쇼핑더하기'>")
print("</form>")
    
   
print("</body></html>")


   
connection.close()









