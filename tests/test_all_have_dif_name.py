import pytest
from selenium.webdriver.common.by import By
from conftest import testing, test_show_my_pets


def test_all_have_dif_name(test_show_my_pets):
    """Проверяем что у всех питомцев разные имена"""

    pytest.driver.implicitly_wait(10)

    # Сохранение элементов с данными о питомцах в переменную "pet_data"
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Создаем список с именами питомцев
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Перебираются имена и, если имя повторяется, к счетчику "r" прибавляется единица
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    # Если r == 0, то повторяющихся имен нет
    assert r == 0
