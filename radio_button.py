import time

from selenium import webdriver

from config.settings import CHROME_PATH, URL

driver = webdriver.Chrome(executable_path=CHROME_PATH)

class TestingRadioButton():

    def radiobutton(self):

        driver.get(URL)

        radio = driver.find_elements_by_xpath("//input[@type='radio']")

        radio[0].click()
        time.sleep(3)

        radio[1].click()
        time.sleep(3)

        radio[2].click()
        time.sleep(3)

        print("Am ajuns aici")

    def checkbox(self):
        driver.get(URL)

        checkbox = driver.find_elements_by_xpath("//input[@type='checkbox']")

        for x in checkbox:
            isSelected = x.is_selected()
                if isSelected:
                print("checkbox just selected")
            else:
                x.click()
                print("checkbox just selected")
                time.sleep(3)

test = TestingRadioButton()
test.radiobutton()
test.checkbox()
driver.quit()