# import random
# names = ['karuna','sagar','singh','rajput','shivam','dave','freddie']
# student_score = {student:random.randint(1,100) for student  in names}
# print(student_score)
# passed_student = {student:score for (student,score) in student_score.items() if score>60}
# print(passed_student)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆
result = {word:len(word) for word in sentence.split()}
# Write your code below:



print(result)