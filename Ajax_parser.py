# Парсим этот сайт https://www.liveinternet.ru/rating/ru/#geo=ru;page=2;

import requests, csv


def get_html(url):
    r = requests.get(url)
    return r.text


def csv_write(data):
    with open('Ajax.csv', 'a', newline='', errors='ignore', ) as f:
        order = ['name', 'url', 'description', 'users_cnt', 'percent']
        writer = csv.DictWriter(f, fieldnames=order)
        writer.writerow(data)





def main():



    pattern = 'https://www.liveinternet.ru/rating/ru//today.tsv?page={}'  #Ссылка из гет запроса

    for i in range(1, 10):
        url = pattern.format(str(i))
        response = get_html(url)     #.split('\n')   без сплит представлялось все в виде одной строки, теперь это список с элементами
        data = response.strip().split('\n')[1:]  #strip убирает пустые элемента списка [1:] - с первого элемента списка и до конца



        for row in data:
            columns = row.strip().split('\t') # рахюиваем по столбцам по \t
            name = columns[0]
            url = columns[1]
            description = columns[2]
            users_cnt = columns[3]
            percent = columns[4]

            print(columns)
            data = {'name': name, 'url': url, 'description': description,
                    'users_cnt': users_cnt, 'percent': percent}

            csv_write(data)

if __name__=='__main__':
    main()