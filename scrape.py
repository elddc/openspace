# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# config, used for both scraping methods
base = "https://uiuc.libcal.com/"
all = "allspaces" # base + all
id  = { # base + "spaces/?lid=" + id of desired library
    "chemistry": 5903,
    "grainger": 3606,
    "international": 5766,
    "main": 3608,
    "music": 3153,
    "studio": 16231
}
args = "&gid=0&c=0" # additional arguments

# url to scrape
url = base + "spaces?lid=" + str(id["chemistry"]) + args
print(url)

# open selenium instance
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# navigate to url
driver.get(url)

# extract data
events = [ev.get_attribute("title") for ev in driver.find_elements(By.CLASS_NAME, "fc-event-today")]
print(len(events))

for ev in events[:10]:
    print(ev)

# quit driver
driver.quit()
