# Section11
# 파이썬 외부 파일 처리
# excel,csv 파일 읽기 및 처리

# csv : mime - text/csv
import csv

# ex1
with open("./resource/sample1.csv", "r") as f:
    reader = csv.reader(f)
    # next(reader) # 한줄 건너뛰기
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# ex2
with open("./resource/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")  # 구분자 옵션
    # next(reader) # 한줄 건너뛰기
    print(reader)
    print(type(reader))
    print(dir(reader))

    for c in reader:
        print(c)

# ex3(Dict 변환)
with open("./resource/sample1.csv", "r") as f:
    reader = csv.DictReader(f)
    for c in reader:
        # print(c)
        for k, v in c.items():
            print(k, v)
        print("------------")


# ex4
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
with open("./resource/sample3.csv", "w", newline="") as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v)

# ex5
with open("./resource/sample3.csv", "w", newline="") as f:
    wt = csv.writer(f)
    wt.writerows(w)

# xsl,xlsx
# openpyxl, xlsxwriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(openpyxl,xlrd)

import pandas as pd

# sheetname='시트명', 또는 숫자, header=숫자, skiprows=숫자
xlsx = pd.read_excel("./resource/sample.xlsx", engine="openpyxl")

# 상위 데이터 확인
print(xlsx.head())

# 데이터 확인
print(xlsx.tail())

# 엑셀 행,열
print(xlsx.shape)

# 엑셀 or csv 다시 쓰기
xlsx.to_excel("./resource/result.xlsx", index=False)
xlsx.to_csv("./resource/result.csv", index=False)
