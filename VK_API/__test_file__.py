# coding=utf-8
__author__ = 'stdimitriev@mail.ru'

import json


def main():
    file = open('user_dialog.txt')
    messages = json.load(file)
    print(len(messages))
    #for message in messages:
    #    print(message['text'])

if __name__ == '__main__':
    main()
