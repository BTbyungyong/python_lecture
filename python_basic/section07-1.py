# SEction07-1
# 파이썬 클래스 상세 이해
# self, class, instance 변수

# 클래스, 인스턴스 차이 중요
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용

# 선언
# class 클래스명:
#     함수

# ex1
class UserInfo:
    # 속성, 메서드
    def __init__(self, name):
        print("초기화", name)
        self.name = name

    def user_info_p(self):
        print("Name:", self.name)


user1 = UserInfo("Kim")
user1.user_info_p()

user2 = UserInfo("Park")
user2.user_info_p()

print(id(user1))
print(id(user2))
# 각각의 네임스페이스 사용
print(user1.__dict__)
print(user2.__dict__)

# ex2
# self
class SelfTest:
    def func1():
        print("func1 called")

    def func2(self):
        print(id(self))
        print("func2 called")


self_test = SelfTest()

# self_test.func1()
SelfTest.func1()

self_test.func2()
print(id(self_test))

SelfTest.func2(self_test)

# ex3
# 클래스 변수, 인스턴스 변수
class WareHouse:
    # 클래스 변수
    stock_num = 0

    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1

    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse("Kim")
user2 = WareHouse("Park")
user3 = WareHouse("Lee")

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
print(user2.stock_num)
print(user3.stock_num)

del user1
print(user2.stock_num)
print(user3.stock_num)
