# Chapter02-2

# 매직메소드 실습

# 매직메소드 기초 설명
print(int)

print(dir(int))

# 사용
n = 100

print("ex1-1", n + 200, n.__add__(200))
print("ex1-2", n.__doc__)
print("ex1-3", bool(n), n.__bool__())
print("ex1-4", n * 100, n.__mul__(100))

# 클래스 예제1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return "Student {}, {}".format(self._name, self._height)

    def __ge__(self, x):
        print("call ge method")
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x):
        print("call le method")
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        return self._height - x._height


# 인스턴스 생성
s1 = Student("james", 181)
s2 = Student("mie", 187)

# 매직메서드 출력
print("ex2-1", s1 >= s2)
print("ex2-2", s1 <= s2)
print("ex2-3", s1 - s2)
print("ex2-4", s2 - s1)
print("ex2-5", s1)
print("ex2-6", s2)

# 클래스 예제2
class Vector:
    def __init__(self, *args):
        """create a vector, example: v=Vector(1,2)"""
        if len(args) == 0:
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """returns the vector info"""
        return "Vector(%r,%r)" % (self._x, self._y)

    def __add__(self, other):
        """returns the vector addition of self and other"""
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

print("ex3-1", Vector.__init__.__doc__)
print("ex3-2", Vector.__repr__.__doc__)
print("ex3-3", Vector.__add__.__doc__)
print("ex3-4", v1, v2, v3)
print("ex3-5", v1 + v2)
print("ex3-6", v1 * 4)
print("ex3-7", v2 * 10)
print("ex3-8", bool(v1), bool(v2))
print("ex3-9", bool(v3))
