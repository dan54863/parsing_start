from bs4 import BeautifulSoup
import re
# .parent - вложенный ищет, когда не знаем какой div
# find()
# find_all()
# find_parent()
# .parents
# find_parents()

#find_next_sibling()  - влево вправо от общих родителей
#find_previous_sibling()


# ^ - начало строки  $ - конец строки . - любой символ
# + - неогранич колво вхождений '\w' - буквы цифры _


def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois: # если слово копирайтер в whois
        return tag #слово есть
    return None


def get_salary(txt):
    #salary: 2700 usd per month ПРИМЕР ФИЛЬТРА
    pattern = r'\d{1,9}'   #r - чтобы интерпретатор не \d интепретировал это (\d - означает цифры)  {1,9} -  конкретеззация цифр, [0] - чтобы отделить только цифры
    salary = re.findall(pattern, txt)[0]  #что ищем (pattern) и где ищем (txt)
    print(salary) #2700


def main():
    file = open('index.html').read()

    soup = BeautifulSoup(file,'lxml')
    # row = soup.find_all('div', {'data-set':'salary'})
    # row = soup.find_all('div', {'class':'row'})
    # alena = soup.find('div', text='Alena').parent   ПРИМЕР ПОИСКА РОДИТЕЛЕЙ


    # copywriters = []
    # persons = soup.find_all('div', class_='row')
    # for person in persons:
    #     cw = get_copywriter(person)
    #     if cw:
    #         copywriters.append(cw)
    # print(copywriters)   ПРИМЕР ФИЛЬТРАЦИИ ТЕГОВ

    salaryss = soup.find_all('div', {'data-set': 'salary'})
    for i in salaryss:
        get_salary(i.text)








if __name__ == '__main__':
    main()