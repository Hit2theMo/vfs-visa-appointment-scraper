import smtplib
import time
from datetime import datetime
from email.message import EmailMessage

import schedule
from selenium import webdriver
from selenium.webdriver.common.by import By

# import os
import config

from_date = '22/02/2023'
to_date = '20/04/2023'


def fetch_latest_appt_date():
    from_date = '22/02/2023'
    to_date = '20/04/2023'
    optimal = False
    driver = webdriver.Chrome()
    driver.get("https://visa.vfsglobal.com/ind/en/deu/login")
    time.sleep(20)
    email = driver.find_element(By.ID, "mat-input-0")
    email.send_keys("mohit.khanwale1@gmail.com")

    password = driver.find_element(By.ID, "mat-input-1")
    password.send_keys(config.VFS_PASSWORD)
    time.sleep(5)
    login = driver.find_element(By.CSS_SELECTOR, ".mat-stroked-button").click()
    time.sleep(5)
    new_booking = driver.find_element(By.CLASS_NAME, "mat-button-wrapper")
    driver.execute_script("arguments[0].click();", new_booking)
    time.sleep(5)

    xpath = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[1]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span"
    visa_application_centre = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", visa_application_centre)
    time.sleep(3)
    xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[3]/span'
    blr_centre = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", blr_centre)
    time.sleep(3)

    xpath = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[2]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span"
    appointment_category = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", appointment_category)
    xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[5]/span'
    schengen_visa = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", schengen_visa)
    time.sleep(3)

    xpath = "/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[3]/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]/span"
    sub_category = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", sub_category)
    xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[12]/span'
    visit_family = driver.find_element(By.XPATH, xpath)
    driver.execute_script("arguments[0].click();", visit_family)
    time.sleep(5)

    xpath = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[1]/form/div[4]/div'
    appointment_date = driver.find_element(By.XPATH, xpath).text
    # appointment_date = "Earliest Available Slot : 22/04/2023"
    appointment_date = (appointment_date.split(":")[1].strip())
    appointment_date_str = appointment_date
    print("Appointment_date-", appointment_date)
    appointment_date = datetime.strptime(appointment_date, '%d/%m/%Y')
    from_date = datetime.strptime(from_date, '%d/%m/%Y')
    to_date = datetime.strptime(to_date, '%d/%m/%Y')

    ##==============================##==============================##==============================##==============================
    if from_date <= appointment_date <= to_date:
        print(f"Appointment date {appointment_date.date()} optimal!")
        optimal = True
    else:
        print(f"Appointment date {appointment_date.date()} outside optimal range :(")

    # xpath = '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button'
    # continue_btn = driver.find_element(By.XPATH, xpath)
    # driver.execute_script("arguments[0].click();", continue_btn)
    # time.sleep(5)
    # ##==============================##==============================##==============================##==============================
    # xpath = '/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[5]/div/div/div/app-input-control/div/mat-form-field/div/div[1]/div[3]/input'
    # first_name = driver.find_element(By.XPATH, xpath).send_keys('MOHIT MILIND')

    # xpath = '/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[6]/div/div/div/app-input-control/div/mat-form-field/div/div[1]/div[3]/input'    
    # last_name = driver.find_element(By.XPATH, xpath).send_keys('KHANWALE')

    # xpath = '/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[7]/div/div[1]/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]'
    # dropdown_gender = driver.find_element(By.XPATH, xpath)
    # driver.execute_script("arguments[0].click();", dropdown_gender)
    # xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[2]/span'
    # male = driver.find_element(By.XPATH, xpath)
    # driver.execute_script("arguments[0].click();", male)
    # # xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[1]/span'
    # # female = driver.find_element(By.XPATH, xpath)

    # xpath = '/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[7]/div/div[2]/div/app-ngb-datepicker/div/div[2]/input'
    # dob = driver.find_element(By.XPATH, xpath).send_keys('10101998')
    # xpath = '/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[9]/div/div[2]/div/app-ngb-datepicker/div/div[2]/input'
    # pp_expiry = driver.find_element(By.XPATH, xpath).send_keys('26012033')
    # try:
    #     xpath = '/html/body/app-root/div/app-applicant-details/section/mat-card[1]/form/app-dynamic-form/div/div/app-dynamic-control[8]/div/div/div/app-dropdown/div/mat-form-field/div/div[1]/div[3]/mat-select/div/div[1]'
    #     dropdown_cntry = driver.find_element(By.XPATH, xpath)
    #     driver.execute_script("arguments[0].click();", dropdown_cntry)
    #     time.sleep(2)
    #     xpath = '/html/body/div[5]/div[2]/div/div/div/mat-option[93]/span'
    #     india = driver.find_element(By.XPATH, xpath)
    #     driver.execute_script("arguments[0].click();", india)
    # except Exception as e:
    #     print(e)
    #     pass
    
    # time.sleep(300)
    driver.quit()
    return appointment_date_str, optimal


def send_email(message):
    EMAIL_ID = config.EMAIL_ID
    EMAIL_PASSWORD = config.EMAIL_PASSWORD 
    msg = EmailMessage()
    msg['Subject'] = 'VFS Latest Appointment Date'
    msg['From'] = EMAIL_ID
    msg['To'] = EMAIL_ID
    msg.set_content(message)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ID, EMAIL_PASSWORD)
        smtp.send_message(msg)


def main():
    appointment_date, optimal = fetch_latest_appt_date()
    # appointment_date = "Earliest Available Slot : 08/05/2023"
    print(f"{datetime.now()}: {appointment_date}")
    send_email(appointment_date)
    

# schedule.every(15).minutes.do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(60)  # wait one minute

main()