# coding=utf-8
__author__ = 'stdimitriev@mail.ru'

import vk_api
import json
from datetime import timedelta
from datetime import datetime


def main():
    # client_id = '5043521'
    # token = 'ce6bf477ce6bf477ceebb0964ece270136cce6bce6bf4779bb1c38045417272d8af6faa'

    # prepare connection
    login = 'ukchuvrus@mail.ru'
    password = ''  # need password
    user_id = 5403120

    vkk = vk_api.VkApi(login, password)
    try:
        vkk.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return


    # fetch service information
    first_values = {
        'count': 1,
        'user_id': user_id
    }
    response = vkk.method('messages.getHistory', first_values)
    if not response:
        print("Good bye. You have not enough mana.")
        return

    messages_count = response['count']

    first_message = {
        'date': response['items'][0]['date'],
        'out': response['items'][0]['out'],
        'body': u''
    }
    last_messages = [
        first_message,
        first_message
    ]

    # fetch messages
    messages = []
    one_count = 200
    offset = 0
    message_id = 0
    while one_count > 0:

        values = {
            'user_id': user_id,
            'count': one_count,
            'offset': offset,
            'rev': 1  # в хронологическом порядке / 0 - с конца
        }
        response = vkk.method('messages.getHistory', values)
        if response['items']:
            for item in response['items']:
                direction = item['out']
                last_date = datetime.fromtimestamp(last_messages[direction]['date'])
                cur_date = datetime.fromtimestamp(item['date'])
                if last_date + timedelta(minutes=15) > cur_date:
                    last_messages[direction] = {
                        'date': item['date'],
                        'out': item['out'],
                        'body': last_messages[direction]['body'] + u' ' + item['body']
                    }
                else:  # прошло больше 15 минут между однонаправленными сообщениями
                    messages.append({
                        'id': message_id,
                        'out': last_messages[direction]['out'],  # 1, если пишу я / 0 - пишут мне
                        'body': last_messages[direction]['body'],
                        'date': last_messages[direction]['date'],
                    })
                    message_id += 1
                    last_messages[direction] = item

        offset = offset + one_count
        one_count = min(one_count, messages_count - offset)

    # save last messages which wasn't saved in cycle
    for message in last_messages:
        if not message == first_message:
            messages.append({
                'id': message_id,
                'out': message['out'],  # 1, если пишу я / 0 - пишут мне
                'body': message['body'],
                'date': message['date'],
            })
            message_id += 1

    # save to file
    output = open('user_documents.txt', 'w')
    output.write(json.dumps(messages))


if __name__ == '__main__':
    main()
