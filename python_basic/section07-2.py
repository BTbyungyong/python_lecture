# Section07-2
# 상속, 다중상속

# ex1
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메서드 사용 가능
class Car:
    """Parent Class"""

    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return "Car class show"


class BMW(Car):
    """Sub Class"""

    def __init__(self, name, tp, color):
        super().__init__(tp, color)
        self.name = name

    def show_model(self) -> None:
        return "Your car name : %s" % self.name


class Benz(Car):
    """Sub Class"""

    def __init__(self, name, tp, color):
        super().__init__(tp, color)
        self.name = name

    def show_model(self) -> None:
        return "Your car name : %s" % self.name

    def show(self):
        print(super().show())
        return "car info %s %s %s" % (self.name, self.color, self.type)


model1 = BMW("520d", "sedan", "red")
print(model1.color)  # Super
print(model1.type)  # Super
print(model1.name)  # Sub
print(model1.show())  # Super
print(model1.show_model())  # Sub
print(model1.__dict__)

# method overriding
model2 = Benz("220d", "suv", "black")
print(model2.show())

# parent method call
model3 = Benz("350s", "sedan", "silver")
print(model3.show())

# inheritance info
print(BMW.mro())
print(Benz.mro())

# ex2
# 다중 상속
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())
print(A.mro())
