# -*- coding: utf-8 -*-

import sqlite3
import cgi
import cgitb
import codecs
import sys


cgitb.enable()
The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

cursor.execute("SELECT code2, name  FROM CODE_TBL   where code1 = '0000'")


salaryOfEmp = []
salaryOfEmp = cursor.fetchall()


cursor.execute("SELECT emp_id, name  FROM EMPLOYEE_TBL")


employee = []
employee = cursor.fetchall()


print("Content-type : text/html ; charset=utf-8 \n")
print("<html><head><title>Python bookstore</title> ")
print("<style> table { font-size : 13px; color : Maroon; font-weight : bold; } fieldset { width : 300 ; }body{margin:auto;width:60%;padding:10px;}</style></head>")
print("<body><img src='/img/bookshelf.png'width=40%>")
print("<h3><a href='books.py?id="+id_v+"&password="+password_v+"'><input type='button' value='돌아가기'></a></h3>")
print("<h2>급여 입력 화면 입니다.  </h2>")
print("<form action='salary-save.py' method='get'>")
print("<fieldset>")
print("<pre> <label for='nameid'> 직원 이름 :  </label><select id = 'nameid'  name='emp_id' >")
for emp in employee :
    print("<option value='"+emp[0]+"'>"+emp[1]+"</option>")
print("</select></pre>")

print("<pre> <label for='codeid'> 급여 항목 선택  :  </label><select id = 'codeid' name='code'> ")
for salary in salaryOfEmp :
    print("<option value='"+salary[0]+"'>"+salary[1]+"</option>")
print("</select></pre>")

print("<pre> <label for='salaryid'> 금액  :  </label><input id = 'salaryid'  type='text' name='salary'  value = ''></pre>")
print("<pre id = 'snd'>                                          <input type='submit' name='send' value='입력' ></pre>")
print("</fieldset>")
print("<input type = 'hidden' name = 'id' value = '" + id_v + "'>")
print("<input type = 'hidden' name = 'password' value = '"+password_v+"'>")
print("</form>")
print("<hr />")
print("<h2>입력된 내용 </h2>")

cursor.execute("SELECT A.name, C.date, B.name, C.salary  FROM EMPLOYEE_TBL A, CODE_TBL B, SALARY_TBL C WHERE A.emp_id = C.emp_id  AND  B.code1 = '0000' AND B.code2 = C.code ORDER BY A.emp_id , C.code")

salaryOfEmp = []
salaryOfEmp = cursor.fetchall()
for salary in salaryOfEmp :
    print("<pre>"+salary[0]+"  ,  " + salary[1] + "  ,  " + salary[2] + "  ,  " + str(salary[3]) + "</pre>")

print("</body>")
print("</html>")
