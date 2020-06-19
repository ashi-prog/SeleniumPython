from Base import InitiateDriver
from Library import ConfigReader

def test_invalidRegistration():
    driver = InitiateDriver.startBrowser()
    driver.find_element_by_name(ConfigReader.fetchElementLocators("Registration","password_name")).send_keys("1234")