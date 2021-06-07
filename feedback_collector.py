class FeedbackCollector:
    feedback_triggers = ["bye", "goodbye", "quit", "exit"]

    feedback_questions = ["Was the module taught this week was presented in a sequence that helped your learning?",                             "Did you have a chance to practice?",
                    "Do you think that you have enough materials to practice and prepare for this module?",
                    "Was there any material that you found difficult?",
                    "Any topic that you found difficult?",
                    "How many class (or section) sessions did you attend?",
                    "On average, how many hours per week have you spent on this course (or section),including attending classes and doing readings, reviewing notes, and any other course-related work?",
                    "Did you finish your quiz this week?",
                    "Did you finish your discussion forum submission this week?",
                    "How satisfied were you with your effort in this course (or section)?",
                    "what you consider to be the topic that you understood the least in this module?"]
    def is_exit(self, question:str):
        return question in self.feedback_triggers

    def record_answer(self, question: str, answer: str):
        filename = 'exit_questions.txt'
        with open(filename, 'a') as f:
            f.write(question + "," + answer + "\n")



    