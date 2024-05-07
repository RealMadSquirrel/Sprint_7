import allure
import requests
import data
import urls


class CourierApi:
    @staticmethod
    @allure.step("Авторизация")
    def auth(creds):
        return requests.post(urls.BASE_URL + urls.AUTH_ENDPOINT, json=creds)

    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса на удаление курьера")
    def delete_courier(courier_id):
        return requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(courier_id))