from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStackedLayout, QHBoxLayout, QMessageBox, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from method_only_integral_and_method_integral_of_piece_res.method_only_integral import *
from method_only_integral_and_method_integral_of_piece_res.method_integral_of_piece import *
from method_introduction_under_dif_sign.method_introduction_under_dif_sign import *

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.setWindowTitle("integrApp")
        self.setGeometry(0, 0, 1680, 720)

        self.container = QWidget(self)
        self.setCentralWidget(self.container)
        self.container_layout = QVBoxLayout(self.container)

        self.stacked_layout = QStackedLayout()
        self.container_layout.addLayout(self.stacked_layout)

        self.frames = {}

        for F in (Menu, Definite_Integral, Indefinite_Integral):
            frame = F(self)
            self.frames[F] = frame
            self.stacked_layout.addWidget(frame)

        self.show_frame(Menu)

        self.setStyleSheet("QWidget {background-color: rgb(19, 26, 29);}")
        self.setWindowOpacity(0.9)

    def show_frame(self, cont):
        self.stacked_layout.setCurrentWidget(self.frames[cont])


class Menu(QWidget):
    def __init__(self, parent):
        super(Menu, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 100, 0, 250)

        label = QLabel("Выберите раздел интегралов", self)
        label.setStyleSheet("QLabel{font-size:50px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif}")
        label.setAlignment(Qt.AlignCenter)
        font = QFont("Helvetica", 35)
        label.setFont(font)
        label.setStyleSheet("color: rgb(240, 248, 255);")

        self.layout.addWidget(label)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(200)
        # button_layout.setM

        self.button_definite_integral = QPushButton("Определенные интегралы", self)
        self.button_definite_integral.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_definite_integral.setFixedSize(400, 100)
        self.button_definite_integral.clicked.connect(lambda: parent.show_frame(Definite_Integral))
        button_layout.addWidget(self.button_definite_integral)

        self.button_indefinite_integral = QPushButton("Неопределенные интегралы", self)
        self.button_indefinite_integral.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_indefinite_integral.setFixedSize(400, 100)
        self.button_indefinite_integral.clicked.connect(lambda: parent.show_frame(Indefinite_Integral))
        button_layout.addWidget(self.button_indefinite_integral)

        self.setStyleSheet("QPushButton {background-color: rgb(34, 45, 51);}")
        button_layout.setAlignment(Qt.AlignCenter)


        self.layout.addLayout(button_layout)


class Definite_Integral(QWidget):
    def __init__(self, parent):
        super(Definite_Integral, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 100, 0, 300)

        label = QLabel("Определенные интегралы", self)
        label.setStyleSheet("QLabel{font-size:50px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif}")
        label.setAlignment(Qt.AlignHCenter)
        font = QFont("Helvetica", 35)
        label.setFont(font)
        label.setStyleSheet("color: rgb(240, 248, 255);")
        self.layout.addWidget(label, alignment=Qt.AlignCenter)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        self.image_label.setContentsMargins(0, 100, 0, 0)

        self.button_layout = QHBoxLayout(self)

        self.button_method_only_integral = QPushButton("Метод непосредственного интегрирования", self)
        self.button_method_only_integral.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_method_only_integral.clicked.connect(lambda: method_only_integral_definite_integral(self, "image/image.png"))
        self.button_method_only_integral.setFixedSize(350, 100)
        self.button_layout.addWidget(self.button_method_only_integral)

        self.button_integral_of_piece = QPushButton("Интегрирование по частям", self)
        self.button_integral_of_piece.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_integral_of_piece.clicked.connect(lambda: method_integral_of_piece_definite_integral(self, "image/image.png"))
        self.button_integral_of_piece.setFixedSize(350, 100)
        self.button_layout.addWidget(self.button_integral_of_piece)

        self.button_introduction_under_dif_sign = QPushButton("Внесение под знак дифферинциала", self)
        self.button_introduction_under_dif_sign.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_introduction_under_dif_sign.clicked.connect(lambda: method_introduction_under_dis_sign(self, "image/image.png"))
        self.button_introduction_under_dif_sign.setFixedSize(350, 100)
        self.button_layout.addWidget(self.button_introduction_under_dif_sign)

        self.layout.addLayout(self.button_layout)
        self.button_layout.setContentsMargins(0, 100, 0, 0)

        self.button_layout_1 = QHBoxLayout(self)

        
        self.button_indefinite_integral = QPushButton("Неопределенные интегралы", self)
        self.button_indefinite_integral.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_indefinite_integral.setFixedSize(400, 100)
        self.button_indefinite_integral.clicked.connect(lambda: parent.show_frame(Indefinite_Integral))
        self.button_layout_1.addWidget(self.button_indefinite_integral)

        self.layout.addLayout(self.button_layout_1)
        self.button_layout_1.setContentsMargins(0, 100, 0, 0)


        self.setStyleSheet("QPushButton {background-color: rgb(34, 45, 51);}")



