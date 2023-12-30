from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
# The colon after the quiz_brain item that gets passed into our function MUST be of type QuizBrain, which is a declared class in another file in this project. The thing after the colon specifies what type the function is expecting and is less error prone than just guessing at the type that needs to be passed in. Specify the output with this: -> type:
# This is known as a type hint

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.minsize(width=300, height=450)

        self.score_label = Label(font=("Arial",15,"normal"),bg=THEME_COLOR, highlightthickness=0, text=f"Score: {self.score}", fg="white")
        self.score_label.grid(row=0, column = 1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="This should display some text. Now is the winter of our discontent. I like turtles",
            font=('Arial', 20, "italic"),
            width=280,
            fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan = 2, pady=50)

        true_button_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image = true_button_img, highlightthickness=0, command=self.true_button)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():

            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\nFinal Score: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_button(self):
        # self.get_next_question()
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button(self):
        # self.get_next_question()
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
