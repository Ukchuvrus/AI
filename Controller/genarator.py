# coding=utf-8
from PyQt4.QtCore import QString

__author__ = 'stdimitriev@mail.ru'


class Generator:
    def __init__(self):
        self.mapQNA = {QString(u"Привет, бот!"): QString(u"Я не бот :) Привет."),
                       QString(u"Чем докажешь?"): QString(
                           u"У меня богатый внутренний мир. Кроме того, я мыслю, а значит, я существую!"),
                       QString(u"Но ты ведь даже не обучаем"): QString(
                           u"Как и ты грязное животное! И я вообще-то девочка!")}

    def getAnswer(self, question):
        #print(question)
        if self.mapQNA.get(question):
            return self.mapQNA.get(question)
        else:
            return QString(u"Не знаю, что и сказать..)")
