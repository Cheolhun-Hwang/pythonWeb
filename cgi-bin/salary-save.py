# -*- coding: utf-8 -*-

import sqlite3
import cgi
import cgitb
import time
import codecs
import sys


cgitb.enable()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value
var_emp_id=The_Form['emp_id'].value
var_code = The_Form['code'].value
var_salary = The_Form['salary'].value



connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

now = time.localtime()

var_date = str(now.tm_year) + "." +str(now.tm_mon) + "." + str(now.tm_mday) 


cursor.execute("INSERT INTO SALARY_TBL VALUES('" + var_emp_id + "','" + var_date  + "','" + var_code + "'," + str(var_salary) + ")")
connection.commit()


connection.close()

print("Content-type : text/html ; charset=utf-8 \n")
print("<html><head><title>python bookstore 게시판</title> ")
print("<meta  http-equiv='refresh' content=\"0;URL='http://localhost:8080/cgi-bin/salary-input.py?id="+id_v+"&password="+password_v+"\">") 
print("</head>")
print("<body>")
print("</body></html>")
