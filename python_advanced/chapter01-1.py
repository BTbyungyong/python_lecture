# Chapter01-1
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) - 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 학생1
student_name_1 = "Kim"
student_num_1 = 1
student_grade_1 = 1
student_detail = [{"gender": "Male"}, {"score1": 95}, {"score2": 88}]

# 학생2
student_name_2 = "Lee"
student_num_2 = 2
student_grade_2 = 2
student_detail = [{"gender": "Female"}, {"score1": 95}, {"score2": 77}]

# 학생3
student_name_3 = "Park"
student_num_3 = 3
student_grade_3 = 4
student_detail = [{"gender": "Male"}, {"score1": 99}, {"score2": 60}]

# 리스트 구조
student_names_list = ["Kim", "Lee", "Park"]
student_numbers_list = [1, 2, 3]
student_grades_list = [1, 2, 4]
student_details_list = [
    {"gender": "Male", "score1": 95, "score2": 88},
    {"gender": "Female", "score1": 95, "score2": 77},
    {"gender": "Male", "score1": 99, "score2": 60},
]

# 학생 삭제
del student_names_list[1]
del student_numbers_list[1]
del student_grades_list[1]
del student_details_list[1]

print(student_names_list)
print(student_numbers_list)
print(student_grades_list)
print(student_details_list)

# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제
students_dicts = [
    {
        "student_name": "Kim",
        "student_number": 1,
        "student_grade": 1,
        "student_detail": {"gender": "Male", "score1": 95, "score2": 88},
    },
    {
        "student_name": "Lee",
        "student_number": 2,
        "student_grade": 2,
        "student_detail": {"gender": "Female", "score1": 95, "score2": 77},
    },
    {
        "student_name": "Park",
        "student_number": 3,
        "student_grade": 4,
        "student_detail": {"gender": "Male", "score1": 99, "score2": 60},
    },
]

del students_dicts[1]

print(students_dicts)

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용
class Student:
    def __init__(self, name, number, grade, details):
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details

    # 우선순위 str > repr
    def __str__(self):
        return "str {} - {}:".format(self._name, self._number)

    def __repr__(self):
        return "repr {} - {}:".format(self._name, self._number)


student1 = Student("Kim", 1, 1, {"gender": "Male", "score1": 95, "score2": 88})
student2 = Student("Lee", 2, 1, {"gender": "Female", "score1": 95, "score2": 77})
student3 = Student("Park", 4, 1, {"gender": "Male", "score1": 99, "score2": 60})

print(student1.__dict__)
print(student2.__dict__)
print(student3.__dict__)

# 리스트 선언
students_list = []

students_list.append(student1)
students_list.append(student2)
students_list.append(student3)

print(students_list)

for x in students_list:
    print(x)
    print(repr(x))
