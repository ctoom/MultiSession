from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading


url = input("What is the url: ")
i = int(input("how many instances?"))
for _ in range(i):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=400,600")
    driver = webdriver.Chrome(executable_path="/Users/arturhnat/Desktop/Coding/WebDrivers/chromedriver", chrome_options=chrome_options)
    driver.get(url)

while True:
    close = input("Press 'q' when done:\t")
    if close.lower() == "q":
        driver.quit()
        break