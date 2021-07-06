from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

# s=Service(r"C:\Users\user\PycharmProjects\SecondSeleniumTest\drivers\chromedriver.exe")
# driver = webdriver.Chrome(service=s)
driver = webdriver.Chrome(executable_path=r"C:\Users\user\PycharmProjects\SecondSeleniumTest\drivers\chromedriver.exe")

driver.get("https://www.facebook.com/")

driver.find_element_by_xpath("//*[text()='Create New Account']").click()

time.sleep(5)

driver.find_element(By.NAME, 'firstname').send_keys('ujunwa')
driver.find_element(By.NAME, 'lastname').send_keys('ogugua')
driver.find_element(By.NAME, 'reg_email__').send_keys('uju@yahoo.com')
driver.find_element(By.NAME, 'reg_email_confirmation__').send_keys('uju@yahoo.com')
driver.find_element(By.ID, 'password_step_input').send_keys('passw123')
day = Select(driver.find_element(By.XPATH, "//select[@title='Day']"))
day.select_by_visible_text('20')
month = Select(driver.find_element(By.NAME, 'birthday_month'))
month.select_by_visible_text('Jun')
year = Select(driver.find_element(By.NAME, 'birthday_year'))
year.select_by_visible_text('2000')
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.XPATH, "//button[text()='Sign Up']").click()
