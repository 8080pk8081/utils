import sqlite3  as db

print(db.sqlite_version)

# cn = db.connect('mytest.db')
# cur = cn.cursor()
# sql='create table testInfo(id integer primary key AUTOINCREMENT,name varchar(10),age int(2))'
# cur.execute(sql)

class DbSqlite:
    pass



def a_insert(sql):
    cn = db.connect('mytest.db')
    cur = cn.cursor()
    try:
        cur.execute(sql)
        cn.commit()
        print("现在有{}条数据了".format(cur.rowcount))
    except:
        print("运行出错了")
    finally:
        cur.close()
        cn.close()

def b_select(sql):
    cn = db.connect('mytest.db')
    cur = cn.cursor()
    try:
        cur.execute(sql)
        print(cur.fetchall())
        print("现在有{}条数据了".format(cur.rowcount))
    except:
        print("运行出错了")
    finally:
        cur.close()
        cn.close()
name = input("请输入姓名：")
age = int(input("请输入年龄:"))
insertinto_sql="insert into testInfo(name, age) VALUES ('{}',{});".format(name,age)
print("开始执行脚本："+insertinto_sql)
a_insert(insertinto_sql)
# b_select('select * from testInfo;')