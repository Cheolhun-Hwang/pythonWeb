import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()


The_Form = cgi.FieldStorage()
idv = The_Form['id'].value
password = The_Form['password'].value
name = The_Form['name'].value
telephone = The_Form['telephone'].value
address = The_Form['address'].value


cursor.execute("SELECT count(cust_id) from customer_tbl WHERE cust_id = '" + idv + "'")

tbl=[]
tbl = cursor.fetchall()
#rows = cursor.rowcount
idvalue = tbl[0][0]

if idvalue  == 0 :

    connection.commit()
    cursor.execute("INSERT INTO customer_tbl VALUES('" + idv + "','" + password  + "','" + name + "','" + telephone + "','" + address + "','1000','0')")
    print("Content-type : text/html \n")
    print("<html><head><title>python bookstore</title><style>#q{color:blue;} body{margin:auto;width:60%;padding:10px;}</style> </head>")
    print("<body><img src='/img/bookshelf.png'width=40%><h1><p> Thank you for registration<br>")
    print("<span id='q'>"+idv + "</span>  is registrated. </h1><br>")
    print("<a href = '../login.html'><img src='/img/login.png'></a><br>")
    print("</p></body></html>")

    connection.commit()
    connection.close()

else:
    print("Content-type : text/html \n")
    print("<html><head><title>python bookstore</title> <style>#q{color:blue;} body{margin:auto;width:60%;padding:10px;}</style></head>")
    print("<body><img src='/img/bookshelf.png'width=40%><p> ")
    print("<h1><span id='q'>"+idv + "</span> is already existed id or You are already registrated.  </h1> <br>")
    print("<a href = '../registrations.html'> <img src='/img/sign-in.png'></a><br>")
    print("</p></body></html>")

    connection.commit()
    connection.close()
