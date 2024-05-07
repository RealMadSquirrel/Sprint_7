import allure
from api.courier_api import CourierApi
import data
from helper import CourierFactory


class TestCreateCourier:
    @allure.title("Проверка успешности создания курьера")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа и тела ответа")
    def test_success_create_courier(self):
        created_courier_request = CourierApi.create_courier(CourierFactory.register_new_courier_and_return_login_password())
        assert (created_courier_request.status_code == 201 and created_courier_request.text == '{"ok":true}')

    @allure.title("Проверка невозможности создать двух одинаковых курьеров")
    @allure.description("Запоминаем креды. Создаем курьера и пытаемся создать курьера с такими же кредами.")
    def test_create_courier_duplicate(self):
        creds = CourierFactory.register_new_courier_and_return_login_password()
        CourierApi.create_courier(creds)
        created_courier_request_2 = CourierApi.create_courier(creds)
        assert (created_courier_request_2.status_code == 409 and created_courier_request_2.json()["message"] == 'Этот логин уже используется. Попробуйте другой.')

    @allure.title("Проверка, что нельзя создать курьера с пустыми данными.")
    @allure.description("Проверка, что нельзя создать курьера с пустыми данными.")
    def test_create_courier_with_empty_load(self):
        created_courier_request = CourierApi.create_courier(data.TestDataCreateCourier.CREATE_COURIER_BODY)
        assert (created_courier_request.status_code == 400 and created_courier_request.json()["message"] == 'Недостаточно данных для создания учетной записи')

