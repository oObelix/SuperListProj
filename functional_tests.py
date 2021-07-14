from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    """тест нового посетителя"""

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """тест: можно начать список и получить его позже"""

        # Заходим на домашнюю страницу неотложного списка
        self.browser.get("http://localhost:8000")

        # Мы видим в заголовке браузера, что находимся в приложении списка
        # неотложных дел
        assert "To-Do" in self.browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Нам сразу же предлагается ввести элемент списка
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Мы набираем втекстовом поле "Купить автомобиль"
        input_box.send_keys('Купить автомобиль')

        # Когда нажимаем Enter, страница обновляется, и теперь страница
        # содержит: "1. Купить автомобиль" в качестве элемента списка
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Купить автомобиль' for row in rows)
        )

        # Текстовое поле попрежнему ожидает ввод элемента списка

        # Мы вводим "Купить мотоцикл"
        self.fail('Закончить тест!')

        # Когда нажимаем Enter, страница обновляется, и теперь страница
        # отображает оба введённых элемента списка

        # Нам интересно запомнит ли приложение наш список. Мы видим, что сайт
        # сгенерировал нам уникальный URL-адрес страницы - об этом нам говорит
        # небольшой текст с объяснениями

        # Мы посещаем этот URL-адрес и убеждаемся, что список ещё там


if __name__ == "__main__":
    unittest.main(warnings="ignore")
