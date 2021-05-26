from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv
import argparse

def get_google_url(q):
    q = '+'.join(q.split())
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    return url


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str, help="path to file")
ap.add_argument("-d", "--driver", type=str, help="path to driver")
args = vars(ap.parse_args())

opts = Options()
opts.add_argument("--headless")
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
driver = webdriver.Firefox(options = opts, executable_path = args['driver'])

with open(args['path'], mode='r', encoding='utf-8-sig') as fp:
    reader = csv.reader(fp, delimiter=",", quotechar='"')
    # next(reader, None)  # skip the headers
    search_list = [row[0] for row in reader]

for data in search_list:
    driver.get(get_google_url(data))

    txt = driver.find_element_by_xpath('//*[@id="result-stats"]').text
    print(f"{data}: {txt}")
    
    