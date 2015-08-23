__author__ = 'stdimitriev@mail.ru'

from PyQt4 import QtGui, uic

input = file("C:\PycharmProjects\AI\UI\mainWindow.ui")
output = open("C:\PycharmProjects\AI\UI\ui_MainWindow.py", "w")
uic.compileUi(input, output)
