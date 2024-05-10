import allure
import json
from api.order_api import OrderApi
import data
from helper import CourierFactory
from helper import ChangeTestDataHelper
import pytest


class TestOrder:
    @allure.title("Проверка успешности создания заказа с разными параметрами в поле color")
    @pytest.mark.parametrize("color", [
        pytest.param("BLACK"),
        pytest.param("GREY"),
        pytest.param(["BLACK", "GREY"]),
        pytest.param(" ")
    ])
    def test_success_create_order(self, color):
        payload = ChangeTestDataHelper.modify_payload_body("color", color)
        created_order_request = OrderApi.create_order(payload)
        order_id = created_order_request.json()["track"]
        assert created_order_request.status_code == 201 and order_id is not None and order_id > 0

    @allure.title("Проверка получения списка товаров")
    def test_success_list_order(self):
        list_order_request = OrderApi.get_list_order()
        assert list_order_request.status_code == 200 and list_order_request.json()["orders"] != []
