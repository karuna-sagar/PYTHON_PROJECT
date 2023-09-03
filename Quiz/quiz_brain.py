class QuizBrain:
    def __init__(self,question):
        self.question_number =0
        self.question_list = question
        self.score = 0
    def is_still_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_choice,current_question.answer)
    def check_answer(self,user_choice,curr_question):
        if user_choice.lower() == curr_question.lower():
            print("You got it right")
            self.score +=1
        else:
            print(f"You got wrong answer!")
        print(f"The correct answer is: {curr_question}")
        print((f"Your current score is {self.score}/{self.question_number}"))
        print("\n")