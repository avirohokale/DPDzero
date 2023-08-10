from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Task:
    text_ip_box_task_Xpath = (By.XPATH, '//input[@type="text"]')
    cal_ip_box_Xpath = (By.XPATH, "//input[@placeholder='Deadline']")
    add_task_button_Xpath = (By.XPATH, '//button[@class="add-task-button"]')
    done_button_Xpath = (By.XPATH, "//li[1]//button[1]")
    delete_button_Xpath = (By.XPATH, "//li[1]//button[2]")
    mark_all_button_Xpath = (By.XPATH, "//button[contains(text(),'Mark all done')]")
    task_list_Xpath = (By.XPATH, "//div[@id='app']//ul//li")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def enter_task(self, new_task):
        self.wait.until(expected_conditions.presence_of_element_located(self.text_ip_box_task_Xpath))
        self.driver.find_element(*Task.text_ip_box_task_Xpath).send_keys(new_task)

    def enter_date(self, date):
        self.wait.until(expected_conditions.presence_of_element_located(self.cal_ip_box_Xpath))
        self.driver.find_element(*Task.cal_ip_box_Xpath).send_keys(date)

    def click_add_task_button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.add_task_button_Xpath))
        self.driver.find_element(*Task.add_task_button_Xpath).click()

    def click_done_button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.done_button_Xpath))
        self.driver.find_element(*Task.done_button_Xpath).click()

    def click_mark_all_Button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.mark_all_button_Xpath))
        self.driver.find_element(*Task.mark_all_button_Xpath).click()

    def mark_all_Button_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.mark_all_button_Xpath))
            self.driver.find_element(*Task.mark_all_button_Xpath)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def click_delete_button(self):
        self.wait.until(expected_conditions.presence_of_element_located(self.delete_button_Xpath))
        self.driver.find_element(*Task.delete_button_Xpath).click()

    def delete_button_status(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located(self.delete_button_Xpath))
            self.driver.find_element(*Task.delete_button_Xpath)
            return True
        except (NoSuchElementException, TimeoutException):
            return False

    def task_list(self):
        task_list = self.driver.find_elements(*Task.task_list_Xpath)
        return task_list
