# -*- coding: utf-8 -*-

import sqlite3
import cgi
import cgitb
import codecs
import sys


cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())


The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value
var_auth = The_Form['auth'].value

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

if var_auth == "11":
    cursor.execute("SELECT A.name, C.date, B.name, C.salary  FROM EMPLOYEE_TBL A, CODE_TBL B, SALARY_TBL C WHERE A.emp_id = C.emp_id  AND  B.code1 = '0000' AND B.code2 = C.code ORDER BY A.emp_id , C.code ")
else:
    cursor.execute("SELECT A.name, C.date, B.name, C.salary  FROM EMPLOYEE_TBL A, CODE_TBL B, SALARY_TBL C WHERE A.emp_id = C.emp_id  AND  B.code1 = '0000' AND B.code2 = C.code AND A.emp_id = '" + id_v +"' ORDER BY C.code")



salaryOfEmp = []
salaryOfEmp = cursor.fetchall()

print("Content-type : text/html ; charset=utf-8 \n")
print("<html><head><title>Python bookstore</title> ")
print("<style> body{margin:auto;width:60%;padding:10px;} table { font-size : 13px; color : Maroon; font-weight : bold; } fieldset { width : 300 ; }</style></head>")
print("<body><img src='/img/bookshelf.png'width=40%>")
print("<h3><a href='books.py?id="+id_v+"&password="+password_v+"'><input type='button' value='돌아가기'></a></h3>")
print("<h2>급여 내용 입니다.   </h2>")

print("<fieldset>")
for salary in salaryOfEmp :
    print("<pre>"+salary[0]+"  ,  " + salary[1] + "  ,  " + salary[2] + "  ,  " + str(salary[3]) + "</pre>")
print("</fieldset></body>")
print("</html>")
