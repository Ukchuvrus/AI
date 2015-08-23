# coding=utf-8
from PyQt4.QtGui import QApplication, QMainWindow, QKeySequence
from PyQt4.QtCore import pyqtSignal, QObject, QString, Qt, QEvent

__author__ = 'stdimitriev@mail.ru'

import sys
from datetime import datetime
from Controller.genarator import Generator

from PyQt4 import QtGui, QtCore

from ui_MainWindow import Ui_MainWindow


class CustomMainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.isShiftPressed = False
        self.model = Model()
        self.generator = Generator()

        self.ui.showArea.setReadOnly(True)
        self.ui.sendButton.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_Q))

        self.connect(self.ui.sendButton, QtCore.SIGNAL('clicked()'), self.onSendButtonClicked)
        self.connect(self.model, QtCore.SIGNAL('messageAdded(QString)'), self.onMessageAdded)

    def onSendButtonClicked(self):
        question = self.ui.inputArea.toPlainText()
        if question:
            message = Message(question, u"Станислав")
            self.ui.inputArea.clear()
            self.model.addMessage(message)

            answer = self.generator.getAnswer(question)
            self.model.addMessage(Message(answer, u"Катерина"))

    def onMessageAdded(self, message):
        self.ui.showArea.append(message + "\n")



class Message:
    def __init__(self, text, author):
        self.datetime = datetime.now()
        self.text = text
        self.author = author

    def toString(self):
        return QString(self.getTime()) + " " + QString(self.author) + QString(u" ответил:\n ") + self.text

    #def __str__(self):
    #    return self.text.encode("utf-8")#"%s %s %s: \n%s" % (self.getTime(), self.author, u"said", self.text.encode("utf-8"))

    def getTime(self):
        return self.datetime.strftime("%d.%m.%y %I:%M %p")


class Model(QObject):
    messageAdded = pyqtSignal(QString, name="messageAdded")

    def __init__(self):
        QObject.__init__(self)
        self.messages = []

    def addMessage(self, message):
        self.messages.append(message)
        self.messageAdded.emit(message.toString())


def main():
    a = QApplication(sys.argv)

    w = CustomMainWindow()
    w.setWindowTitle("Let's talk, bitch!")

    # Show window
    w.show()

    sys.exit(a.exec_())


if __name__ == '__main__':
    main()
