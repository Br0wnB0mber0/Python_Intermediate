from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# Creates an empty list we will pass to the QuizBrain object we create later in the program
question_bank = []
# for loop that pulls the question and answer from the question_data dictionary from the data class, creates a Question object using that
# Then adds that question to the question bank list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
# Pass the QuizBrain into the quiz UI, so we can get access to the next_question() method and use that to update the canvas image text
quiz_ui = QuizInterface(quiz)
# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
