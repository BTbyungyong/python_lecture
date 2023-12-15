# Section08-1
# 모듈과 패키지

# 패키지 예제
# 상대경로
# ..: 부모 디렉토리
# .  : 현재 디렉토리

# 사용1 클래스
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1:", Fibonacci.fib2(400))
print("ex1:", Fibonacci().title)

# 사용2 클래스(권장x)
from pkg.fibonacci import *

Fibonacci.fib(500)

print("ex2:", Fibonacci.fib2(600))
print("ex2:", Fibonacci().title)

# 사용3 클래스(as)
from pkg.fibonacci import Fibonacci as fb

fb.fib(1000)

print("ex3:", fb.fib2(1600))
print("ex3:", fb("ex3").title)

# 사용4 함수
import pkg.calculations as c

print("ex4:", c.add(10, 100))
print("ex4:", c.mul(10, 100))
print("ex4:", c.div(10, 100))

# 사용5 함수
from pkg.calculations import div as d

print("ex5:", int(d(4, 2)))

# 사용6
import pkg.prints as p
import builtins

p.prt1()
p.prt2()
print(dir(builtins))

# python 2.xx 는 패키지 디렉토리에 __init__.py 파일을 생성해야 패키지로 인식
