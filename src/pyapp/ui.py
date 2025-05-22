from selenium.webdriver.common.by import By

def enter_numbers(driver, n1, n2, n3):
    driver.find_element(By.ID, "input1").send_keys(str(n1))
    driver.find_element(By.ID, "input2").send_keys(str(n2))
    driver.find_element(By.ID, "input3").send_keys(str(n3))

def click_add(driver):
    driver.find_element(By.ID, "add-btn").click()

def click_subtract(driver):
    driver.find_element(By.ID, "subtract-btn").click()

def click_multiply(driver):
    driver.find_element(By.ID, "multiply-btn").click()

def click_divide(driver):
    driver.find_element(By.ID, "divide-btn").click()

def get_result_text(driver):
    return driver.find_element(By.ID, "result").text


