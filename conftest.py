import pytest
import helper
from helper import CourierFactory
import allure


@allure.step("Создание рандомного курьера")
@pytest.fixture(scope='function')
def create_creds_courier():
    creds = helper.CourierFactory.register_new_courier_and_return_login_password()
    return creds
