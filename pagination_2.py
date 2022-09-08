import requests
from bs4 import BeautifulSoup
import csv
import re

def get_html(url):
    r = requests.get(url)
    if r.ok:  # сервер вернул код 200 - все ок ## 403 404 - будет плохо
        return r.text  # вернули html страницу
    print(r.status_code)


def csv_write(data):
    with open('Crypt.csv', 'a', newline='', errors='ignore') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'], data['sym'], data['price'], data['url']))


def clean_txt(s):
    str = s.split(" ")[-1]
    return str


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = soup.find('div', class_='coingecko-table').find('tbody').find_all(
        'tr')  # теги tr в таблице это строка, которые содержат данные по тегам td
    for tr in trs:
        tds = tr.find_all('td')  # список всех тегов td в данном tr

        try:
            name = tds[2].find('span', class_="lg:tw-flex font-bold tw-items-center tw-justify-between").text.strip()
        except:
            name = ''

        try:
            sym = tds[2].find('span',
                              class_="d-lg-inline font-normal text-3xs tw-ml-0 md:tw-ml-2 md:tw-self-center tw-text-gray-500 dark:tw-text-white dark:tw-text-opacity-60").text.strip()
        except:
            sym = ''

        try:
            url = 'https://www.coingecko.com/ru' + tds[2].find('a',
                                                               class_="tw-flex tw-items-start md:tw-flex-row tw-flex-col").get(
                'href')
        except:
            url = ''

        try:
            price = tds[3].get('data-sort')
        except:
            price = ''

        print(name, sym, url, price)
        data = {'name': name,
                'sym': sym,
                'price': price,
                'url': url}

        csv_write(data)

def main():
    pattern = 'https://www.coingecko.com/ru?page={}'
    for i in range(1, 130):
        url = pattern.format(str(i))
        get_page_data(get_html(url))  #№по номеру пагинации
    # url = 'https://www.coingecko.com/ru?page=1'
    # while True:
    #     get_page_data(get_html(url))
    #     soup = BeautifulSoup(get_html(url), 'lxml')
    #
    #     try:
    #         pattern ='Next'
    #         url = 'https://www.coingecko.com/' + soup.find('ul', class_='pagination').find('a', text=re.compile(pattern)).get('href')
    #     except:
    #         break
if __name__ == '__main__':
    main()
