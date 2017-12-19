# -*- coding: utf-8 -*- 
import codecs
import sys
import sqlite3
import cgi
import cgitb
import time
                 
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value

print("content-type : text/html \n")
print("<!doctype html>")
print("<meta charset='utf-8'>")
print("<html><head><title>게시물보기</title>")
print("""
<style>fieldset {width : 400px;}
pre {  font-size : 14px;
font-family :'Times New Roman'; 	}
#snd { float : right; }
body{margin:0 auto ;
width: 60%;
padding: 10px;}
</style></head>
""")

print("<body><h1><img src='/img/bookshelf.png' width=30%></h1>")
print("<h1>작성하기</h1>")
print("<form action='board-save.py?id=" + id_v + "&password="+password_v+"' method='get'>")
print("<fieldset><input id = 'iid'  type='hidden' name='iid' value = 'MINJUN'>")
print("<input type='hidden' name='ttype' value='I'>")
print("<input type='hidden' name='page' value='1'>")
print("<input type='hidden' name='id' value='"+id_v+"'>")
print("<input type='hidden' name='password' value='"+password_v+"'>")
print("<pre> <label for='nameid'>  작성자 :   </label>  <input id = 'nameid'  type='text' name='nm' value = 'MINJUN'></pre>")              
print("<pre> <label for='titleid'>  제목 :   </label>      <input id = 'titleid'  type='text' name='title' style='width:500px'>     </pre>")
print("<pre>  <textarea id = 'conid'  name='content' cols='80' rows ='20'></textarea></pre>")
print("<pre id = 'snd'>  <a href='board-list.py?id=" + id_v + "&password="+password_v+"'><input type=button value='돌아가기'></a>   <input type='submit' name='send' value='등록' > </pre>")
print("</fieldset></form></body></html>")

