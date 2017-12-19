import sqlite3
import cgi
import cgitb
import codecs
import sys
cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value
cursor.execute("SELECT count(*) from EMPLOYEE_TBL where emp_id = '" + id_v + "' and password = '" + password_v + "'")

numOfEmp = []
numOfEmp = cursor.fetchall()
id_count = numOfEmp[0][0]


if int(id_count)  > 0 :

    cursor.execute("SELECT * from employee_tbl where emp_id = '" + id_v + "' and password = '" + password_v + "'")
    emp_nameOfid = []
    emp_idOfcount = cursor.fetchall()
    empname = emp_idOfcount[0][2]
    print("Content-type : text/html ; charset='utf-8' \n")
    print("<html><head><title>Python bookstore</title> ")
    print("<style>  img{ width: 70%; }table{margin:0 auto;text-align:center;} #blue{color:blue;}  ol li, fieldset legend{font-size:24px;} fieldset{padding-left:220px;padding-right:220px;}</style></head>")
    print("<body><br><br>")
    print("<table><tr><th><img src='/img/bookshelf.png'></th></tr><tr><th><h1><span id='blue'><i>"+empname + "&nbsp;</i></span>&nbsp;관리자님 안녕하세요.<br> 오늘도 좋은 하루 되세요 ~!</h1><h3><a href='../login.html'>로그아웃</a> </h3></th></tr></table>")

    print("<table><tr><td width = '30'></td><td>")
    cursor.execute("SELECT * from EMPLOYEE_TBL where emp_id = '" + id_v + "' and password = '" + password_v + "'")
    employee = []
    employee = cursor.fetchall()
    var_authority = str(employee[0][5])

    print("<fieldset><legend>MENU</legend><ol>")
    print("<li><a href='custmanage.py?id="+id_v+"&password="+password_v+"&find=n'>판매량 관리</a> </li>")
    print("<li><a href='bookmanage.py?id=admin&insert=no'>서적 관리</a> </li>")

    if var_authority == "11":
        print("<li><a href='../emp_registrations.html'>사원 계정 추가</a></li>")
        print("<li><a href='salary-input.py?id="+id_v+"&password="+password_v+"'>급여 입력</a> </li>")
    print("<li><a href='salary-view.py?id=" + id_v + "&password="+password_v+"&auth=" + var_authority+"'>급여 조회</a> </li>")
    print("</ol></fieldset>")

    print("</td><tr></table>")

else:
    cursor.execute("SELECT count(cust_id) from customer_tbl where cust_id = '" + id_v + "' and password = '" + password_v + "'")

    idOfcount = []
    idOfcount = cursor.fetchall()
    id_count = idOfcount[0][0]

    print("Content-type : text/html; charset='utf-8' \n")
    print("<html><head><title>MINJUN bookstore</title> ")
    print("<style> #title{color:black; text-align:center; font-size:36px;}#name{color:blue;} table { font-size : 13px; color : Maroon; font-weight : bold;margin:0 auto; }table tr td{padding:5px;} img{ width: 200px; height: 300px; }body{margin:0 auto;align:center;text-align:center;}</style></head>")

    print("<body>")

    if int(id_count)  == 0 :
         print("Login id doesn't exist. Please confirm one more!!!")
         print("<a href = '../login.html'> Login screen </a>")
    
    else:

         cursor.execute("SELECT * from customer_tbl where cust_id = '" + id_v + "' and password = '" + password_v + "'")
         nameOfid = []
         idOfcount = cursor.fetchall()
         custname = idOfcount[0][2]
         print("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
         print("<table id='title'><tr><th><img src='/img/bookshelf.png'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th><th><span id='name'><i>"+custname + "&nbsp;</i></span> 님 안녕하세요,<br>  민준서점에 오신 것을 환영합니다 !!! </h1></th></tr></table>")
         print("<h2>MENU&nbsp;&nbsp; >>> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='../login.html'>로그아웃</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='myroom.py?id=" + id_v + "&custname=" + custname+"&password="+password_v+"'>구매내역</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a href='board-list.py?id=" + id_v + "&password="+password_v+"'>독후감</a></h2><br>")
         print("<form action='search.py' method= 'get ' accept-charset='utf-8'><input type='text' name='search'><input type='submit' value='검색'>")
         print("<input type = 'hidden' name = 'custid' value = '" + id_v + "'>")
         print("<input type = 'hidden' name = 'custname' value = '" + custname + "'>")
         print("<input type = 'hidden' name = 'custpw' value = '"+password_v+"'>")
         print("</form>")
         
         books_tbl = []
         print("<form  action = 'pointpay.py' method = 'POST'><br>")
         print("<input type = 'hidden' name = 'custid' value = '" + id_v + "'>")
         print("<input type = 'hidden' name = 'custname' value = '" + custname + "'>")
         print("<input type = 'hidden' name = 'custpw' value = '"+password_v+"'>")
         print("<table >")
         
         cursor.execute("SELECT * from books_tbl ")
         bookd_tbl = cursor.fetchall()
         
         i = 0 
         for book in bookd_tbl:
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

