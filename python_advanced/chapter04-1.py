# Chapter04-1
# 일급함수(일급 객체)
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 등에 할당 가능
# 3. 함수에 인수 전달 가능
# 4. 함수 결과로 반환 가능

# 함수 객체 예제
def factorial(n: int):
    """
    Factorial Function
    """
    if n == 1:
        return 1
    return n * factorial(n - 1)


class A:
    pass


print("ex1-1", factorial(5))
print("ex1-2", factorial.__doc__)
print("ex1-3", type(factorial), type(A))
print("ex1-4", set(sorted(dir(factorial))) - set(sorted(dir(A))))
print("ex1-5", factorial.__name__)
print("ex1-5", factorial.__code__)

# 변수 할당
var_func = factorial

print("ex2-1", var_func)
print("ex2-2", var_func(5))
print("ex2-3", map(var_func, range(1, 6)))
print("ex2-3", list(map(var_func, range(1, 6))))

# 함수 인수 전달 및 함수 결과로 반환 - 고위함수
print("ex3-1", list(map(var_func, filter(lambda x: x % 2, range(1, 6)))))
print("ex3-2", [var_func(i) for i in range(1, 6) if i % 2])

# reduce()
from functools import reduce
from operator import add

print("ex3-3", reduce(add, range(1, 11)))  # 누적
print("ex3-4", sum(range(1, 11)))

# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 기명 함수 사용
# 일반 함수 형태로 리팩토링 권장
print("ex3-5", reduce(lambda x, t: x + t, range(1, 11)))

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
import random

# 로또 추첨 클래스
class Lotto:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):
        return self.pick()


# 객체 생성
lotto = Lotto()

# 호출 가능 확인
print(
    "ex4-1",
    callable(str),
    callable(list),
    callable(factorial),
    callable(3.14),
    callable(lotto),
)

# 로또 추첨
print("ex4-2", lotto.pick())
print("ex4-3", lotto())

# 다양한 매개변수 입력(*args,**kwargs)
def args_test(name, *args, point=None, **kwargs):
    return "<args_test> {} {} {} {}".format(name, args, point, kwargs)


print("ex5-1", args_test("test1"))
print("ex5-2", args_test("test1", "test2"))
print("ex5-3", args_test("test1", "test2", "test3", id="admin"))
print("ex5-4", args_test("test1", "test2", "test3", id="admin", point=7))
print(
    "ex5-5", args_test("test1", "test2", "test3", id="admin", point=7, password="1234")
)

# 함수 Signatures
from inspect import signature

sg = signature(args_test)

print("ex6-1", sg)
print("ex6-1", sg.parameters)

# 모든 정보 출력
for name, param in sg.parameters.items():
    print("ex6-3", name, param.kind, param.default)

# partial 사용법 : 인수 고정 -> 주로 특정 인수 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된 함수의 새 버전 반환
# 함수의 새 객체 타입은 이전 함수의 자체를 기술
from operator import mul
from functools import partial

print("ex7-1", mul(10, 100))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print("ex7-2", five(1000))
print("ex7-3", six())
print("ex7-4", [five(i) for i in range(1, 11)])
print("ex7-4", list(map(five, range(1, 11))))
