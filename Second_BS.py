import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    response = requests.get(url)  # получаем ответ response
    return response.text     # вернем html содержимое через text

def clean(str):
    # 1,971 total ratings чистим от ненужных слов справа
    r = str.split(' ')[0] # строга делится по пробелам, забераем первый элемент (1,971)
    return r.replace(',', '') #убрали запятые  1971

def get_data(html):
    #разберем данные
    soup = BeautifulSoup(html, 'lxml') #второй арг - это парсер
    for k in range(4):
        popular = soup.find_all('section')[k]  # find_all ищет все секшн на странице, для популар это 3 (что то типо списка)
        plugins = popular.find_all('article') # find_all ищет все плагины в секшне

        for plugin in plugins:
            name = plugin.find('h3').text # выводим названия плагинов из обьекта soup (как в списках)
            url = plugin.find('h3').find('a').get('href') #ищем по тэгу a, href - атрибут берется через метод get
            r = plugin.find('span', class_='rating-count').find('a').text #важно указывать класс именно через_ , так как тут не ссылка, то без тега href и через text
            rating = clean(r)


            data = {'name': name,
                    'url': url,
                    'rating': rating }
            csv_write(data)


def csv_write(data):
    with open('Plugins.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'],
                         data['url'],
                         data['rating']))

def main():
    url = 'https://wordpress.org/plugins/'
    print(get_data(get_html(url)))


if __name__ == '__main__':
    main()