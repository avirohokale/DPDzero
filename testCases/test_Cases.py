import time

from PageObject.TaskObject import Task
from utilities.Logger import LogGen


class Test_URL:
    new_task = 'abcd'
    date = '07/08/2023'
    log = LogGen.loggen()

    # A. Test case for loading the app
    # 1) Verify that the Simple To-Do App loads successfully and displays the initial user interface without errors.
    def test_url_01(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")
        time.sleep(2)

        if self.driver.title == 'todo-app-2':
            self.log.info("test_url_01 is Passed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_url_01_pass.png")
            assert True
        else:
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_url_01_fail.png")
            self.log.info("test_url_01 is Failed ")
            assert False

    # B. Test case for input validation
    # 2) Verify that the 'New Task' input box is enabled.
    def test_box_enable_02(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")

        if self.driver.find_element(*Task.text_ip_box_task_Xpath).is_enabled():
            self.log.info("test_box_enable_02 is Passed ")
            assert True
        else:
            self.log.info("test_box_enable_02 is Failed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_box_enable_02_fail.png")
            assert False

    # B. Test case for input validation
    # 3) Verify that the 'Date' input box is enabled.
    def test_date_box_enable_03(self, setup):
        self.driver = setup
        if self.driver.find_element(*Task.cal_ip_box_Xpath).is_enabled():
            self.log.info("test_date_box_enable_03 is Passed ")
            assert True
        else:
            self.log.info("test_date_box_enable_03 is Passed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_date_box_enable_03_fail.png")
            assert False

    # C. Test case for adding a task
    # 4) Verify that the 'Add Task' Button without any input is disabled.
    def test_add_task_disable_without_ip_04(self, setup):  # 3)Test case for adding a task
        self.driver = setup
        if self.driver.find_element(*Task.add_task_button_Xpath).is_enabled():
            self.log.info("test_add_task_disable_without_ip_04 is Passed ")
            assert False
        else:
            self.log.info("test_add_task_disable_without_ip_04 is Failed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_add_task_disable_without_ip_04_fail.png")
            assert True

    # C. Test case for adding a task
    # 5) Verify that the after task is added count is increased by one.
    def test_adding_task_05(self, setup):
        self.driver = setup
        self.to = Task(self.driver)
        self.log.info("Counting list of task before adding task")
        initial_task_count = len(self.to.task_list())

        self.log.info("Adding Task " + self.new_task)
        self.to.enter_task(self.new_task)
        self.log.info("Adding date " + self.new_task)
        self.to.enter_date(self.date)
        self.to.click_add_task_button()

        self.log.info("Counting list of task before adding task")
        updated_task_count = len(self.to.task_list())

        if updated_task_count == initial_task_count + 1:
            self.log.info("test_adding_task_05 is Passed ")
            assert True
        else:
            self.log.info("test_adding_task_05 is Failed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_adding_task_05_fail.png")
            assert False

    # D. Test case for marking a task as done
    # 6) Verify that the task marking as done
    def test_mark_task_done_06(self, setup):
        self.driver = setup
        self.to = Task(self.driver)
        self.to.enter_task(self.new_task)
        self.to.enter_date(self.date)
        self.to.click_add_task_button()
        self.to.click_done_button()

        done_button = self.driver.find_element(*Task.done_button_Xpath)
        if done_button.get_attribute('innerHTML') == 'Not done':
            self.log.info("test_mark_task_done_06 is Passed ")
            assert True
        else:
            self.log.info("test_mark_task_done_06 is Failed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_mark_task_done_06_fail.png")
            assert False

    # E. Test case for deleting a task
    # 7) Verify that the after task is delete count is decreased by one.
    def test_delete_task_07(self, setup):
        self.driver = setup
        self.to = Task(self.driver)
        self.to.enter_task(self.new_task)
        self.to.enter_date(self.date)
        self.to.click_add_task_button()
        before_delete_task_count = len(self.to.task_list())

        self.to.click_delete_button()
        after_delete_task_count = len(self.to.task_list())

        if after_delete_task_count == before_delete_task_count - 1:
            self.log.info("test_delete_task_07 is Failed ")
            assert True
        else:
            self.log.info("test_delete_task_07 is Failed ")
            self.driver.save_screenshot("D:\\Avinash\\Testing\\Automation\\Practice\\DPDzero\\ScreenShot\\test_delete_task_07_fail.png")
            assert False
