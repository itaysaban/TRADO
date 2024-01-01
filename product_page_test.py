import time
import unittest
from log_in_test import log_in
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from driver_set_up import driver_set_up

class Testcase(unittest.TestCase):

    def setUp(self):
        self.driver = driver_set_up()
        self.driver.get('http://qa.trado.ai/')
        log_in(self.driver)
        go_to_products = WebDriverWait(self.driver, 10).until((EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[9]/div/a/div'))))
        go_to_products.click()

    def tearDown(self):
        self.driver.close()

    def test1_arrows(self):

        go_left = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[2]')))
        go_left.click()
        time.sleep(2)

        go_right = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div/div/div/div/div[1]/div/div[2]/div[1]/span/i')))
        go_right.click()

    def test2_items_in_importing(self):

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[2]/div/div[2]/div[2]/div[3]',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[3]/div/div[2]/div[2]/div[2]/div']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test3_items_in_PM(self):

        go_to_PM = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[10]/div/a/div')))
        go_to_PM.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div/div[2]/div[2]/div[1]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test4_items_in_zxczxczx(self):

        go_to_zxc = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[11]/div/a/div')))
        go_to_zxc.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div/div[2]/div[2]/div[1]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test5_items_in_beers(self):

        go_to_beers = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[12]/div/a/div')))
        go_to_beers.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[2]/div/div[2]/div[2]/div[3]',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[3]/div/div[2]/div[2]/div[3]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()


    def test6_items_in_snacks(self):

        go_to_snacks = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[13]/div/a/div')))
        go_to_snacks.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div/div[2]/div[2]/div[3]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test7_go_to_kanabis(self):

        go_to_kanabis = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[14]/div/a/div')))
        go_to_kanabis.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[1]/div/div[2]/div[2]/div[2]/div',
                 '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a[2]/div/div[2]/div[2]/div[3]']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()

    def test7_go_to_wagwan(self):

        go_to_wagwan = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[15]/div/a/div')))
        go_to_wagwan.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until( EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()


    def test7_go_to_drinks(self):

        go_to_drinks = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/ul/li[16]/div/a/div')))
        go_to_drinks.click()

        items = ['//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/div[1]/div[3]/a/div']

        wait = WebDriverWait(self.driver, 10)

        for item in items:
            try:
                element = wait.until(EC.element_to_be_clickable((By.XPATH, item)))
                element.click()
                print(f"Clicked on element: {item}")
                item_add = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'micon-plus icon_icon '))).click()
                time.sleep(1)
                item_remove = wait.until( EC.element_to_be_clickable((By.CLASS_NAME, 'micon-minus icon_icon '))).click()
                time.sleep(1)

                # Perform some checks or actions on the new page if needed

            except TimeoutException:
                print(f"Element {item} not found or not clickable within the specified time.")

            # Navigate back to the main page after each click
            self.driver.back()



