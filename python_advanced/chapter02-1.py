# Chapter02-1
# 데이터 모델
# Namedtuple 실습
# 시퀀스(sequence),반복(iterator),함수(function),클래스(class)

# 객체 - 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value
# 파이썬 - 일관성

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.4, 1.5)

from math import sqrt

line_len1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2)

print("ex1-1", line_len1)

# 네임드 튜플
from collections import namedtuple

Point = namedtuple("Point", "x y")

# 두 점 선언
pt1 = Point(1.0, 5.0)
pt2 = Point(2.4, 1.5)

# 계산
line_len2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2)

print("ex1-2", line_len2)
print("ex1-3", line_len1 == line_len2)

# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ["x", "y"])
Point2 = namedtuple("Point", "x,y")
Point3 = namedtuple("Point", "x y")
Point4 = namedtuple("Point", "x y x class", rename=True)  # name으로 사용 못하는 값 런타임에 생성


# 출력
print("ex2-1", Point1, Point2, Point3, Point4)

# 선언
p1 = Point1(x=10, y=35)
p2 = Point2(10, 35)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
# Dict to Unpacking
temp_dict = {"x": 75, "y": 50}
p5 = Point3(**temp_dict)


print("ex2-2", p1, p2, p3, p4, p5)

# 사용
print("ex3-1", p1[0] + p2[1])  # Index Error 주의
print("ex3-2", p1.x + p2.y)

# unpacking
x, y = p3

print("ex3-3", x, y)

# Rename 테스트
print("ex3-4", p4)

# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p6 = Point1._make(temp)
print("ex4-1", p6)

# _fields : 필드 네임 확인
print("ex4-2", p6._fields)

# _asdict() : 정렬된 딕셔너리 반환
print("ex4-3", p1._asdict())
print("ex4-3", dict(p1._asdict()))

# _replace() : 수정된 '새로운' 객체 반환
print("ex4-4", p2._replace(y=100))

# 실사용 실습
# 학생 전체 그룹 생성
# 반20명,4개의 반

# 네임드튜플 선언
Classes = namedtuple("Classes", ["rank", "number"])

# 그룹리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = "A B C D".split()

# 리스트 컴프리헨션
students = [Classes(rank, number) for rank in ranks for number in numbers]
print("ex5-1", students)
print("ex5-2", len(students))

# 가독성x
students2 = [
    Classes(rank, number)
    for rank in "A B C D".split()
    for number in [str(n) for n in range(1, 21)]
]
print("ex6-1", students)
print("ex6-2", len(students))

# 출력
for s in students:
    print("ex7-1", s)
