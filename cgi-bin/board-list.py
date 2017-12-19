import sqlite3
import cgi
import cgitb
import time


cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

now = time.localtime()

The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value

if 'page' in The_Form:
   var_page = The_Form['page'].value
else :
   var_page = 1


var_id = 'MINJUN'
var_date = str(now.tm_year) + "." + str(now.tm_mon) + "." + str(now.tm_mday)

cursor.execute("SELECT * from board_tbl ORDER BY rowid DESC limit 10 offset " + str((int(var_page) - 1) * 10) + ";")
tbl=[]
tbl = cursor.fetchall()

cursor.execute("SELECT count(id) from board_tbl")
countOf = []
countOf = int(cursor.fetchall()[0][0])
numOfpage = 10;
pageNumber = 0;

if countOf % numOfpage != 0:
   pageNumber = int(countOf/numOfpage) + 1
else :
   pageNumber = int(countOf/numOfpage)


print("Content-type : text/html \n")
print("<!DOCTYPE HTML>")
print("<html><head><title>python bookstore 공용 게시판 </title>")
print("<style>")
print("  #f { display : inline-block; width : 200px; }")

print("  #s { display : inline-block; width : 200px; }")
print("  #d { display : inline-block; width : 600px; }")
print("  #th { display : inline-block; width : 200px; } ")
print("body{ margin: 0 auto;    width: 80%; padding: 10px; }")
print("</style> ")
print("</head>")

print("<body><pre>                                                                 <img src='/img/bookshelf.png' width=30%></pre><h3><span id='f'>작성자</span><span id='s'> 제목</span><span id='d'> 내용</span><span id='t'>날짜</span> </h3><hr>")

for tmp in tbl :
   print("<span id='f'>" + var_id + "</span><span id='s'><a href='/cgi-bin/board-show.py?page="+str(var_page)+"&num="+str(tmp[0])+"&iid="+str(tmp[1])+
         "&title="+str(tmp[2])+"&content="+str(tmp[3])+"&date="+str(tmp[5])+"&id=" + id_v + "&password="+password_v+"'>" + str(tmp[2]) + "</a></span><span id='d'>" + str(tmp[3]) + "</span><span id='th'>" + str(tmp[5]) + "</span><br>")
print("<br>")
for i in range(pageNumber):
   if int(var_page) == (i+1):
      print(str(i+1))
   else:
      print("<a href = '/cgi-bin/board-list.py?id=" + id_v + "&password="+password_v+"&page= " + str(i + 1) + "'>" + str(i + 1) + "</a>")

print("<br><pre>                                                                            <a href='books.py?id=" + id_v + "&password="+password_v+"'><img src='/img/previous.png' width=5%'></a>        <a href='board-content.py?id=" + id_v + "&password="+password_v+"'><img src='/img/contract.png' width=5%></a><pre>")

    
print("</body></html>")
connection.commit()
connection.close()
