import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
table_info="""
create table student(name varchar(25),class varchar(25),section varchar(25),marks int);
"""
cursor.execute(table_info)
cursor.execute("insert into student values('John','10','A',90)")
cursor.execute("insert into student values('Jane','10','B',85)")
cursor.execute("insert into student values('Jim','10','C',80)")
cursor.execute("insert into student values('Jill','10','D',75)")
cursor.execute("insert into student values('Jack','10','E',70)")
print("The inserted records are")
data=cursor.execute("select * from student")
for row in data:
    print(row)
connection.commit()
connection.close()

