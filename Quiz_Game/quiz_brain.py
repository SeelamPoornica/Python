class Quiz_Brain:
    def __init__(self,question_list):
        self.question_no=0
        self.question_list=question_list
        self.score=0

    def next_question(self):
        curr_question=self.question_list[self.question_no]
        self.question_no += 1
        user_answer=input(f"Q.{self.question_no}:{curr_question.q_text}(True/False): ")
        self.check_answer(user_answer,curr_question.answer_text)

    def still_has_questions(self):
        return self.question_no<len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            print("You are right!")
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_answer}.")
        print(f"The current score is {self.score}/{self.question_no}.")
        print("\n")
