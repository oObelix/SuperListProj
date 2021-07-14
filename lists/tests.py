# from django.urls import resolve
from django.test import TestCase
# from django.http import HttpRequest

# from lists.views import home_page


class HomePageTest(TestCase):
    """тест домашней страницы"""

    def test_uses_home_template(self):
        """тест: используется шаблон home.html"""

        # request = HttpRequest()
        # response = home_page(request)
        response = self.client.get('/')

        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<!DOCTYPE html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')
