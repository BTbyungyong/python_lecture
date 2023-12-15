# Section10-1
# 예외처리

# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드스타일, 문법체크

# SyntaxError : 잘못된 문법

# print('test)


# NameError : 참조변수 없음

a = 10
b = 15
# print(c)


# ZeroDivisionError : 0 나누기 에러

# print(10/0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
# print(x[3])


# KeyError

dic = {"name": "Kim", "age": 33, "city": "Seoul"}
# print(dic['hobby'])
print(dic.get("hobby"))


# AttributeError : 모듈, 클래스에 없는 잘못된 속성 사용 시

import time

print(time.time())
# print(time.month())


# ValueError : 참조 값이 없을 때

x = [1, 5, 9]
# x.remove(10)
# x.index(10)


# FileNotFoundError

# f = open('test.txt','r')


# TypeError
x = [1, 2]
y = (1, 2)
z = "test"
# print(x+y)
# print(x+z)


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외처리 코딩 권장(EAFP 코딩스타일)

# 예외 처리 기본
# try: 에러가 발생할 가능성이 있는 코드 실행
# except: 에러명
# else: 에러가 발생하지 않았을 경우 실행
# finally: 항상 실행

# ex1
name = ["Kim", "Lee", "Park"]

try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! {} in name".format(z, x + 1))
except ValueError:
    print("Not Found It. - Value Error")
else:
    print("else block running")

# ex2
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! {} in name".format(z, x + 1))
except:
    print("Not Found It. - Error")
else:
    print("else block running")

# ex3
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! {} in name".format(z, x + 1))
except:
    print("Not Found It. - Error")
else:
    print("else block running")
finally:
    print("finally")

# ex4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴
try:
    print("try")
finally:
    print("finally")

# ex5
try:
    z = "Kim"
    x = name.index(z)
    print("{} Found it! {} in name".format(z, x + 1))
except IndexError as e:
    print(e)
except ValueError:
    print("Not Found It. - ValueError")
except:
    print("Not Found It. - Error")
else:
    print("else block running")
finally:
    print("finally")

# ex6
# 예외 발생 시키기 : raise
try:
    a = "Kim"
    if a == "Kim":
        print("ok")
    else:
        raise ValueError
except ValueError:
    print("not kim")
except Exception as e:
    print(e)
