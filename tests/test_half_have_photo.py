import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import testing, test_show_my_pets


def test_half_pets_have_photo(test_show_my_pets):
    """Поверяем что хотя бы у половины питомцев есть фото"""

    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Получаем количество питомцев
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
    number = len(pets)

    # Нахождение половины от количества питомцев
    half = number // 2

    # Сохранение элементов с атрибутом "img" в переменную "images"
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Нахождение количества питомцев с фотографией
    number_of_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_of_photos += 1

    # Проверка того, что количество питомцев с фотографией больше или равно половине количества питомцев
    try:
        assert number_of_photos >= half
        print('Хотя бы у половины питомцев есть фото')
    except:
        raise Exception('Более чем у половины питомцев отсутствуют фотографии')
