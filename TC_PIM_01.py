import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ORANGEHRM_Forgot_link(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_orangeHRM_forgot_password(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(5)

        username_field = self.driver.find_element(By.XPATH,"//input[@name='username']")
        username_field.send_keys("Admin")
        time.sleep(2)

        forgot_password_link=self.driver.find_element(By.XPATH,"//*[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")
        forgot_password_link.click()
        time.sleep(5)


        username=self.driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']")
        username.click()
        username.send_keys("Admin")
        time.sleep(2)

        reset_password_button=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        reset_password_button.click()
        time.sleep(2)

        def tearDown(self):
            self.driver.quit()

if __name__ == "__main__":
        unittest.main()
