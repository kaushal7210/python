student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights :
  total_height += height
print(total_height)
total_studs = 0
for length in student_heights :
  total_studs += 1
print(total_studs)
avg_height = total_height/total_studs
print(round(avg_height))