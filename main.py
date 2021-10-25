from selenium import webdriver
from pathlib import Path
import requests
import time
import os
directory = input('Where do you want to download it?: ')
directory = Path(directory)
if directory.exists():
    foldername = 'Average database class book folder html'
    path = directory/foldername
    os.mkdir(path)
browser = webdriver.Firefox(executable_path='/home/scrappycoco/Documents/geckodriver')
browser.get('https://sites.psu.edu/database')
userElem = browser.find_element_by_id('blog_pass')
userElem.send_keys('ist210bk')
userElem.submit()
for _ in range(53):
    time.sleep(2)
    pagetitle = browser.find_element_by_class_name('entry-title')
    title = pagetitle.text
    print(f'Downloading {title}')
    if '/' in title:
        title = title.replace('/', '')
    filename = title + '.html'
    filler = path/filename
    file = open(filler, 'w+')
    with open(filler, "w") as f:
        f.write(browser.page_source)
    nextpage = browser.find_element_by_class_name('page-navigation-title')
    nextpage.click()
print('Done')
