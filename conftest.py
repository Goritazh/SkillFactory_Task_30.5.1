import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(driver_path)

    # Переход на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()


@pytest.fixture()
def test_show_my_pets():
    # Явное ожидание
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.ID, 'email')))

    # Ввод эл. почты
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)

    # Ввод пароля
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)

    # Клик по кнопе "Войти"
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Проверяем что мы на главной странице
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Переходим на страницу с питомцами пользователя
    pytest.driver.get('https://petfriends.skillfactory.ru/my_pets')
