import requests, csv
from bs4 import BeautifulSoup

def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.5.940 Yowser/2.5 Safari/537.36'}
    r = requests.get(url, headers=user_agent)
    return r.text

def write_csv(data):
    with open('testiomials.csv', 'a', newline='', errors='ignore') as f:
        order = ['worker', 'since']
        writer =csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)

def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts #вернет либо пустой список, либо с отзывами


def get_page_data(ts):
    for t in ts:
        try:
            since = t.find('p', class_='traxer-since').text.strip()
        except:
            since = ''
        try:
            worker = t.find('p', class_='testimonial-author').text.strip()
        except:
            worker = ''

        print(worker, since)
        data = {'worker': worker, 'since': since}
        write_csv(data)


def main():
    page = 1
    while True:

        url = 'https://catertrax.com/traxers/page/{}/'.format((str(page)))

        articles = get_articles(get_html(url))

        if articles: # если полный то тру
            get_page_data(articles)
            page += 1
        else:
            break

    print('END')
if __name__=='__main__':
    main()