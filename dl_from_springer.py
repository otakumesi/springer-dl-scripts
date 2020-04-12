import ipdb
from time import sleep
import requests
import pandas as pd
from bs4 import BeautifulSoup
from glob import glob

SPRINGER_URL = 'https://link.springer.com'
EBOOK_LIST_EXCEL_DIR = './src'
EBOOK_LIST_SHEET_INDEX = 1
EBOOK_URL_COLUMN_NAME = 'OpenURL'

DOWNLOADED_PDF_DIR = './downloads'

def main():
    files = glob(f'{EBOOK_LIST_EXCEL_DIR}/*')
    excel_path = [f for f in files if f.endswith('.xlsx')][0]
    urls = read_ebook_list(excel_path)[EBOOK_URL_COLUMN_NAME]

    for url in urls:
        text = get_content(url)
        soup = BeautifulSoup(text, 'lxml')

        title = soup.find('h1').text
        pdf_url = soup.find('a', class_='test-bookpdf-link')['href']

        pdf = get_content(f'{SPRINGER_URL}/{pdf_url}')

        with open(f'{DOWNLOADED_PDF_DIR}/{title}', 'wb') as f:
            f.write(pdf)
        sleep(2)
        ipdb.set_trace()



def read_ebook_list(file_path):
    return pd.read_excel(file_path, EBOOK_LIST_SHEET_INDEX)

def get_content(url):
    r = requests.get(url, timeout=5)

    if r.status_code != 200:
        return None

    if  r.headers['Content-Type'].startswith('text'):
        return r.text

    return r.content

if __name__ == '__main__':
    main()
