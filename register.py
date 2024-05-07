#!C:\python311\python.exe

import cgi
import mysql.connector
print("Content-type:text/html\r\n\r\n")

print("<html>")
print("<body>")
print("<h1>WELCOME</h1>")
form=cgi.FieldStorage()
fname=form.getvalue("name")
fage=form.getvalue("age")
fgender=form.getvalue("gender")
fphone=form.getvalue("phone")
femail=form.getvalue("email")
fcourse=form.getvalue("course")
fwork=form.getvalue("work")
fexperience=form.getvalue("experience")
farea=form.getvalue("area")

print("<h1>",fname,"</h1>")
print("<h1>",fage,"</h1>")
print("<h1>",fgender,"</h1>")
print("<h1>",fphone,"</h1>")
print("<h1>",femail,"</h1>")
print("<h1>",fcourse,"</h1>")
print("<h1>",fwork,"</h1>")
print("<h1>",fexperience,"</h1>")
print("<h1>",farea,"</h1>")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="zoho" )

mycursor=mydb.cursor();

sql="INSERT INTO apply (NAME,AGE,GENDER,PHONE,EMAIL,COURSE,WORK,EXPERIENCE,AREA) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val=(fname,fage,fgender,fphone,femail,fcourse,fwork,fexperience,farea)

mycursor.execute(sql,val)
mydb.commit()

print("</body>")

print("</html>")
