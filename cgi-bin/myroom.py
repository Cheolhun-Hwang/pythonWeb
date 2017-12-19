import sqlite3
import datetime
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

d = datetime.date.today()
sumOfpoint = 0

The_Form = cgi.FieldStorage()
custid = The_Form['id'].value
custname = The_Form['custname'].value
password_v = The_Form['password'].value


print("Content-type : text/html \n")
print("<html><head><title>Python bookstore</title> ")
print("<style>body{margin:auto;width:60%;padding:10px;} table  { font-size : 13px;  font-weight : bold; }</style></head>")
print("<body><br><img src='/img/bookshelf.png'width=40%><br><br>")

print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
print("<form action = 'books.py' method='post'><br>")
print("<input type = 'hidden' name = 'id' value = '" + custid + "'>")
print("<input type = 'hidden' name = 'password' value = '" + password_v + "'>")
print("<input type = 'submit' name = 'submit' value = '돌아가기'>")
print("</form>")
print("There are book list which " + custname + " buys until now  <br><br>")



bookOfpurchase = []
cursor.execute("SELECT a.name, b.b_title, c.date, c.point from customer_tbl a, books_tbl b, purchase_tbl c where a.cust_id = '" + custid + "' and a.cust_id = c.cust_id and c.b_name = b.b_id order by c.date")
bookOfpurchase = cursor.fetchall()


print("<table ><tr><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td><td><table border = '1'>")
for book in bookOfpurchase:
    print("<tr><td>" + book[0] + "</td><td>" + book[1] + "</td><td>" + book[2] + "</td><td>" + str(book[3]) + "</td><tr>")
connection.commit()   
print("</table></td></tr></table>")


   
print("</body></html>")


   
connection.close()









