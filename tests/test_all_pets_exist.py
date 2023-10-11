import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import testing, test_show_my_pets


def test_pets_exist(test_show_my_pets):
    """ Проверяем что присутствуют все питомцы """

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # Сохранение элементов статистики
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Получение количества питомцев
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Получение количества карточек питомцев
    number_pets = len(pets)

    # Проверка того, что количество питомцев из статистики совпадает с количеством карточек питомцев
    assert number == number_pets
