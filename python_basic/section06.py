# Section06
# 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# ex1
def hello(world):
    print("hello", world)


hello("world")
hello("python")

# ex2
def hello_return(world):
    val = "hello " + str(world)
    return val


word = hello_return("python!!")
print(word)

# ex3
# 다중 반환 함수
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3


x1, x2, x3 = func_mul(2)
print(x1, x2, x3)

# ex4
# 데이터타입 반환
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


lt = func_mul(2)
print(lt, type(lt))

# ex5
# *args, **kwargs
def args_func(*args):
    print(args)
    print(type(args))  # 튜플
    for t in args:
        print(t)
    for i, v in enumerate(args):  # 인덱스 생성
        print(i, v)


args_func("kim")
args_func("kim", "lee")
args_func("kim", "lee", "choi")


def kwargs_func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)


kwargs_func(name1="kim", name2="park", name3="lee")
kwargs_func(name1="kim", name2="park")
kwargs_func(name1="kim")


def ex_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)


ex_mul(10, 20)
ex_mul(10, 20, "park", "kim")
ex_mul(10, 20, "park", "kim", age1=23, age2=43)

# ex6
# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print("inner func", num)

    print("outer func")
    func_in_func(num + 10000)


nested_func(10000)

# ex6
# 타입 힌트
def func_mul(x: int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]


print(func_mul(3))

# lambda
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)
print(type(var_func))

print(var_func(10))

lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10(10))


def func_final(x, y, func):
    print(x * y * func(10))


func_final(10, 10, lambda_mul_10)
func_final(10, 10, lambda x: x * 1000)
