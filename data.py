import pytest
import urls


class TestDataCreateCourier:
    CREATE_COURIER_BODY = {
        "login": "",
        "password": "",
        "firstName": ""
    }


class TestDataCreateOrder:
    CREATE_ORDER_BODY_PARAM = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }

SUCCESS_CREATE_COURIER = '{"ok":true}'
DOUBLE_COURIER = 'Этот логин уже используется. Попробуйте другой.'
EMPTY_COURIER = 'Недостаточно данных для создания учетной записи'
LOGIN_EMPTY_COURIER = 'Недостаточно данных для входа'
LOGIN_NONEXISTENT_COURIER = 'Учетная запись не найдена'