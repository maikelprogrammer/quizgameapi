from data import question_data
from question_model import  Question
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank=[]
for question in question_data:
    c_text=question["question"]
    c_answer=question["correct_answer"]
    c_question=Question(c_text,c_answer)
    question_bank.append(c_question)

quiz=QuizBrain(question_bank)
#passing the quiz obj as a parameter to the quiz_interface so that we can use it in ui.py
quiz_interface=QuizInterface(quiz)

while quiz.still_has_question():
    quiz.next_question()

print(f"your final score is {quiz.score}/{quiz.question_number}")
