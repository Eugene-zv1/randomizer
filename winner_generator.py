#подключение библиотек
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint
def show_winner():
    if number.text() == '?':
        random_number = randint(1,100)
        number.setText(str(random_number))
        text.setText('Победитель:')
        btn.setText('Выход')
    elif btn.text() == 'Выход':
        window.close()

#создание элементов интерфейса

app = QApplication([])
window = QWidget()
window.setWindowTitle('Рандомайзер')
window.resize(900, 700)
window.move(10,11)

#привязка элементов к вертикальной линии

text = QLabel('Нажми и узнай победителя!!!')

number = QLabel('?')
btn = QPushButton('Создать')
btn.clicked.connect(show_winner)
v_line  = QVBoxLayout()
v_line.addWidget(text, alignment = Qt.AlignCenter)
v_line.addWidget(number, alignment = Qt.AlignCenter)
v_line.addWidget(btn, alignment = Qt.AlignCenter)

window.setLayout(v_line)

#запуск приложения

window.show()
app.exec()