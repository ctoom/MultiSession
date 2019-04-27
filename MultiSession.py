from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from threading import Thread
from colorama import Fore, Back, Style
from colorama import init
from pyfiglet import figlet_format


#TODO Add threading support
#TODO Monitor for changes


print(figlet_format(('rTunaboss'), font='big'))

init(autoreset=True)



url = input("\nEnter the url:\t")

instances = int(input("\nHow many instances?\t"))

def set_options():
    # Initialize the webdriver
    chrome_options = Options()
    chrome_options.add_argument("--window-size=400,600")
    return chrome_options

def initialize_driver(options, url):
    driver = webdriver.Chrome(executable_path="/Users/arturhnat/Desktop/Coding/WebDrivers/chromedriver", options=options)
    driver.get(url)


options = set_options()

for i in range(instances):
    initialize_driver(options=options, url=url)
    print(Fore.GREEN + f"\nDriver n.{i+1} has been started.")


while True:
    q = input(Fore.RED + "Enter 'Q' to exit")
    if q.lower() == "q":
        print("\nExiting...")
        break
