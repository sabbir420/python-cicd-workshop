import my_app
import unittest

class TestMyApp(unittest.TestCase):

    def setUp(self):
        self.app = my_app.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'Welcome to CI/CD 101 using CircleCI!'
        self.assertEqual(my_app.greet(), greeting)

if __name__ == '__main__':
    unittest.main()