from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_object = Question(question["text"], question["answer"])
    question_bank.append(question_object)

quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quizz.score}/12")