class Indefinite_Integral(QWidget):
    def __init__(self, parent):
        super(Indefinite_Integral, self).__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 100, 0, 300)

        label = QLabel("Неопределенные интегралы", self)
        label.setStyleSheet("QLabel{font-size:50px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif}")
        label.setAlignment(Qt.AlignHCenter)
        font = QFont("Helvetica", 35)
        label.setFont(font)
        label.setStyleSheet("color: rgb(240, 248, 255);")
        self.layout.addWidget(label, alignment=Qt.AlignCenter)

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label, alignment=Qt.AlignCenter)
        self.image_label.setContentsMargins(0, 100, 0, 0)

        self.button_layout = QHBoxLayout(self)

        self.button_method_only_integral = QPushButton("Метод непосредственного интегрирования", self)
        self.button_method_only_integral.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_method_only_integral.clicked.connect(lambda: method_only_integral(self, "image/image.png"))
        self.button_method_only_integral.setFixedSize(350, 100)
        self.button_layout.addWidget(self.button_method_only_integral, alignment=Qt.AlignCenter)

        self.button_integral_of_piece = QPushButton("Интегрирование по частям", self)
        self.button_integral_of_piece.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_integral_of_piece.clicked.connect(lambda: method_integral_of_piece(self, "image/image.png"))
        self.button_integral_of_piece.setFixedSize(350, 100)
        self.button_layout.addWidget(self.button_integral_of_piece, alignment=Qt.AlignCenter)

        self.button_introduction_under_dif_sign = QPushButton("Внесение под знак дифферинциала", self)
        self.button_introduction_under_dif_sign.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_introduction_under_dif_sign.clicked.connect(lambda: method_introduction_under_dis_sign(self, "image/image.png"))
        self.button_introduction_under_dif_sign.setFixedSize(350, 100)
        self.button_layout.addWidget(self.button_introduction_under_dif_sign, alignment=Qt.AlignCenter)

        self.layout.addLayout(self.button_layout)
        self.button_layout.setContentsMargins(0, 100, 0, 0)

        self.button_layout_1 = QHBoxLayout(self)

        self.button_definite_integral = QPushButton("Определенные интегралы", self)
        self.button_definite_integral.setStyleSheet("color: rgb(240, 248, 255);")
        self.button_definite_integral.setFixedSize(400, 100)
        self.button_definite_integral.clicked.connect(lambda: parent.show_frame(Definite_Integral))
        self.button_layout_1.addWidget(self.button_definite_integral, alignment=Qt.AlignCenter)

        self.layout.addLayout(self.button_layout_1)
        self.button_layout_1.setContentsMargins(0, 100, 0, 0)

        self.setStyleSheet("QPushButton {background-color: rgb(34, 45, 51);}")


class ImageDialog(QDialog):
    def __init__(self, image_path, parent=None):
        super(ImageDialog, self).__init__(parent)
        self.setWindowTitle("Результат генерирования интеграла")

        layout = QVBoxLayout(self)

        pixmap = QPixmap(image_path)
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        label = QLabel(self)
        label.setStyleSheet("QLabel{font-size:50px;font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif}")
        self.setStyleSheet("QPushButton {background-color: rgb(255, 255, 255);}")
        label.setPixmap(scaled_pixmap)
        label.setScaledContents(True)
        label.setWordWrap(True)

        layout.addWidget(label)

        self.adjustSize()



def method_only_integral(self, image_path):
    dialog = QDialog(self)
    dialog.setWindowTitle("Метод непосредственного интегрирования")

    result_result(0)

    dialog = ImageDialog(image_path)
    dialog.exec_()


def method_integral_of_piece(self, image_path):
    dialog = QDialog(self)
    dialog.setWindowTitle("Метод интегрирования по частям")

    result_method_integral_of_piece(0)

    dialog = ImageDialog(image_path)
    dialog.exec_()

def method_introduction_under_dis_sign(self, image_path):
    dialog = QDialog(self)
    dialog.setWindowTitle("Метод интегрирования путем внесения под дифферинциал")

    result_introd_under_dif_sign(0)

    dialog = ImageDialog(image_path)
    dialog.exec_()

def method_only_integral_definite_integral(self, image_path):
    dialog = QDialog(self)
    dialog.setWindowTitle("Метод непосредственного интегрирования для определенного интеграла")

    result_result(1)

    dialog = ImageDialog(image_path)
    dialog.exec_()

def method_integral_of_piece_definite_integral(self, image_path):
    dialog = QDialog(self)
    dialog.setWindowTitle("Метод интегрирования по частям для определенного интеграла")

    result_method_integral_of_piece(1)

    dialog = ImageDialog(image_path)
    dialog.exec_()

def method_introduction_under_dif_sign(self, image_path):
    dialog = QDialog(self)
    dialog.setWindowTitle("Метод интегрирования путем внесения под дифферинциал")

    result_introd_under_dif_sign(1)

    dialog = ImageDialog(image_path)
    dialog.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec_()
