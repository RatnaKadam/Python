from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    question_text = ques["question"]
    question_answer = ques["correct_answer"]
    new_ques = Question(q_text=question_text, q_ans=question_answer)
    question_bank.append(new_ques)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the Quiz game.")
print(f"Your final score is: {quiz.score}/{quiz.ques_num}")
