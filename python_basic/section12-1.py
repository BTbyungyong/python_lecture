# Section12-1
# 데이터베이스 연동
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print(now)

nowDatetime = now.strftime("%Y-%m-%d %H:%M:%S")
print(nowDatetime)

print("sqlite3.version", sqlite3.version)
print("sqlite3.sqlite_version", sqlite3.sqlite_version)

# DB 생성 및 Auto Commit - Rollback
conn = sqlite3.connect("C:/python_basic/resource/database.db", isolation_level=None)

# cursor
c = conn.cursor()
print(type(c))

# 테이블 생성(Data type:text,numeric,integer,real,blob)
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,username text, \
          email text,phone text, website text, regdate text)"
)

# 데이터 삽입
# 변수 삽입 시 해당 데이터 자리에 ? 입력 후 두번째 인자로 해당 변수 튜플로 전달
# c.execute('INSERT INTO users VALUES(1,"Kim","kim@naver.com","000-0000-0000","kim.com",?)',(nowDatetime,))
# c.execute("INSERT INTO users(id,username,email,phone,website,regdate) VALUES (?,?,?,?,?,?)",(2,'Park','park@daum.net','010-0000-0000','park.com',nowDatetime))

# Many 삽입(튜플,리스트)
userList = (
    (3, "lee", "lee@daum.net", "010-0000-0000", "lee.com", nowDatetime),
    (4, "cho", "cho@daum.net", "010-0000-0000", "cho.com", nowDatetime),
    (5, "choi", "choi@daum.net", "010-0000-0000", "choi.com", nowDatetime),
)

# c.executemany("INSERT INTO users(id,username,email,phone,website,regdate) VALUES (?,?,?,?,?,?)",userList)

# 테이블 데이터 삭제
# conn.execute("DELETE FROM users")
# print('user db deleted',conn.execute("DELETE FROM users").rowcount)

# commit : isolation_level=None일 경우 자동 반영(auto commit)
# conn.commit()

# rollback
# conn.rollback()

# 접속해제
conn.close()
