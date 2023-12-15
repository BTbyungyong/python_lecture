# Section09
# 파일 읽기, 쓰기
# 읽기모드 : r, 쓰기모드(기존 파일 삭제) : w, 추가모드(파일 생성 또는 추가) : a

# 파일 읽기
# ex1
f = open("./resource/review.txt", "r")
content = f.read()
print(content)
# 반드시 close로 리소스 반환
f.close()
# print(dir(f))

# ex2
# with close호출 없어도 with문 종료 시 리소스 반환
with open("./resource/review.txt", "r") as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

# ex3
with open("./resource/review.txt", "r") as f:
    for c in f:
        print(c, end="")
        print(c.strip())

# ex4
with open("./resource/review.txt", "r") as f:
    content = f.read()
    print(content)
    # read는 한번 파일 읽고 나면 포커스가 파일 마지막으로 이동. 이후 내용 없기 때문에
    # 다시 파일 읽어도 쓸모없음
    content = f.read()
    print(content)

# ex5
with open("./resource/review.txt", "r") as f:
    line = f.readline()  # 한줄 읽기
    # print(line)
    while line:
        print(line, end="# ")
        line = f.readline()

# ex6
with open("./resource/review.txt", "r") as f:
    contents = f.readlines()  # \n(줄바꿈) 기준으로 리스트로 반환
    print(contents)
    for c in contents:
        print(c, end="* ")
print()

# ex7
score = []

with open("./resource/score.txt", "r") as f:
    for line in f:
        score.append(int(line))
    print(score)

print("평균:{:6.3}".format(sum(score) / len(score)))

# 파일 쓰기
# ex1
with open("./resource/text1.txt", "w") as f:
    f.write("niceman\n")

# ex2
with open("./resource/text1.txt", "a") as f:
    f.write("niceman!!\n")

# ex3
from random import randint

with open("./resource/text2.txt", "a") as f:
    for cnt in range(6):
        f.write(str(randint(1, 46)))
        f.write("\n")

# ex4
# writelines : 리스트를 파일로 저장
# readlines와 반대 역할
with open("./resource/text3.txt", "a") as f:
    file_list = ["Kim\n", "Park\n", "Cho\n"]
    f.writelines(file_list)

# ex5
with open("./resource/text4.txt", "a") as f:
    print("Test contents1", file=f)
    print("Test contents2", file=f)
