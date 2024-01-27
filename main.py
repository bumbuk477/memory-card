from PyQt5.QtWidgets import *
app = QApplication([])
from main_window import *
from random import choice,shuffle

class Question:
    def __init__(self,question,answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.attemps = 0
        self.correct = 0
    def got_right(self):
        self.attemps += 1
        self.correct += 1
        print("Це правильна відповідь!")
    

    def got_wrong(self):
        self.attemps += 1
        print("Відповідь невірна")

def new_question(question,radio_list):
    random_question = choice(question)
    text_qwestion.setText(random_question.question)
    right_answer.setText(random_question.answer)
    answer = radio_list[0]
    wrong_answer1,wrong_answer2,wrong_answer3 = radio_list[1],radio_list[2],radio_list[3]
    answer.setText(random_question.answer)
    wrong_answer1.setText(random_question.wrong_answer1)
    wrong_answer2.setText(random_question.wrong_answer2)
    wrong_answer3.setText(random_question.wrong_answer3)
    return random_question


def swich_screen():
    global random_question
    if btn_answer.text()== "Відповісти":
        qwestion_group.hide()
        answer_group.show()
        btn_answer.setText("Наступне питання")
    else:
        qwestion_group.show()
        answer_group.hide()
        btn_answer.setText("Відповісти")
        random_question = new_question(question,radio_list)




q1 = Question("Яблуко","apple","aple","ale","aplle")
q2 = Question("Машина","car","lamborgini","buss",'ckar')
q3 = Question("Будинок","house","home","horse","homework")
question = [q1,q2,q3]

radio_list = [rbtn1,rbtn2,rbtn3,rbtn4]
shuffle(radio_list)

main_win = QWidget()
main_win.resize(600,500)
main_win.setWindowTitle("Memory card")
main_win.move(300,300)


main_win.setLayout(line)


random_question = new_question(question,radio_list)
btn_answer.clicked.connect(swich_screen)
main_win.show()



app.exec()
