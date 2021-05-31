import time

from selenium import webdriver

from config.settings import USERNAME, PAROLA, CHROME_PATH, URL

driver = webdriver.Chrome(executable_path=CHROME_PATH)

class TestingLogin():

    def LoginOK(self, username, parola):
        driver.get(URL)

        #user = driver.find_element_by_name("uid")
        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)
        #//input[@name='uid']

        #password = driver.find_element_by_name("password")
        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN PASS")
            else:
                print("TEST CASE LOGIN PASS")
        except:
            print("TEST CASE LOGIN FAILED")

    def LoginNotOK(self, username, parola, testcase):
        driver.get(URL)

        user = driver.find_element_by_xpath("//input[@name='uid']")
        user.send_keys(username)

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys(parola)

        button = driver.find_element_by_name("btnLogin")
        button.click()

        time.sleep(5)

        try:
            actualTitle = driver.title
            print(actualTitle)
            if (actualTitle == "Guru99 Bank Manager HomePage"):
                print("TEST CASE LOGIN " + testcase + " NOT OK FAILED")
            else:
                print("TEST CASE LOGIN " + testcase + " NOT OK PASS")
        except:
            print("TEST CASE LOGIN " + testcase + " NOT OK PASS")



test = TestingLogin()
test.LoginOK(USERNAME, PAROLA)
test.LoginNotOK(USERNAME, "rehavAs-NotOK", "UserOK, PassNotOK")
test.LoginNotOK("user-NotOK", PAROLA, "UserNotOK, PassOK")
test.LoginNotOK("user-NotOK", "rehavAs-NotOK", "UserNotOK, PassNotOK")
test.LoginNotOK("", PAROLA, "UserEmpty, PassOK")
test.LoginNotOK(USERNAME, "", "UserOK, PassEmpty")
test.LoginNotOK("", "", "UserEmpty, PassEmpty")

driver.quit()
