import requests
from bs4 import BeautifulSoup
import csv




def get_html(url):
    r = requests.get(url)
    if r.ok: # сервер вернул код 200 - все ок ## 403 404 - будет плохо
        return r.text # вернули html страницу
    print(r.status_code)

def csv_write(data):
    with open ('Music.csv', 'a', newline='', errors='ignore') as f:
        writer = csv.writer(f)

        writer.writerow((data['name'], data['janre'], data['downloads'], data['url']))

def clean_txt(s):
    str =s.split(" ")[-1]
    return str

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    list_songs = soup.find('div', id='allEntries')
    for song in (list_songs):
        try:
            name = song.find('span', class_="eTitle").text
        except:
            name =''
        try:
            url = song.find('a').get('href')
        except:
            url =''
        try:
            downloads = song.find('div', class_="ownedemis-bottom odd").find('span').text
            clean_txt(str(downloads))
            print(downloads)
        except:
            downloads =''

        try:
            janre = song.find(class_="game-detali odd").find('a').text
        except:
            janre =''
        print(name, janre, downloads, url)

        date = {'name': name,
                'janre': janre,
                'downloads': downloads,
                'url': url}

        csv_write(date)
def main():
    pattern = 'https://mobzvonok.ru/page/{}/'

    for i in range(1, 4):
        url = pattern.format(str(i))
        get_page_data(get_html(url))


if __name__=='__main__':
    main()


