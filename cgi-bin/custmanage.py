import sqlite3
import cgi
import cgitb

cgitb.enable()

connection = sqlite3.connect("bookstore.sqlite")
cursor = connection.cursor()



The_Form = cgi.FieldStorage()
id_v = The_Form['id'].value
password_v = The_Form['password'].value
find = The_Form['find'].value


   

print("Content-type : text/html \n")
print("<html><head><title>python bookstore admin </title> <style>body{margin:auto;width:60%;padding:10px;}</style></head>")
print("<body> <img src='/img/bookshelf.png'width=40%><br> <a href='books.py?id="+id_v+"&password="+password_v+"'><input type='button' value='돌아가기'></a> <h2> 판매량 관리 </h2>")



print("<table>")
print("<tr><td></td><td></td><td></td><td></td><td></td>")
print("<tr><td><a href='custmanage.py?id="+id_v+"&password="+password_v+"&find=d'>날짜별 도서별 판매량</a></td><td width='40'></td>")
print("<td><a href='custmanage.py?id="+id_v+"&password="+password_v+"&find=c'>고객별 판매량</a></td><td width='40'></td>")
print("<td><a href='custmanage.py?id="+id_v+"&password="+password_v+"&find=b'>도서별 판매량</a></td></tr></table>")
    
if find == 'd':
        print("<h3> 날짜별 도서별 판매량 </h3>")
        cursor.execute("SELECT a.date, b.b_title, count(a.date) from purchase_tbl a, BOOKS_TBL b where a.b_name = b.b_id group by a.date , a.b_name, b.b_title")
        count = []
        count = cursor.fetchall()

        print("<table border = '1'>")
        print("<tr><th> 날짜 </th><th> 도서명 </th><th> 판매량 </th></tr>")
        
        for howmany in count:
            print("<tr><td width = '100' align = 'middle'>"+howmany[0] + "</td><td width = '200' align = 'left'>" + howmany[1] + "</td><td width = '80' align = 'right'>" + str(howmany[2]) + "</td></tr>")
        print("</table>")
elif find == 'c':
        print("<h3> 고객별 판매량 </h3>")
        cursor.execute("SELECT  b.name, count(b.cust_id) from purchase_tbl a, CUSTOMER_TBL b where a.cust_id = b.cust_id group by b.cust_id, b.name")
        count = []
        count = cursor.fetchall()

        print("<table border = '1'>")
        print("<tr><th > 고객 </th><th> 판매량 </th></tr>")
        
        for howmany in count:
            print("<tr><td width = '150' align = 'left'>"+howmany[0] + "</td><td width = '80' align = 'right'>" + str(howmany[1]) + "</td></tr>")
        print("</table>")
elif find == 'b':
        print("<h3> 도서별 판매량 </h3>")

        cursor.execute("SELECT b.b_title, count(a.b_name) from purchase_tbl a, books_tbl b where a.b_name = b.b_id group by a.b_name, b.b_title")
        count = []
        count = cursor.fetchall()

        print("<table border = '1'>")
        print("<tr><th> 도서명 </th><th> 판매량 </th></tr>")
        
        for howmany in count:
            print("<tr><td width = '200' align = 'left'>"+howmany[0] + "</td><td width = '80' align = 'right'>" + str(howmany[1]) + "</td></tr>")
            
        print("</table>")
        
    


print("</body></html>")










