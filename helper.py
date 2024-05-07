import requests
import random
import string

import data
import urls


# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
class CourierFactory:
    @staticmethod
    def register_new_courier_and_return_login_password():
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload


class ChangeTestDataHelper:
    @staticmethod
    def modify_payload_body(key, value):
        body = data.TestDataCreateOrder.CREATE_ORDER_BODY_PARAM.copy()
        body[key] = [value]
        return body
