from interfaces import Chatter
from textblob import TextBlob

class FeedbackChatter(Chatter):
    positive_feedbacks = 0
    negative_feedbacks = 0
    def feedback(x):
        feedback_polarity = TextBlob(x).sentiment.polarity
        if feedback_polarity>=0:
            FeedbackChatter.positive_feedbacks += 1
        else:
            FeedbackChatter.negative_feedbacks += 1

    def __init__(self) -> None:
        super().__init__()
                
    def get_answer(self, question: str) -> str:
        if FeedbackChatter.positive_feedbacks > FeedbackChatter.negative_feedbacks:
            answer = 'Positive Feedback: ' + question
            return answer
        answer = 'Negative Feedback: ' + question
        return answer
    
