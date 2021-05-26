class FeedbackCollector:
    feedback_triggers = ["bye", "goodbye", "quit", "exit"]

    feedback_questions = ["Was the module taught this week was presented in a sequence that helped your learning?",                             "Did you have a chance to practice?",
                    "Do you think that you have enough materials to practice and prepare for this module?",
                    "Was there any material that you found difficult?",
                    "Any topic that you found difficult?"]

    def is_exit(self, question:str):
        return question in self.feedback_triggers

    def record_answer(self, question: str, answer: str):
        filename = 'exit_questions.txt'
        with open(filename, 'a') as f:
            f.write(question + "," + answer + "\n")



    