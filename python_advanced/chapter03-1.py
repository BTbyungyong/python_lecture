# Chapter03-1
# 시퀀스 형
# container : 서로 다른 자료형 저장 list, tuple, collections.depue
# flat : 한 개의 자료형 str, bytes, bytearray, array.array, memoryview
# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, ste, bytes

# 지능형 리스트(Comprehending Lists)
chars = "!@#$%^&*()_+"
codes1 = []

# Non comprehending list
for s in chars:
    codes1.append(ord(s))

# comprehending list
codes2 = [ord(s) for s in chars]

# comprehending list
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40]

# comprehending list + map,filter
codes4 = list(filter(lambda x: x > 40, map(ord, chars)))


print("ex1-1", codes1)
print("ex1-2", codes2)
print("ex1-3", codes3)
print("ex1-4", codes4)
print("ex1-5", [chr(s) for s in codes1])
print("ex1-6", [chr(s) for s in codes2])
print("ex1-7", [chr(s) for s in codes3])
print("ex1-8", [chr(s) for s in codes4])

# Generator
import array

# Generator : 한번에 한개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)

# Array(자료형 타입,)
array_g = array.array("I", (ord(s) for s in chars))

print("ex2-1", tuple_g)
print("ex2-2", next(tuple_g))
print("ex2-3", next(tuple_g))
print("ex2-4", array_g)
print("ex2-5", array_g.tolist())

# 제네레이터 예제
print("ex3-1", ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)))

for s in ("%s" % c + str(n) for c in ["A", "B", "C", "D"] for n in range(1, 21)):
    print("ex3-2", s)

# 리스트 사용 시 주의할 점
marks1 = [["~"] * 3 for n in range(3)]
marks2 = [["~"] * 3] * 3

print("ex4-1", marks1)
print("ex4-2", marks2)

marks1[0][1] = "x"
marks2[0][1] = "x"

print("ex4-3", marks1)
print("ex4-4", marks2)

# 증명
print("ex4-5", [id(i) for i in marks1])
print("ex4-6", [id(i) for i in marks2])

# Tuple
# Packing & Unpacking
print("ex5-1", divmod(100, 9))
print("ex5-2", divmod(*(100, 9)))
print("ex5-3", *(divmod(100, 9)))

x, y, *rest = range(10)
print("ex5-4", x, y, rest)

x, y, *rest = range(2)
print("ex5-5", x, y, rest)

x, y, *rest = 1, 2, 3, 4, 5
print("ex5-5", x, y, rest)

# Mutable(가변) vs Immutable(불변)
l = (10, 15, 20)
m = [10, 15, 20]

print("ex6-1", l, m, id(l), id(m))

l = l * 2
m = m * 2

print("ex6-2", l, m, id(l), id(m))

l *= 2
m *= 2

print("ex6-2", l, m, id(l), id(m))

# sort vs sorted
# opt : reverse, key=len, key=str.lower, key=func
f_list = ["orange", "apple", "mango", "papaya", "lemon", "strawberry", "coconut"]

# sorted : 정렬 후 '새로운' 객체 반환
print("ex7-1", sorted(f_list))
print("ex7-2", sorted(f_list, reverse=True))
print("ex7-3", sorted(f_list, key=len))  # 길이 순서
print("ex7-4", sorted(f_list, key=lambda x: x[-1]))
print("ex7-5", sorted(f_list, key=lambda x: x[-1], reverse=True))

print("ex7-6", f_list)

# sort : 원본 객체 직접 변경
# 별도 반환 값 없음 None
print("ex7-7", f_list.sort(), f_list)
print("ex7-8", f_list.sort(reverse=True), f_list)
print("ex7-9", f_list.sort(key=len), f_list)
print("ex7-10", f_list.sort(key=lambda x: x[-1]), f_list)
print("ex7-11", f_list.sort(key=lambda x: x[-1], reverse=True), f_list)
