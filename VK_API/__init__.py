# coding=utf-8
__author__ = 'stdimitriev@mail.ru'

import vk
import vk_api
import json


def main():
    client_id = '5043521'
    token = 'ce6bf477ce6bf477ceebb0964ece270136cce6bce6bf4779bb1c38045417272d8af6faa'

    login = 'ukchuvrus@mail.ru'
    password = '' # need password

    user_id = 5403120

    # vkapi = vk.API(client_id, 'ukchuvrus@mail.ru', '')
    # vkapi.access_token = token
    # vkapi.wall.post(message="Hello, world")

    vkk = vk_api.VkApi(login, password)

    try:
        vkk.authorization()
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

    file = open('user_dialog.txt', 'w')

    messages = []

    first_values = {
        'count': 0,
        'user_id': user_id
    }
    response = vkk.method('messages.getHistory', first_values)
    messages_count = 0
    if response:
        messages_count = response['count']
    else:
        return

    one_count = 200
    offset = 0
    while one_count > 0:
        values = {
            'user_id': user_id,
            'count': one_count,
            'offset': offset,
            'rev': 1  # в хронологическом порядке / 0 - с конца
        }
        response = vkk.method('messages.getHistory', values)

        if response['items']:
            for i, item in enumerate(response['items']):
                messages.append({
                    'id': i,
                    'out': item['out'],  # 1, если пишу я / 0 - пишут мне
                    'text': item['body'],
                    'date': item['date'],
                })

            offset = offset + one_count
            one_count = min(one_count, messages_count - offset)
            file.write(json.dumps(messages))
        else:
            print('Нет ответа')


if __name__ == '__main__':
    main()
