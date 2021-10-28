from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()

print("You've completed the quiz")
print(f"You're final score is: {qb.score}/{qb.question_number}")