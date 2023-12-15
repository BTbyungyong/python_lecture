# Section12-3
# 데이터 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect("C:/python_basic/resource/database.db")

# Cursor 연결
c = conn.cursor()

# 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ("niceman", 2))
# conn.commit()

# 수정2
c.execute(
    "UPDATE users SET username = :name WHERE id = :id", {"name": "goodman", "id": 3}
)
# conn.commit()

# 수정3
c.execute('UPDATE users SET username = "%s" WHERE id = "%s"' % ("badboy", "5"))
# conn.commit()

# 중간 데이터 확인
for user in c.execute("SELECT * FROM users"):
    print(user)

# 삭제1
c.execute("DELETE FROM users WHERE id =?", (2,))
# conn.commit()

# 삭제2
c.execute("DELETE FROM users WHERE id = :id", {"id": "5"})
# conn.commit()

# 삭제3
c.execute("DELETE FROM users WHERE id = '%s'" % 3)
# conn.commit()

# 중간 데이터 확인2
for user in c.execute("SELECT * FROM users"):
    print(user)

# 전체 삭제
print(conn.execute("DELETE FROM users").rowcount)
conn.commit()

conn.close()
