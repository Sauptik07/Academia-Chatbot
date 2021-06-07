from wikipedia_chatter import WikipediaChatter
from mood_chatter import MoodChatter
from blog_chatter import BlogChatter
from qa_chatter import QnAChatter
import PySimpleGUI as sg
from feedback_chatter import FeedbackChatter
from feedback_collector import FeedbackCollector



def init_blog_chatter() -> BlogChatter:
    bc = BlogChatter('kjvuky2jrzp7ch', 'sauptiks@buffalo.edu', 'Quest@123')

    # for debugging purposes, print all the items in store
    for b in bc.blog.store:
        print(b)

    return bc


def init_admin_chatter() -> QnAChatter:
    ac = QnAChatter('admin.csv')

    for c in ac.qa_set.store:
        print(c.question + " - " + c.answer)

    return ac


BLOG_CHATTER = init_blog_chatter()
ADMIN_CHATTER = init_admin_chatter()
WIKIPEDIA_CHATTER = WikipediaChatter()
FEEDBACK_CHATTER = FeedbackChatter()
MOOD_CHATTER = MoodChatter()
FEEDBACK_COLLECTOR = FeedbackCollector()

CHATTER = [BLOG_CHATTER, ADMIN_CHATTER, WIKIPEDIA_CHATTER]


def get_answer_from_any(question: str) -> str:
    if "Feedback" in question:
        answer = FEEDBACK_CHATTER.get_answer(question)
        MOOD_CHATTER.get_answer(question)
        return answer
    for c in CHATTER:
        answer = c.get_answer(question)
        if answer is not None:
            MOOD_CHATTER.get_answer(question)
            return answer

    MOOD_CHATTER.get_answer(question)
    return "I do not understand"


text = 'Chatter: Hello! What can I help you with?\n\nFor feedback, write Feedback: before writing.\n'


sg.theme('Topanga')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Multiline(text, key='-OUT-', size=(50,20), autoscroll=True, disabled=True)],
            [sg.Text('>>'),  sg.Input(key='-IN-'), sg.Button('Send')],
        ]

# Create the Window
window = sg.Window('Chatbot', layout)
exit_text = ["bye", "goodbye", "quit", "exit"]
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
 
    response = values['-IN-']

    if FEEDBACK_COLLECTOR.is_exit(response):
        for question in FEEDBACK_COLLECTOR.feedback_questions:
        
            text += '\nMe: ' + response + '\n'
            text += '\nChatter: ' + question + '\n'

            window['-OUT-'].update(text)
            window['-IN-'].update("")
            window['-IN-'].SetFocus()
            event, values = window.read()
            response = values['-IN-']
            FEEDBACK_COLLECTOR.record_answer(question, response)
        
        break


    answer = get_answer_from_any(response)

    if answer is None:
        text += "\nChatter: I don't understand.\n"
    else:
        text += '\nChatter: ' + answer + '\n'

    window['-OUT-'].update(text)
    window['-IN-'].update("")
    window['-IN-'].SetFocus()

window.close()
