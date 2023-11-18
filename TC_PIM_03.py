import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ORANGEHRM_Admin_page(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_ORANGEHRM_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(2)

        Username_box=self.driver.find_element(By.NAME,"username")
        Username_box.send_keys("Admin")
        time.sleep(2)

        password_box=self.driver.find_element(By.NAME,"password")
        password_box.send_keys("admin123")
        time.sleep(2)

        login_button=self.driver.find_element(By.XPATH,"//button[@type='submit']")
        login_button.click()
        time.sleep(2)

        admin_click=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
        admin_click.click()
        time.sleep(2)

        goto_mainmenu=self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/div/div/button")
        goto_mainmenu.click()
        time.sleep(2)

        self.driver.quit()

        def tearDown(self):
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
