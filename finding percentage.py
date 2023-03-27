n = int(input())
student_marks = {}
student_average = {}
for i in range (n):
    name, *line= input().split()
    score = list(map(float,line))
    student_marks[name] = score
    average = sum(score)/3.0
    student_average[name] = average
query_name = input()

if query_name in student_marks:
    y = ((float(student_marks[query_name][0])+float(student_marks[query_name][1])+float(student_marks[query_name][2]))/3)
print(f"%.2f" %y)