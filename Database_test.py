import csv
from peewee import *

db = PostgresqlDatabase(database='test', user='postgres', password='funtun', host='localhost')


class Coin(Model):
    # Создаем таблицу
    name = CharField() # Создаем имя в таблице
    syb = CharField()
    price = CharField()
    url = TextField()


    class Meta: # связь класса и бд
        database = db


def main():

    db.connect() # коннектим
    db.create_tables([Coin]) # создаем одну таблицу (класс)

    with open('Crypt.csv') as f:
        order = ['name', 'syb', 'price', 'url']
        reader = csv.DictReader(f, fieldnames=order)

        coins = list(reader) # превращаем в список монеты

#### медленный и грузящий жд способ добавления в бд

        # for row in coins:
        #     coin = Coin(name=row['name'], syb=row['syb'],
        #                 price=row['price'], url=row['url']) # cоздаем экземпляр класса
        #     coin.save() # сохраняем экзепляр класса в бд


#### способ ПОЛУЧШЕ
        # with db.atomic():   #способ работы с транзакциями бд
        #     for row in coins:
        #         Coin.create(**row)  #на каждой итерации передайем словарик row, ** - словарик kwargs

        with db.atomic():
            for index in range(0, len(coins), 100):  # запись слайсами по 100 штук
                Coin.insert_many(coins[index:index+100]).execute()




if __name__ == '__main__':
    main()