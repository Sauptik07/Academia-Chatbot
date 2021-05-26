from interfaces import Chatter
import text2emotion as te

class MoodChatter(Chatter):
    def human_mood_find(x):
        emotion_dict = te.get_emotion(x)
        return emotion_dict

    def __init__(self) -> None:
        super().__init__()
                
    def get_answer(self, question: str) -> str:
        answer = {}
        answer = MoodChatter.human_mood_find(question)
        filename = 'mood.txt'
        with open(filename, 'w') as f:
            for i,j in answer.items():
                f.write(i + ' : ' + str(j))
                f.write('\n')
        return None
    
