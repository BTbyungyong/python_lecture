# Section05-1
# 조건문

print(type(True))
print(type(False))

# ex1
if True:
    print("yes")

# ex2
if False:
    print("no")

# ex3
if False:
    print("no")
else:
    print("yes")

# 관계연산자
# >, >=, <, <=, ==, !=

a = 10
b = 0

print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# falsy : "", [], (), {}, 0, False
# truthy : falsy 제외한 모든 값

city = ""

if city:
    print("True")
else:
    print("False")

# 논리 연산자
# and or not

a = 100
b = 60
c = 15

print("and: ", a > b and b > c)
print("or: ", a > b or c > b)
print("not: ", not a > b)
print(not True)
print(not False)

# 산술, 관계, 논리 연산자
# 산술 > 관계 > 논리 연산자 우선순위
print("ex1: ", 5 + 10 > 0 and not 7 + 3 == 10)

score1 = 90
score2 = "A"

if score1 >= 90 and score2 == "A":
    print("합격")
else:
    print("불합격")

# 다중조건문
num = 90

if num >= 90:
    print("A", num)
elif num >= 80:
    print("B", num)
elif num >= 70:
    print("C", num)
else:
    print("꽝", num)

age = 27
height = 175

if age >= 20:
    if height >= 170:
        print("A지망 지원 가능")
    elif height >= 160:
        print("B지망 지원 가능")
    else:
        print("지원불가")
else:
    print("20세 미만 지원불가")
