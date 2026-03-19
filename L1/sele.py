import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.quit()


class InputTesting(TestCase):
    BLOG_URL = (
        "https://login.pwr.edu.pl/auth/realms/pwr.edu.pl/protocol/cas/login?service=https%3A%2F%2Fweb.usos.pwr.edu.pl%2Fkontroler.php%3F_action%3Dlogowaniecas%2Findex%26callback%3DK7YyNrVS0s%252FOzyspys9JLdIryCiwj09MLsnMz7PNSy0v1k9JTUsszSlRsgYA3337cee5a350ca4443a95607dcb84a09568b90c1&locale=pl"
    )
    INPUT_NAME = "username"
    CLEAR_BUTTON_ID = "clearForm"

    def _get_login_input(self):
        try:
            return self.driver.find_element(by=By.NAME, value=self.INPUT_NAME)
        except Exception:
            self.fail("Login input not found!")

    def test_input_value(self):
        self.driver.get(self.BLOG_URL)
        login_box = self._get_login_input()
        login_box.send_keys("your_username")

        input_value = login_box.get_attribute("value")
        self.assertEqual("your_username", input_value)

    def test_clear_button_functionality(self):
        self.driver.get(self.BLOG_URL)
        login_box = self._get_login_input()
        login_box.send_keys("test_user")

        try:
            clear_button = self.driver.find_element(by=By.ID, value=self.CLEAR_BUTTON_ID)
            clear_button.click()
        except Exception:
             self.fail(f"Clear button with ID '{self.CLEAR_BUTTON_ID}' not found!")

        input_value = login_box.get_attribute("value")
        self.assertEqual("", input_value, "Pole nie zostało wyczyszczone!")


if __name__ == "__main__":
    unittest.main()
