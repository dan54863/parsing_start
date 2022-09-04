import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)  # получаем ответ response
    return response.text # вернем html содержимое через text

def clean(str):
    # 1,971 total ratings чистим от ненужных слов справа
    r = str.replace('$', '')
    r = r.replace(',', '')
    r = r.replace('.', ',')
    return r


def get_data(html):
    #разберем данные
    soup = BeautifulSoup(html, 'lxml') #второй арг - это парсер
    trs = soup.find('table', class_='h7vnx2-2 czTsgW cmc-table').find('tbody').find_all('tr') # теги tr в таблице это строка, которые содержат данные по тегам td

    for tr in trs:
        tds = tr.find_all('td') # список всех тегов td в данном tr
        if tds[2].find('p') is None:
            name = 'No type'
        else:
            name = tds[2].find('p').text

        if tds[2].find('p', class_='sc-1eb5slv-0 gGIpIK coin-item-symbol') is None:
            sym = 'No type'
        else:
            sym = tds[2].find('p', class_='sc-1eb5slv-0 gGIpIK coin-item-symbol').text


        url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
        p = tds[3].find('span').text
        price = clean(p)
        print(name, price, sym, url)

        data = {'name': name,
                'sym': sym,
                'url': url,
                'price': price}
        csv_write(data)


def csv_write(data):
    with open('Table.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['sym'],
                         data['price'],
                         data['url']))

def main():
    url = 'https://coinmarketcap.com/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()