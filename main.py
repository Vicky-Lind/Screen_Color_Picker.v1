#*****************************************************
# @author: VL
# @since: 18.5.2023
# @version: 1.0
#*****************************************************/


import sys 
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint, QPoint
import PyQt5.QtWidgets as QW
from PyQt5.QtWidgets import QPushButton, QColorDialog, QDesktopWidget, QFrame

class MainWindow(QW.QMainWindow):

    def __init__(self):
        super().__init__()

        # Set the QMainWindow to not have default windows frame
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # Set the QMainWindow to be transparent
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, 300, 150)

        main_frame = QFrame(self)
        main_frame.setGeometry(0, 30, 300, 100)
        main_frame.setStyleSheet("""
            QFrame {
                background: QLinearGradient( x1: 0, y1: 0,
                                            x2: 0, y2: 1, 
                                            stop: 0 #5a4bf0, 
                                            stop: 1 #85c4f9 );
                border-radius: 30px;
            }
        """)


        open_button = QPushButton('Open color dialog', self)
        open_button.setGeometry(24, 60, 125, 40)
        open_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 130);
                border-color: white;
                border-style: solid;
                border-width: 3px;
                color: rgba(0, 0, 0, 200);
                font-family: Yu Gothic UI Light;
                font-size: 14px;
                border-top-left-radius: 15px;
                border-bottom-left-radius: 15px;
            } 
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 80);
            }
        """)
        open_button.clicked.connect(QColorDialog.getColor)

        close_button = QPushButton('Exit', self)
        close_button.setGeometry(149, 60, 125, 40)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 130);
                border-color: white;
                border-style: solid;
                border-width: 3px;
                color: rgba(0, 0, 0, 200);
                font-family: Yu Gothic UI Light;
                font-size: 14px;
                border-top-right-radius: 15px;
                border-bottom-right-radius: 15px;
            } 
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 80);
            }
        """)
        close_button.clicked.connect(self.close)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.center())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

if __name__ == "__main__":
    app = QW.QApplication(sys.argv)
    app.setStyle('Fusion')
    appWindow = MainWindow()
    appWindow.show()
    sys.exit(app.exec())