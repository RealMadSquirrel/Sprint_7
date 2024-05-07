import allure
import json
from api.courier_api import CourierApi
import data
from helper import CourierFactory


class TestLoginCourier:
    @allure.title("Проверка успешной авторизации")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа. Авторизация, удаление.")
    def test_success_login_courier(self):
        creds = CourierFactory.register_new_courier_and_return_login_password()
        created_courier_request = CourierApi.create_courier(creds)
        if created_courier_request.status_code == 201:
            auth_request = CourierApi.auth(creds)
            courier_id = auth_request.json()["id"]
            CourierApi.delete_courier(courier_id)
            assert auth_request.status_code == 200 and courier_id is not None and courier_id > 0


    @allure.title("Проверка авторизации с пустыми данными")
    @allure.description("Авторизация с пустыми данными")
    def test_login_empty_payload_courier(self):
        created_courier_request = CourierApi.auth(data.TestDataCreateCourier.CREATE_COURIER_BODY)
        assert (created_courier_request.status_code == 400 and created_courier_request.json()["message"] == 'Недостаточно данных для входа')

    @allure.title("Проверка авторизации c несуществующим пользователем")
    @allure.description("Авторизации c несуществующим пользователем, запрос возвращает ошибку")
    def test_login_nonexistent_courier(self):
        created_courier_request = CourierApi.auth(CourierFactory.register_new_courier_and_return_login_password())
        assert (created_courier_request.status_code == 404 and created_courier_request.json()[
            "message"] == 'Учетная запись не найдена')

