# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# config, used for both scraping methods
base = "https://uiuc.libcal.com/"
all = "allspaces" # base + all
id  = { # base + "spaces/?lid=" + id of desired library
    "chemistry": 5903,
    "funk": 3604,
    "grainger": 3606,
    "international": 5766,
    "main": 3608,
    "music": 3153,
    "studio": 16231
}
args = "&gid=0&c=0" # additional arguments

busyness = {
    "chemistry": 0,
    "funk": 0,
    "grainger": 0,
    "international": 0,
    "main": 0,
    "music": 0,
    "studio": 0
}

for key in id:
    # url to scrape
    url = base + "spaces?lid=" + str(id[key]) + args

    # # open selenium instance
    # # note that headless running is currently broken in 4.13 - https://stackoverflow.com/questions/77191221
    driver = webdriver.Chrome()

    # # navigate to url
    driver.get(url)

    # # extract data
    events = [ev.get_attribute("title") for ev in driver.find_elements(By.CLASS_NAME, "fc-event-today")]
    if len(events) == 0:
        busyness[key] = 0
    else:
        total_unavailable = 0

        for ev in events:
            if "Unavailable" in ev:
                total_unavailable = total_unavailable + 1

        ratio = float(total_unavailable)/len(events) * 100

        # quit driver
        driver.quit()
    
    busyness[key] = round((ratio)/20)

print(busyness)
