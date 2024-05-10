import allure
from api.courier_api import CourierApi
import data



class TestCreateCourier:
    @allure.title("Проверка успешности создания курьера")
    @allure.description("Создание шаблонного курьера, проверка статуса ответа и тела ответа")
    def test_success_create_courier(self, create_creds_courier):
        created_courier_request = CourierApi.create_courier(create_creds_courier)
        assert (created_courier_request.status_code == 201 and created_courier_request.text == data.SUCCESS_CREATE_COURIER)

    @allure.title("Проверка невозможности создать двух одинаковых курьеров")
    @allure.description("Запоминаем креды. Создаем курьера и пытаемся создать курьера с такими же кредами.")
    def test_create_courier_duplicate(self, create_creds_courier):
        CourierApi.create_courier(create_creds_courier)
        created_courier_request_2 = CourierApi.create_courier(create_creds_courier)
        assert (created_courier_request_2.status_code == 409 and created_courier_request_2.json()["message"] == data.DOUBLE_COURIER)

    @allure.title("Проверка, что нельзя создать курьера с пустыми данными.")
    @allure.description("Проверка, что нельзя создать курьера с пустыми данными.")
    def test_create_courier_with_empty_load(self):
        created_courier_request = CourierApi.create_courier(data.TestDataCreateCourier.CREATE_COURIER_BODY)
        assert (created_courier_request.status_code == 400 and created_courier_request.json()["message"] == data.EMPTY_COURIER)

