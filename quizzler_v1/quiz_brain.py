import html
# Creates the QuizBrain class, requires a list parameter to be passed in during the object creation
class QuizBrain:

    def __init__(self, q_list):
        # Defines the question number, score, current question, and takes the list that was passed in and sets the self.question_list variable
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    # If the question number is less that the length of the question list, returns True
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Function that creates a question for the quiz game
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    # Function that checks the user answer against the correct one and returns True or False, increasing the score as appropriate
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if correct_answer == user_answer:
            self.score += 1
            return True
        else:
            return False




