# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print("Hello Python!")
print("Hello Python!")
print("""Hello Python!""")
print("""Hello Python!""")

print()

# Separator 옵션 사용
print("T", "e", "s", "t", sep="")
print("2019", "02", "19", sep="-")
print("niceman", "google.com", sep="@")

# End 옵션 사용
print("Welcome To", end=" ")
print("the black parade", end=" ")
print("piano notes")

print()

# Format 사용
print("{} and {}".format("You", "Me"))
print("{0} and {1} and {0}".format("You", "Me"))
print("{a} and {b}".format(a="You", b="Me"))

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ("Eunki", 7))

print("Test1: %5d, Price: %4.2f" % (776, 6534.123))
print("Test1: {0:5d}, Price: {1:4.2f}".format(776, 6534.123))
print("Test1: {a:5d}, Price: {b:4.2f}".format(a=776, b=6534.123))

print("'you'")
print("'you'")
print('"you"')
print("""'you'""")
print("\\you\n")
print("\t\t\ttest")
