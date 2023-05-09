# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
max = 0
for i in range(0,len(student_scores)):
    if student_scores[i] > max:
        max = student_scores[i]
    else:
        max = max
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
print(f"The Highest Number Is: {max}")