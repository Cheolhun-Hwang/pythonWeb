import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()


The_Form = cgi.FieldStorage()
id_v = The_Form['custid'].value
password_v = The_Form['custpw'].value
b_search = The_Form['search'].value
custname = The_Form['custname'].value

print("Content-type : text/html \n")
print("<html><head><title>Python bookstore</title> ")
print("<style> #title{color:black; text-align:center; font-size:36px;}#name{color:blue;} table { font-size : 13px; color : Maroon; font-weight : bold;margin:0 auto; }table tr td{padding:5px;} img{ width: 200px; height: 300px; }body{margin:0 auto;align:center;text-align:center;}</style></head>")
print("<body>")
cursor.execute("SELECT * from customer_tbl where cust_id = '" + id_v + "' and password = '" + password_v + "'")
nameOfid = []
idOfcount = cursor.fetchall()
custname = idOfcount[0][2]
print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
print("<table id='title'><tr><th><img src='/img/bookshelf.png'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th><th><span id='name'><i>"+custname + "&nbsp;</i></span> 님 안녕하세요,<br>  민준서점에 오신 것을 환영합니다 !!! </h1></th></tr></table>")

print("<h2>MENU&nbsp;&nbsp; >>> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='../login.html'>로그아웃</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='myroom.py?id=" + id_v + "&custname=" + custname+"&password="+password_v+"'>구매내역</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='board-list.py'>독후감</a></h2><br>")
print("<form action='' method= 'POST ' accept-charset='utf-8'><input type='text' name='search'><input type='submit' value='검색'>")
print("<input type = 'hidden' name = 'custid' value = '" + id_v + "'>")
print("<input type = 'hidden' name = 'custname' value = '" + custname + "'>")
print("<input type = 'hidden' name = 'custpw' value = '"+password_v+"'>")
print("</form>")
print("<table >")
        
cursor.execute("SELECT * FROM books_tbl WHERE b_title LIKE '%"+b_search+"%';")
search_tbl=[]
search_tbl = cursor.fetchall()
i = 0 
print("<form  action = 'pointpay.py' method = 'POST'><br>")
print("<input type = 'hidden' name = 'custid' value = '" + id_v + "'>")
print("<input type = 'hidden' name = 'custname' value = '" + custname + "'>")
print("<input type = 'hidden' name = 'custpw' value = '"+password_v+"'>")
for book in search_tbl:
     if i % 3 == 0:
          print("<tr>")
     print("<td><table>")
     print("<tr><td rowspan = '5'><img src = '/"+ book[6]+"'></td><td><h1>"+book[2]+"</h1></td></tr>")
     print("<tr><td>출판사 : " + book[5] + "</td></tr>")
     print("<tr><td>출판일 : " + book[4] + "</td></tr>")
     print("<tr><td>장  르 : " + book[1] + "</td></tr>")
     print("<tr><td><input type = 'checkbox' name = '"+ book[0] + "'></td></tr>")
     print("<tr><td></td><td></td></tr>")
     print("<tr><td></td><td></td></tr>")
     print("</table></td>")
     i +=  1
     if i % 3 == 0:
          print("</tr>")
                
if i % 3 != 0:
     print("</tr>")
          
print("<tr><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;<input type = 'submit' name = 'submit' value = '결제'></td><td></td></tr>")
print("</table>")
print("</form>")
connection.commit()
    
print("</body></html>")


   
connection.close()

