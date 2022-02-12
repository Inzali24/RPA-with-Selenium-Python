import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

txtData = []
with open('oat.txt') as f:
    lines = f.readlines()
    for l in lines:
        txtData.append(l)

    driver = webdriver.Chrome(ChromeDriverManager().install())  # Chromeを起動
    driver.maximize_window()
    driver.get("https://operation-analysis-tool.herokuapp.com/")
    time.sleep(3)
    driver.find_element_by_class_name("input_inputData__3gK-e").send_keys(txtData)
    time.sleep(3)
print("sample test case sucessfully completed")