# Section05-2
# 반복문 실습

# 기본 반복문 : for,while

v1 = 1

while v1 < 11:
    print("v1 is", v1)
    v1 += 1

for v2 in range(10):
    print("v2 is", v2)

for v3 in range(1, 11):
    print("v3 is", v3)

# 1 ~ 100 합

sum1 = 0
cnt1 = 1

while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print("1 ~ 100", sum1)
print("1 ~ 100", sum(range(1, 101)))
print("1 ~ 100", sum(range(1, 101, 2)))

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 딕셔너리
# iterable : range, reserved, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Choi", "Yoo"]

for v in names:
    print("You are", v)

word = "dreams"

for s in word:
    print("Word is", s)

my_info = {"name": "Kim", "age": 33, "city": "Seoul"}

# 키
for key in my_info:
    print("my_info", key)

# 키
for key in my_info.keys():
    print("my_info", key)

# 값
for value in my_info.values():
    print("my_info", key)

# 키,값
for key, value in my_info.items():
    print("my_info", key, value)

name = "KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]

for num in numbers:
    if num == 33:
        print("found 33!")
        break
    else:
        print("not found 33..")

# for - else 구문
# for문에 break 작동하지 않은 경우, 마지막 반복 후 else 블럭 실행
for num in numbers:
    if num == 33:
        print("found 33!")
        break
    else:
        print("not found 33..")
else:
    print("not found 33")

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue
    print("타입", type(v))
