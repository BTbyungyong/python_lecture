# Chapter03-2
# 해시테이블 - 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복 x
# Set -> 중복 x

# Dict 구조
print("ex1-1")
# print(__builtins__.__dict__)

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print("ex1-2", hash(t1))
# print('ex1-3',hash(t2)) # 에러

# 지능형 딕셔너리
import csv

# 외부 csv to list of tuple
# with open('./resources/test1.csv','r',encoding='UTF-8') as f:
#     temp = csv.reader(f)
#     # Header skip
#     next(temp)
#     # 변환
#     NA_CODES = [tuple(x) for x in temp]

# print('ex2-1')
# print(NA_CODES)

# n_code1 = {country : code for country, code in NA_CODES}
# n_code2 = {country.upper():code for country,code in NA_CODES}

# print('ex2-2')
# print(n_code1)

# print('ex2-3')
# print(n_code2)

# Dict Setdefault 예제
source = (
    ("k1", "v1"),
    ("k1", "v2"),
    ("k2", "v3"),
    ("k2", "v4"),
    ("k2", "v5"),
)

new_dict1 = {}
new_dict2 = {}

# not use setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print("ex3-1", new_dict1)

# use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print("ex3-2", new_dict2)


# 사용자 정의 dict 상속(UserDict 가능)
class UserDict(dict):
    def __missing__(self, key):
        print("__missing__")
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        print("__get__")
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        print("__contains__")
        return key in self.keys() or str(key) in self.keys()


user_dict1 = UserDict(one=1, two=2)
user_dict2 = UserDict({"one": 1, "two": 2})
user_dict3 = UserDict([("one", 1), ("two", 2)])

# 출력
print("ex4-1", user_dict1, user_dict2, user_dict3)
print("ex4-2", user_dict1.get("two"))
print("ex4-3", user_dict1.get("aaa"))
print("ex4-4", "one" in user_dict3)
# print('ex4-5',user_dict1['three']) # 에러
print("ex4-6", "three" in user_dict3)

# immutable dictionary
from types import MappingProxyType

d = {"k1": "test1"}

# readonly
d_frozen = MappingProxyType(d)

print("ex5-1", d, id(d))
print("ex5-2", d_frozen, id(d_frozen))
print("ex5-3", d is d_frozen, d == d_frozen)

# 수정불가
# d_frozen['k1'] = 'test2' # 에러

# Set 구조(FrozenSet)
s1 = {"apple", "orange", "apple", "orange", "kiwi"}
s2 = set(["apple", "orange", "apple", "orange", "kiwi"])
s3 = {}
s4 = set()  # {}은 빈 딕셔너리
s5 = frozenset({"apple", "orange", "apple", "orange", "kiwi"})

# 추가
s1.add("melon")

# frozenset 추가 불가
# s5.add('melon')

print("ex6-1", s1, type(s1))
print("ex6-2", s2, type(s2))
print("ex6-3", s3, type(s3))
print("ex6-4", s4, type(s4))
print("ex6-5", s5, type(s5))

# 선언 최적화
from dis import dis

print("ex6-5")
print(dis("{10}"))

print("ex6-6")
print(dis("set([10])"))

# 지능형 집합
from unicodedata import name

print("ex7-1")
print({name(chr(i), "") for i in range(0, 256)})
