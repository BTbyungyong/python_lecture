# Chapter01-3
# 클래스 메소드, 인스턴스 메소드, 스테틱 메소드

# 기본 인스턴스 메소드
class Student(object):
    """
    Student Class
    Author :
    Date :
    Description : Class, Static, Instance Method
    """

    # Class Variable
    tuition_per = 1.0  # 등록금

    def __init__(self, id, first_name, last_name, email, grade, tuition, gpa):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._grade = grade
        self._tuition = tuition
        self._gpa = gpa

    # Instance Method
    def full_name(self):
        return "Name : {} {}".format(self._first_name, self._last_name)

    # Instance Method
    def detail_info(self):
        return "Student Detail Info : {} {} {} {} {}".format(
            self._id, self.full_name(), self._email, self._grade, self._gpa
        )

    # Instance Method
    def get_fee(self):
        return "Before Tuition -> Id : {}, fee: {}".format(self._id, self._tuition)

    # Instance Method
    def get_fee_calc(self):
        return "After Tuition -> Id : {}, fee: {}".format(
            self._id, self._tuition * Student.tuition_per
        )

    # Class Method
    @classmethod
    def raise_fee(cls, per):
        if per <= 1:
            print("Please Enter 1 or more")
            return
        cls.tuition_per = per
        print("Suceed! tuition increase")

    # Class Method
    @classmethod
    def student_const(cls, id, first_name, last_name, email, grade, tuition, gpa):
        return cls(
            id, first_name, last_name, email, grade, tuition * cls.tuition_per, gpa
        )

    # Static Method
    @staticmethod
    def is_scholarship_st(inst):
        if inst._gpa >= 4.3:
            return "{} is a scholarship recipient".format(inst._last_name)
        return "Sorry. Not a scholarship recipient"

    def __str__(self):
        return "Student Info -> name: {} grade: {} email: {}".format(
            self.full_name(), self._grade, self._email
        )


student1 = Student(1, "Kim", "Sarang", "sss@sds.ca", "1", 400, 3.5)
student2 = Student(2, "Lee", "Myungho", "sss@sddsa.ca", "2", 500, 4.3)

# 기본정보
print(student1)
print(student2)

# 전체정보
print(student1.detail_info())
print(student2.detail_info())

# 학비 정보(인상 전)
print(student1.get_fee())
print(student2.get_fee())

# 학비 인상(클래스 메소드 미사용)
# Student.tuition_per = 1.2

# 학비 인상(클래스 메소드 사용)
Student.raise_fee(1.5)

# 학비 정보(인상 후)
print(student1.get_fee_calc())
print(student2.get_fee_calc())

# 클래스 메소드 인스턴스 생성
student3 = Student.student_const(3, "Park", "Minji", "sss@sddsa.ca", "3", 600, 4.0)
student4 = Student.student_const(4, "Cho", "ddd", "sss@sddsa.ca", "4", 600, 4.1)

# 전체 정보
print(student3.detail_info())
print(student4.detail_info())

# 학비 변경 확인
print(student3._tuition)
print(student4._tuition)

# 장학금 혜택 여부(스테틱 메소드 미사용)
def is_scholarship(inst):
    if inst._gpa >= 4.3:
        return "{} is a scholarship recipient".format(inst._last_name)
    return "Sorry. Not a scholarship recipient"


print(is_scholarship(student1))
print(is_scholarship(student2))
print(is_scholarship(student3))
print(is_scholarship(student4))

# 장학금 혜택 여부(스테틱 메소드 사용)
print(Student.is_scholarship_st(student1))
print(Student.is_scholarship_st(student2))
print(Student.is_scholarship_st(student3))
print(Student.is_scholarship_st(student4))

print(student1.is_scholarship_st(student1))
print(student2.is_scholarship_st(student2))
print(student3.is_scholarship_st(student3))
print(student4.is_scholarship_st(student4))
