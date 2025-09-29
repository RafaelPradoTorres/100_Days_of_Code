from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.label_score = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question = self.canvas.create_text(
            150,
            125,
            text="ê lalaia ê lalaia",
            font=("Arial", 20, "italic"),
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_right = PhotoImage(file='./images/true.png')
        self.button_right = Button(image=img_right)
        self.button_right.grid(row=2, column=0)

        img_wrong = PhotoImage(file='./images/false.png')
        self.button_wrong = Button(image=img_wrong)
        self.button_wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)
