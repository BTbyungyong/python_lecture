# Section13-1
# 타이핑 게임 제작 및 기본 완성

import random
import time
import winsound  # 사운드 출력 필요 모듈
import sqlite3
import datetime

# DB생성 & Auto Commit
conn = sqlite3.connect("C:/python_basic/resource/records.db", isolation_level=None)

cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS records(\
               id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt INTEGER, record text, regdate text\
)"
)

words = []  # 영어 단어 리스트(1000개)
exec_num = 1  # 게임 실행 횟수
cor_cnt = 0  # 정답 개수

with open("./resource/word.txt", "r") as f:
    for c in f:
        words.append(c.strip())
# print(words) # 단어 리스트 확인

input("Ready? Press Enter Key!")

start = time.time()

while exec_num <= 5:
    random.shuffle(words)
    q = random.choice(words)
    print()
    print("*Question # {}".format(exec_num))
    print(q)  #  문제 출력

    x = input()  # 정답 입력

    print()

    if str(q).strip() == str(x).strip():  # 정답 확인
        print("Pass!")
        # 정답 소리 재생
        winsound.PlaySound("./sound/good.wav", winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Wrong!")
        # 오답 소리 재생
        winsound.PlaySound("./sound/bad.wav", winsound.SND_FILENAME)

    exec_num += 1

end = time.time()

et = end - start
end_time = format(et, ".3f")

if cor_cnt >= 3:
    print("합격")
else:
    print("불합격")

# 기록 DB 삽입
cursor.execute(
    "INSERT INTO records('cor_cnt','record','regdate') VALUES (?,?,?)",
    (cor_cnt, end_time, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
)

print("게임 시간 : ", end_time, "초", "정답 개수 : {}".format(cor_cnt))

if __name__ == "__main__":
    pass
