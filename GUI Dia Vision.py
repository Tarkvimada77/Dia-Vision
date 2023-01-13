import os
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
import Defenation_for_Countours
import Detect_countours

class dlgMain(QDialog):
    def __init__(self):

        super().__init__()

        self.res = [""]

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle("Dia Vision")
        self.resize(450, 220)

        self.label = QLabel("Введите путь до файла: ", self)
        self.label.setFont(QFont("Arial", 11))
        self.label.move(10, 20)

        self.butt_file = QPushButton("Выбрать путь", self)
        self.butt_file.move(225, 16)
        self.butt_file.setFont(QFont("Arial", 9))
        self.butt_file.clicked.connect(self.vybor)

        self.lebel_name = QLabel("Введите название файла: ", self)
        self.lebel_name.setFont(QFont("Arial", 11))
        self.lebel_name.move(10, 80)

        self.editText = QLineEdit("", self)
        self.editText.setFont(QFont("Arial", 9))
        self.editText.move(240, 80)

        self.final_button = QPushButton("Компелировать график", self)
        self.final_button.setFont(QFont("Arial", 11))
        self.final_button.move(115, 150)
        self.final_button.clicked.connect(self.final_func)


    def vybor(self):
        self.res = QFileDialog.getOpenFileName(self, "open", r"C:\Users", "Graphic png(*.png)")

        if self.res[0] != '':
            a = QMessageBox.information(self, "Info", f"Путь успешно сохранён \n({self.res[0]})")
        else:
            a = QMessageBox.warning(self, "Warning", "НИЧЕГО НЕ ВЫБРАНО!!!")

    def final_func(self):
        if self.res[0] == '':
            az = QMessageBox.warning(self, "Warning", "Вы не выбрали файл")
        if self.editText.text() == "":
            ax = QMessageBox.warning(self, "Warning", "Вы не дали название ")

        result = Detect_countours.coo(len(Defenation_for_Countours.pixel_cont(Defenation_for_Countours.rotata(self.res[0]))), Defenation_for_Countours.rotata(self.res[0]))

        Detect_countours.cont_to_ex(self.editText.text(), Detect_countours.raspk_coort(result))

        os.remove(Defenation_for_Countours.rotata(self.res[0]))

        azx = QMessageBox.information(self, "Успех", "График успешно скомпелирован")


# Создаём экземляр программы и запускаем
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Создаём экземпляp созданного изменённого файла
    main = dlgMain()

    # Рисуем окно виджетов
    main.show()

    # Бесконечный цикл (луп)

    sys.exit(app.exec_())