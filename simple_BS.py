import requests
from bs4 import BeautifulSoup



def get_html(url):
    response = requests.get(url)  # получаем ответ response
    return response.text # вернем html содержимое через text


def get_data(html):
    #разберем данные
    soup = BeautifulSoup(html, 'lxml') #второй арг - это парсер
    h1 = soup.find('div', id='intro').find('h1').text
    return h1

def main():
    url = 'https://wordpress.org/'
    print(get_data(get_html(url)))




if __name__ == '__main__':
    main()