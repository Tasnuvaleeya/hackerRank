n = int(input())
eng_student = set([int(x) for x in input().split()])
f = int(input())
french_stu = set([int(i) for i in input().split()])

both = eng_student.intersection(french_stu)

print(both)
print(len(both))
