import urllib.request, sys, time
from bs4 import BeautifulSoup
import requests
import pandas as pd

pagesToGet = 4

upperframe = []
for page in range(1, pagesToGet + 1):
    print('processing page :', page)
    url = 'https://english.onlinekhabar.com/category/political/page/' + str(page)
    print(url)


    try:

        page = requests.get(url)

    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print('ERROR FOR LINK:', url)
        print(error_type, 'Line:', error_info.tb_lineno)
    time.sleep(2)
    soup = BeautifulSoup(page.text, 'html.parser')
    frame = []
    links = soup.find_all('div', attrs={'h2': 'ok-news-post ltr-post'})
    print(len(links))
    filename = "NEW.csv"
    f = open(filename, "w", encoding='utf-8')
    headers = "Statement"
    f.write(headers)

    for j in links:
        Statement = j.find("h2", first=True)

f.close()
data = pd.DataFrame(upperframe, columns=['Statement'])
data.to_csv(NEWS.csv,index=False, encoding='utf-8')