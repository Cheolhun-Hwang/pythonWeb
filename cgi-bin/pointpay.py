import sqlite3
import datetime
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

d = datetime.date.today()
sumOfpoint = 0
sumOfprice = 0

The_Form = cgi.FieldStorage()
id_v = The_Form['custid'].value
custname_v = The_Form['custname'].value
password_v = The_Form['custpw'].value

print("Content-type : text/html \n")
print("<html><head><title>bookstore</title> ")
print("<style>body{margin:auto;width:60%;padding:10px;}</style></head><body>")
print("<br><img src='/img/bookshelf.png'width=40%><br>The book list which <em>" + custname_v + "</em> buyes now.<br><br> ")
print("<table border='1'>")
print("<tr><th> Title </th><th>Price</th><th>Point</th>")



print("<form  action = 'purchase.py' method = 'POST'><br>")




for att in The_Form.keys():
    if att != "submit" and att != "custid" and att != "custname" and att !="custpw":
        bookOfpurchase = []
        cursor.execute("SELECT * from books_tbl where b_id = '" + att + "'")
        
        
        bookOfpurchase = cursor.fetchall()
        point = int(int(bookOfpurchase[0][7]) * 0.05)
        
        sumOfpoint += point
        sumOfprice += int(bookOfpurchase[0][7])
        

        print("<tr><td width = '200' align = 'middle'>" + bookOfpurchase[0][2] + "</td><td width = '100' align = 'right'>" + str(bookOfpurchase[0][7]) + "</td>")
        print("<td width = '200' align = 'middle'>" + str(point) + "</td></tr>")

        #insert books which customer buys into table
        cursor.execute("insert into purchase_tbl values('" + id_v + "','" + bookOfpurchase[0][0] + "','" + str(d.year)+ "-" +str(d.month) + "-" + str(d.day) + "'," + str(point) + ")")
        connection.commit()                


print("</table>")


print("<br> Total price : " + str(sumOfprice))


points_var = []

cursor.execute("SELECT points, used from customer_tbl where cust_id = '" + id_v + "'")
points_var = cursor.fetchall()


print("<input type = 'hidden' name = 'custid' value = '" + id_v + "'>")
print("<input type = 'hidden' name = 'custname' value = '" + custname_v + "'>")
print("<input type = 'hidden' name = 'sumofprice' value = '" + str(sumOfprice) + "'>")
print("<input type = 'hidden' name = 'point' value = '" + str(points_var[0][0]) + "'>")
print("<input type = 'hidden' name = 'newpoint' value = '" + str(sumOfpoint) + "'>")
print("<input type = 'hidden' name = 'custpw' value = '"+password_v+"'>")


print("<br>"+custname_v+"'s points are " + str(points_var[0][0]) + ". &nbsp;&nbsp;")


print("Will you use your points for payment?  <input type='checkbox' name = 'pointcheck'>")
print("&nbsp;&nbsp;&nbsp;&nbsp;<input type = 'submit' name = 'submit' value = '결제'></td><td></td></tr>")



print("</form>")
print("<form action = 'books.py' method='post'><br>")
print("<input type = 'hidden' name = 'id' value = '" + id_v + "'>")
print("<input type = 'hidden' name = 'password' value = '" + password_v + "'>")
print("<input type = 'submit' name = 'submit' value = '돌아가기'>")
print("</form>")        
        
   
print("</body></html>")

