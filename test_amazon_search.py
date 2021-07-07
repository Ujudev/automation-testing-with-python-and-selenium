from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def test_amazon_search():
    driver = webdriver.Chrome()
    driver.get('https://www.amazon.com/')
    driver.maximize_window()
    driver.implicitly_wait(5)

    search = driver.find_element_by_id('twotabsearchtextbox')
    search.send_keys('dress', Keys.ENTER)

    expected_text = '"dress"'
    actual_text = driver.find_element_by_xpath("//span[@class='a-color-state a-text-bold']").text
    assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual text: {actual_text}'

    driver.quit()


