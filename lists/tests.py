from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class SmokeTest(TestCase):
    """тест на токсичность"""

    def test_root_url_resolves_to_home_page_view(self):
        """тест: корневой URL преобразуется в представление
        домашней страницы"""

        found = resolve("/")
        self.assertEqual(found.func, home_page)

    # def test_bad_maths(self):
    #     """тест на неправильные математические расчёты"""
    #     self.assertEqual(1 + 1, 3)
