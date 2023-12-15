# Section12-2
# 테이블 조회

import sqlite3

conn = sqlite3.connect("C:/python_basic/resource/database.db")

c = conn.cursor()

c.execute("SELECT * FROM users")

# 커서 위치가 변경
# 1개 로우 선택
# print('one -> \n',c.fetchone())

# 지정 로우 선택
# print('three -> \n',c.fetchmany(size=3))

# 전체 로우 선택
# print('All -> \n',c.fetchall())

# print('All -> \n',c.fetchall())

# 순회1
# rows = c.fetchall()
# for row in rows:
#     print(row)

# 순회2
for row in c.fetchall():
    print(row)

# 순회3
for row in c.execute("SELECT * FROM users ORDER BY id desc"):
    print(row)

# WHERE Retrieve1
param1 = (3,)
c.execute("SELECT * FROM users WHERE id=?", param1)
print("param", c.fetchone())
print("param", c.fetchall())

# WHERE Retrieve2
param2 = 4
c.execute("SELECT * FROM users WHERE id='%s'" % param2)
print("param", c.fetchone())
print("param", c.fetchall())

# WHERE Retrieve3
c.execute("SELECT * FROM users WHERE id=:Id", {"Id": 5})
print("param", c.fetchone())
print("param", c.fetchall())

# WHERE Retrieve4
param4 = (3, 5)
c.execute("SELECT * FROM users WHERE id IN(?,?)", param4)
print("param4", c.fetchall())

# WHERE Retrieve5
c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (3, 1))
print("5", c.fetchall())

# WHERE Retrieve6
c.execute("SELECT * FROM users WHERE id=:id1 OR id=:id2", {"id1": 1, "id2": 2})
print("6", c.fetchall())

# Dump 출력(SQL문)
with conn:
    with open("C:/python_basic/resource/dump.sql", "w") as f:
        for line in conn.iterdump():
            f.write("%s\n" % line)
        print("dump complete")

# f.close(), conn.close()
