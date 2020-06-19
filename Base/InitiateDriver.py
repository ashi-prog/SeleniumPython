from selenium.webdriver import Chrome
from Library import ConfigReader
def startBrowser():
    global driver
    path = "C:\\Users\\milin\\PycharmProjects\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get(ConfigReader.readConfigData('Registration','email_name'))
    driver.maximize_window()
    return driver
def closeBrowser():
    driver.close()
