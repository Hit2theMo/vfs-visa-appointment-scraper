"""
Create a python web scraper which logs in to https://visa.vfsglobal.com/ind/en/deu/login using the below credentials-
email- mohit.khanwale1@gmail.com
password- Clouds@911
and then click on "Start New Booking"
and then find the Earliest Available Slot for-
    1. Visa Application Centre- Bangalore - Visa Application Centre
    2. appointment category - Schengen Visa (stay of max. 90 days or less)
    3. sub-category- visit (family & Friends)
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://visa.vfsglobal.com/ind/en/deu/login")
time.sleep(5)
email = driver.find_element(By.ID, "mat-input-0")
email.send_keys("mohit.khanwale1@gmail.com")

password = driver.find_element(By.ID, "mat-input-1")
password.send_keys("Clouds@911")
time.sleep(5)
login = driver.find_element(By.CSS_SELECTOR, ".mat-stroked-button").click()
time.sleep(6)
new_booking = driver.find_element(By.CLASS_NAME, "mat-button-wrapper")
driver.execute_script("arguments[0].click();", new_booking)
time.sleep(7)

xpath = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span"
visa_application_centre = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", visa_application_centre)
time.sleep(6)
xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[3]/span'
blr_centre = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", blr_centre)
time.sleep(6)

xpath = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span"
appointment_category = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", appointment_category)
xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[5]/span'
schengen_visa = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", schengen_visa)
time.sleep(6)

xpath = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span"
sub_category = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", sub_category)
xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[12]/span'
visit_family = driver.find_element(By.XPATH, xpath)
driver.execute_script("arguments[0].click();", visit_family)
time.sleep(7)

xpath = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]/div'
appointment_date = driver.find_element(By.XPATH, xpath).text
print("appointment_date-", appointment_date)

# try:
#     element_present = EC.presence_of_element_located((By.ID, 'calendar'))
#     WebDriverWait(driver, 10).until(element_present)
#     print("Page is ready!")
# except TimeoutException:
#     print("Loading took too much time!")

# calendar = driver.find_element(By.ID, "calendar")

# calendar_dates = calendar.find_elements_by_tag_name("td")

# for date in calendar_dates:
#     if date.text == "":
#         date.click()
#         break


# driver.quit()
