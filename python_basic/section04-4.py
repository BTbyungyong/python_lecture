# Section04-4
# 딕셔너리, 집합

# 딕셔너리(Dictionary) : 순서x,중복x,수정o,삭제o

# Key, Value
# 선언
a = {"name": "Kim", "phone": "000-0000-0000", "birth": "970402"}
b = {0: "hello python", 1: "hello coding"}
c = {"arr": [1, 2, 3]}

print(type(a))

# 출력
print(a["name"])
print(a.get("name"))
print(a.get("address"))
print(c["arr"][1:3])

# 딕셔너리 추가
a["address"] = "seoul"
print(a)
a["rank"] = [1, 2, 4]
a["rank2"] = (1, 2, 3, 4)
print(a)

# keys, values, items
print(a.keys())
print(list(a.keys()))

temp = list(a.keys())
print(temp[1:3])

print(a.values())
print(list(a.values()))

print(a.items())
print(list(a.items()))

print(1 in b)
print("name2" not in a)

# 집합(set) 순서x, 중복x
a = set()
b = set([1, 2, 3, 4])
c = set([1, 2, 3, 4, 5, 6, 6, 6])

print(type(a))
print(c)

t = tuple(b)
print(t)

l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

print(s1.difference(s2))
print(s1 - s2)

# 추가 / 제거
s3 = set([7, 8, 9])

s3.add(18)
s3.add(7)
print(s3)

s3.remove(9)
print(s3)
