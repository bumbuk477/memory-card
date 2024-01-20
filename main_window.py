from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*

def swich_screen():
    if btn_answer.text()== "Відповісти":
        qwestion_group.hide()
        answer_group.show()
        btn_answer.setText("Наступне питання")
    else:
        qwestion_group.show()
        answer_group.hide()
        btn_answer.setText("Відповісти")

btn_menu = QPushButton('Меню')
btn_sleep = QPushButton("Відпочити")
btn_answer = QPushButton('Відповісти')
timer = QSpinBox()
timer.setValue(30)
timer_text = QLabel('Хвилин')

text_qwestion = QLabel("Питання")
right_answer = QLabel("Відповідь")
text_result = QLabel("Результат")

rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')
radio_group = QButtonGroup()
radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)


qwestion_group = QGroupBox("Варівнт відповідей")
answer_group=QGroupBox("Резудьтат тесту")

line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line3_q = QHBoxLayout()
line3_a = QVBoxLayout()
line4 = QHBoxLayout()

line_v1 = QVBoxLayout()
line_v2 = QVBoxLayout()

line_v1.addWidget(rbtn1)
line_v1.addWidget(rbtn2)
line_v2.addWidget(rbtn3)
line_v2.addWidget(rbtn4)

line3_q.addLayout(line_v1)
line3_q.addLayout(line_v2)

qwestion_group.setLayout(line3_q)

line3_a.addWidget(text_result,alignment=(Qt.AlignLeft |Qt.AlignTop))
line3_a.addWidget(right_answer,alignment=Qt.AlignCenter)
answer_group.setLayout(line3_a)
answer_group.hide()



line1.addWidget(btn_menu)
line1.addStretch(1)
line1.addWidget(btn_sleep)
line1.addWidget(timer)
line1.addWidget(timer_text)

line2.addWidget(text_qwestion,alignment=Qt.AlignCenter)

line3.addWidget(qwestion_group)
line3.addWidget(answer_group)
line4.addStretch(1)
line4.addWidget(btn_answer,stretch=2)
line4.addStretch(1)

line.addLayout(line1,stretch=1)
line.addLayout(line2,stretch=2)
line.addLayout(line3,stretch=6)
line.addStretch(1)
line.addLayout(line4,stretch=3)
line.addStretch(1)
