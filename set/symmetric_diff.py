n = int(input())
eng_student = set(map(int, input().split()))
f = int(input())
french_stu = set(map(int, input().split()))

print(*sorted(eng_student.symmetric_difference(french_stu)), sep='\n')