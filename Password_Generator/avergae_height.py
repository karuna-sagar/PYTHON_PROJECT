# 🚨 Don't change the code below 👇
import math
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
sum =0
for k in range(0,len(student_heights)):
    sum+= student_heights[k]
avg = math.floor(sum/len(student_heights))
#Write your code below this row 👇
print(student_heights)
print(sum)
print(f"Your Average score is {avg}")