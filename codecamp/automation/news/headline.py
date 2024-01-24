from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year =now.strftime("%m%d%Y")
website = "https://www.bola.com/"
path = "/home/haris/Downloads/chromedriver-linux64 (1)/chromedriver-linux64/chromedriver"

options = Options()
options.add_argument("--headless=new")
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

cointainers = driver.find_elements(by='xpath', value='//aside[@class="articles--iridescent-list--text-item__details"]')

titles = []
subtitles = []
links = []

for cointainer in cointainers:
    title = cointainer.find_element(by="xpath", value="./header/h4/a").get_attribute("title")
    subtitle = cointainer.find_element(by="xpath", value="./div").text
    link = cointainer.find_element(by="xpath", value="./header/h4/a").get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)


my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{month_day_year}.csv'
file_patch = os.path.join(application_path,file_name)
df_headlines.to_csv(file_patch)

driver.quit()