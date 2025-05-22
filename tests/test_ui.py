import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_addition():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/calculator.html")

    input1 = driver.find_element(By.ID, "input1")
    input1.clear()
    input1.send_keys("1")

    input2 = driver.find_element(By.ID, "input2")
    input2.clear()
    input2.send_keys("4")

    input3 = driver.find_element(By.ID, "input3")
    input3.clear()
    input3.send_keys("5")

    driver.find_element(By.ID, "add-btn").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    assert result == "10"

    driver.quit()



def test_subtraction():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/calculator.html")

    input1 = driver.find_element(By.ID, "input1")
    input1.clear()
    input1.send_keys("5")

    input2 = driver.find_element(By.ID, "input2")
    input2.clear()
    input2.send_keys("3")

    input3 = driver.find_element(By.ID, "input3")
    input3.clear()
    input3.send_keys("2")

    driver.find_element(By.ID, "subtract-btn").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    assert result == "0"

    driver.quit()



def test_multiplication():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/calculator.html")

    input1 = driver.find_element(By.ID, "input1")
    input1.clear()
    input1.send_keys("1")

    input2 = driver.find_element(By.ID, "input2")
    input2.clear()
    input2.send_keys("4")

    input3 = driver.find_element(By.ID, "input3")
    input3.clear()
    input3.send_keys("5")

    driver.find_element(By.ID, "multiply-btn").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    assert result == "20"

    driver.quit()



def test_division():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/calculator.html")

    input1 = driver.find_element(By.ID, "input1")
    input1.clear()
    input1.send_keys("1")

    input2 = driver.find_element(By.ID, "input2")
    input2.clear()
    input2.send_keys("4")

    input3 = driver.find_element(By.ID, "input3")
    input3.clear()
    input3.send_keys("5")

    driver.find_element(By.ID, "divide-btn").click()
    time.sleep(1)

    result = driver.find_element(By.ID, "result").text
    rounded_result = round(float(result), 2)
    assert rounded_result == 0.05

    driver.quit()


    driver.quit()