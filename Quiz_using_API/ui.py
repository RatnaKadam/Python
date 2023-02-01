import tkinter
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Times', '20', 'bold italic')


class QuizInterface:
    def __init__(self, quizzy: QuizBrain):
        self.quiz = quizzy
        # create window
        self.window = Tk()
        self.window.title("Welcome to Quiz Game!!")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        # create label
        self.label = Label(text="Score: 0")
        self.label.configure(activebackground=THEME_COLOR, activeforeground="white")
        self.label.grid(column=1, row=0)

        # create canvas
        self.canvas = Canvas(height=250, width=300)
        self.canvas.configure(bg="white", bd=0)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Hello there", fill=THEME_COLOR, font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # create buttons
        self.right_img = tkinter.PhotoImage(file="images/true.png")
        right_button = Button(image=self.right_img, highlightthickness=0, command=self.true_pressed)
        right_button.grid(column=0, row=2)

        self.wrong_img = tkinter.PhotoImage(file="images/false.png")
        wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.false_pressed)
        wrong_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=q_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="Quiz ends here!")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
