# Creates the question class. The object needs two parameters in the call to function:
# The question text, which is the question from question_data in the data class
# The question answer, also from question_data
# Powers combined, this creates the Question object
class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
