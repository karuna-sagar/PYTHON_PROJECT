from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
Question_bank  = []
for item in question_data:
    question = item["text"]
    answer = item["answer"]
    new_question = Question(question,answer)
    Question_bank.append(new_question)
quiz = QuizBrain(Question_bank)
while quiz.is_still_question():
    quiz.next_question()
print("You Have Completed The Quiz")
print(f"Your Final Score is :{quiz.score}/{quiz.question_number}")