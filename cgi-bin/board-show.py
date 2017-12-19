# -*- coding: utf-8 -*- 
import codecs
import sys

import sqlite3
import cgi
import cgitb
import time
                 
cgitb.enable()
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value
var_id =  The_Form['iid'].value
var_title =  The_Form['title'].value
var_content =  The_Form['content'].value
var_date =  The_Form['date'].value
var_num =  The_Form['num'].value
var_page= The_Form['page'].value

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

print("content-type : text/html \n")
print("<!doctype html>")
print("<meta charset='utf-8'>")
print("<html><head><title>게시물보기</title><style>html { margin: auto;   width: 60%;      padding: 10px;}img {block:inline}</style>")
print("<p><h2>CONTENTS</h2></p></head>")
print("<body> <hr> <p><br>제목 : " +var_title+" </p> <p><br>작성자 : "+var_id+"</p> <p><br>시간 : "+var_date+"</p>")
print("<form action='/cgi-bin/board-save.py' method=\"get\" accept-charset=\"UTF-8\">")
print("<textarea name=\"content\" cols=\"60\" rows=\"20\">"+var_content+"</textarea>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img src='/img/bookshelf.png' width=38%>")
print("<input type=\"hidden\" name=\"ttype\" value=\"U\">")
print("<input type=\"hidden\" name=\"page\" value="+var_page+">")
print("<input type=\"hidden\" name=\"iid\" value="+var_id+">")
print("<input type=\"hidden\" name=\"title\" value="+var_title+">")
print("<input type=\"hidden\" name=\"num\" value="+var_num+">")
print("<input type=\"hidden\" name=\"id\" value="+id_v+">")
print("<input type=\"hidden\" name=\"password\" value="+password_v+">")

print("<br><a href='board-list.py?id=" + id_v + "&password="+password_v+"'><input type='button' value='취소'></a>")

print("<br><br><input type=\"submit\" name=\"send\" value=\"수정\"></pre></form><br>")
print("<form action='/cgi-bin/board-save.py' method=\"get\" accept-charset=\"UTF-8\">")
print("<input type=\"hidden\" name=\"num\" value="+var_num+">")
print("<input type=\"hidden\" name=\"page\" value="+var_page+">")
print("<input type=\"hidden\" name=\"ttype\" value=\"D\">")
print("<input type=\"hidden\" name=\"id\" value="+id_v+">")
print("<input type=\"hidden\" name=\"password\" value="+password_v+">")
print("<input type=\"submit\" name=\"send\" value=\"삭제\"></form>")
print("</body></html>")
