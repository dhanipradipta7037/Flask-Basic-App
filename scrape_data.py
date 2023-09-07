from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import json

data = []
url = 'https://www.periplus.com/recommendations/Bestseller+Business'

# running playwright go to web
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url, timeout=120000)
    time.sleep(5)

#Scraping data with BeautfilSoup
    data_html = page.inner_html('div.row.row-category.row-categor-grid')
    soup = BeautifulSoup(data_html, "html.parser")
    books = soup.find_all('div', {'class':'single-product'})
    for book in books:
        img = book.find('img', {'class':'hover-img'}).get('src')
        urls = book.find('a').get('href')
        titles = book.find('h3', {'style':'line-height:10px;height:18px;'}).text.strip()
        try:
            author = book.find('a', {'style':'font-size:11.5px'}).text.strip()
        except:
            author = 'None'
        price = book.find('div', {'style':'font-size:100%;color:#000000;font-weight:600;'}).text.strip()
        list_data ={ 
            'Total':[
                {
                    'Title':titles,
                    'Price':price,
                    'Author':author,
                    'Image':img,
                    'Url':urls
                }
            ]
        }
        data.append(list_data)

# Save data to json
    with open("sample_v2.json", "w") as f:
        json.dump(data, f, indent=4)
    

    browser.close()
    
