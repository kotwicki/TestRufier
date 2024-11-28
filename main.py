from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

app = QApplication([])
window = QWidget()

window.resize(300, 300)
window.setWindowTitle('Медичний додаток')

# створюємо шпблом за яким будемо розташовувати віджети
v_line = QVBoxLayout()

# створюємо віджети
question1 = QLineEdit()
question1.setPlaceholderText('питання №1')
btn_ok = QPushButton('Результат')

#додати стоврені віджети в шаблон
v_line.addWidget(question1)
v_line.addWidget(btn_ok)

# додаємо шалон до нашого вікна (можно тільки один шалон)
window.setLayout(v_line)


window.show()
app.exec_()