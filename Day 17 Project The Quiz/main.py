from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]

    #Creating a list of 'Question' Objects
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

questions = QuizBrain(question_bank)

print("Welcome to The Quiz!")
while questions.still_has_questions():
    questions.next_question()