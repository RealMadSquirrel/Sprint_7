import allure
import requests
import data
import urls


class OrderApi:
    @staticmethod
    @allure.step("Отправка запроса на создание заказа")
    def create_order(body):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)

    @staticmethod
    @allure.step("Отправка запроса получение списка заказов")
    def get_list_order():
        return requests.get(urls.BASE_URL + urls.LIST_ORDER_ENDPOINT)


