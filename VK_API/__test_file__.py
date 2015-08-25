# coding=utf-8
__author__ = 'stdimitriev@mail.ru'

import json


def main():
    file = open('user_documents.txt')
    messages = json.load(file)
    print(len(messages))
    print(messages[0]['body'])
    print(messages[1]['body'])
    print(messages[2]['body'])

    #for message in messages:
    #    print(message['text'])

if __name__ == '__main__':
    main()
