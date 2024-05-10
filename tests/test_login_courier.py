import allure
import json
from api.courier_api import CourierApi
import data



class TestLoginCourier:
    @allure.title("Проверка успешной авторизации")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа. Авторизация, удаление.")
    def test_success_login_courier(self, create_creds_courier):
        CourierApi.create_courier(create_creds_courier)
        auth_request = CourierApi.auth(create_creds_courier)
        courier_id = auth_request.json()["id"]
        CourierApi.delete_courier(courier_id)
        assert auth_request.status_code == 200 and courier_id is not None and courier_id > 0


    @allure.title("Проверка авторизации с пустыми данными")
    @allure.description("Авторизация с пустыми данными")
    def test_login_empty_payload_courier(self):
        created_courier_request = CourierApi.auth(data.TestDataCreateCourier.CREATE_COURIER_BODY)
        assert (created_courier_request.status_code == 400 and created_courier_request.json()["message"] == data.LOGIN_EMPTY_COURIER)

    @allure.title("Проверка авторизации c несуществующим пользователем")
    @allure.description("Авторизации c несуществующим пользователем, запрос возвращает ошибку")
    def test_login_nonexistent_courier(self,create_creds_courier):
        created_courier_request = CourierApi.auth(create_creds_courier)
        assert (created_courier_request.status_code == 404 and created_courier_request.json()[
            "message"] == data.LOGIN_NONEXISTENT_COURIER)

