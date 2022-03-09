import html

class QuizBrain:

    def __init__(self,g_list):
        self.question_number=0
        self.q_list=g_list
        self.score=0
        self.current_question=None

    def still_has_question(self):
        #running the program and showing the questions untill the last one(len(q_list))
        return self.question_number<len(self.q_list)

    def  next_question(self):
        self.current_question=self.q_list[self.question_number]
        self.question_number+=1
        #html unescape can change the text into human readable
        q_text=html.unescape(self.current_question.text)
        return f"Q.{self.question_number}:{q_text} "

    def check_answer(self,user_answer):
        #checking user answers and correct answers and giving the score for correct one
        correct_answer=self.current_question.answer
        if user_answer.lower()==correct_answer.lower():
            self.score+=1
            return True
        else:
            return False



