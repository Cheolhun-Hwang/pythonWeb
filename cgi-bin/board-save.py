import sqlite3
import cgi
import cgitb
import time

cgitb.enable()
connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()

now = time.localtime()

The_Form = cgi.FieldStorage()
var_ttype=The_Form['ttype'].value
id_v = The_Form['id'].value
password_v = The_Form['password'].value

if var_ttype == 'I' :
    var_page = The_Form['page'].value
    var_id = The_Form['iid'].value
    var_title = The_Form['title'].value
    var_content = The_Form['content'].value
    var_date = str(now.tm_year) + "." +str(now.tm_mon) + "." + str(now.tm_mday) 
    cursor.execute("SELECT ifnull(max(id),0) from board_tbl")
    tbl=[]
    tbl = cursor.fetchall()
    cursor.execute("INSERT INTO board_tbl(id,title,content,upload,date) VALUES('" + var_id  + "','" + var_title + "','" + var_content + "',' ','" + var_date + "')")
    connection.commit()
    connection.close()


elif var_ttype == "U" :
    var_page = The_Form['page'].value
    var_id = The_Form['id'].value
    var_title = The_Form['title'].value
    var_content = The_Form['content'].value
    var_num = The_Form['num'].value
    var_date = str(now.tm_year) + "." +str(now.tm_mon) + "." + str(now.tm_mday)  
    cursor.execute("UPDATE board_tbl set content=\""+var_content+"\" , date=\""+var_date+"\"where num=\""+var_num+"\"")
    connection.commit()
    connection.close()
                   
elif var_ttype == "D" :
    var_num = The_Form['num'].value
    var_page = The_Form['page'].value
    cursor.execute("delete from board_tbl where num=" + var_num)
    connection.commit()
    connection.close()





print("Content-type : text/html \n")
print("<html><head><title>python bookstore 게시판</title> ")
print("<meta  http-equiv='refresh' content=\"0;URL='http://localhost:8080/cgi-bin/board-list.py?id=" + id_v + "&password="+password_v+"'\">") 


print("</head>")
print("<body>")

print("</body></html>")

