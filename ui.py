from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR="#375362"

class QuizInterface:

    def __init__(self,quiz_in:QuizBrain):
        #pssing the parameter quiz so that we can use quizbrain class in ui
        #ex:type hints
        #def greeting(name:str)->str:(passing the parameter and giving tha data type that we want to use)
            #return "hello"+name(it must be str if we give another data type it'll show you erroe)
        self.quiz=quiz_in
        self.window=Tk()
        self.window.title("QUIZ GAME")
        self.window.config(padx=50,pady=50,bg=THEME_COLOR)

        #score label
        self.score_label=Label(text="Score:0",fg="white",font=("arial",30,"bold"),bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)
        
        #create canvas
        self.canvas=Canvas(width=600,height=400,bg="white")
        self.canvas_text=self.canvas.create_text(300,200,
                                                 text="quiz questions will appear here",width=580,
                                                 font=("arial",30,"bold"),fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2,pady=10)

        #true image button
        true_image=PhotoImage(file="images/true.png")
        self.true_button=Button(image=true_image,highlightthickness=0,command=self.true_click)
        self.true_button.grid(column=0,row=2)

        #false image button
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,command=self.false_click)
        self.false_button.grid(column=1, row=2)

        self.get_new_question()

        self.window.mainloop()

    def get_new_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_question():
            current_question=self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=current_question)
            self.score_label.config(text=f"Score:{self.quiz.score}")
        else:
            self.canvas.itemconfig(self.canvas_text, text=f"you've reached the end of this quiz, here is your final score"
                                                      f" {self.quiz.score}/{self.quiz.question_number}")
            self.score_label.config(text=f"Score:{self.quiz.score}")
            #disabilling tyhe buttons after quiz
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_click(self):
            is_right=self.quiz.check_answer("True")
            self.show_info(is_right)

    def false_click(self):
        self.show_info(self.quiz.check_answer("False"))

    def show_info(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_new_question)



