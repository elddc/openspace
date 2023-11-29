# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime, timedelta
from time import sleep
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from db_helper import update_building

load_dotenv()
engine = create_engine(os.getenv("DB_URI"))
Session = sessionmaker(engine)

# config, used for both scraping methods
base = "https://uiuc.libcal.com/"
all = "allspaces" # base + all
id  = { # base + "spaces/?lid=" + id of desired library
    "Chemistry Library": 5903, 
    "Funk ACES Library": 3604, 
    "Grainger Library": 3606,
    "Main Library": 3608,
    "Music & Performing Arts Library": 3153,
    "studio": 16231,
    # "international": 5766
}

args = "&gid=0&c=0" # additional arguments

busyness = {
    "Chemistry Library": [0, 0],
    "Funk ACES Library": [0, 0],
    "Grainger Library": [0, 0],
    "Main Library": [0, 0],
    "Music & Performing Arts Library": [0, 0],
    "studio": [0, 0]
}

rounded = datetime.now() - (datetime.now() - datetime.min) % timedelta(minutes=30)
meridian = ("am", "pm")[bool(int((datetime.now()).strftime('%H')) > 11)]
current_time = (rounded.strftime('%Y/%m/%d %I:%M:%S'))[11:16] + meridian
next_time = ((rounded + timedelta(minutes=30)).strftime('%Y/%m/%d %I:%M:%S'))[11:16] + meridian

# # open selenium instance
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

for key in id:
    print("_______________________")
    print("Library: " + key)

    # url to scrape
    url = base + "spaces?lid=" + str(id[key]) + args

    print(url)
    # # navigate to url
    driver.get(url)

    # wait for page load
    sleep(0.5)

    # # extract data
    events = [ev.get_attribute("title") for ev in driver.find_elements(By.CLASS_NAME, "fc-event-today")
              if current_time in ("0" + ev.get_attribute("title")) or next_time in ("0" + ev.get_attribute("title"))]

    total_unavailable = 0

    for ev in events:
        print(ev)
        if "Unavailable" in ev:
            total_unavailable = total_unavailable + 1

    print("Total: " + str(len(events)))
    print("Unavailable: " + str(total_unavailable))

    busyness[key] = [total_unavailable, len(events)]

    print("Busyness: " + str(busyness[key]))

# quit driver
driver.quit()

print(busyness)
busyness["Main Library"] = [busyness["Main Library"][i] + busyness["studio"][i] for i in range(2)]
busyness.pop("studio")
print(busyness)

with Session() as session:
    for building in busyness:
        ratio = busyness[building]
        update_building(session, building, int(float(ratio[0])/ratio[1] * 100) if ratio[1] != 0 else 0)
