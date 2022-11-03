import json
from datetime import datetime
import itertools
import uuid


class Products:
    def __init__(self, file_name, string_name):
        with open(file_name) as file:
            self._products_data = json.load(file)
        self._string_name = string_name

    @property
    def get_info(self):
        return f'{self._products_data.items()}'

    def __str__(self):
        return '\n'.join(f'{i}' for i in self._products_data[self._string_name])


class Sauces(Products):
    def __init__(self, file_name='Sauces.json', string_name="Sauces"):
        super().__init__(file_name, string_name)
        self._string_name = string_name

class Pizza:
    def __init__(self):
        self._today = datetime.today().strftime('%A')
        with open('Task_2.json') as file:
            pizza_database = json.load(file)
        date = self._today
        for i in pizza_database['Pizza']:
            if date == i['day']:
                self.__dict__ = i.copy()

    @property
    def get_info(self):
        return dict(itertools.islice(self.__dict__.items(), 4))

    def add_topping(self, product):
        self.__dict__['ingredients'].append(product['name'])
        self.__dict__['weight'] += product['weight']
        self.__dict__['price'] += product['price']

    def __str__(self):
        return str.join('\n', [f'{i}: {self.__dict__[i]}' for i in self.__dict__.keys() if i != 'day'])


class Order:
    def __init__(self):
        self._order_id = uuid.uuid1()
        with open('Task_2.json') as file:
            self._pizza_menu = json.load(file)
        self._extra = Sauces()
        self._order = Pizza()

    @property
    def get_menu(self):
        return '\n'.join([f'{i}' for i in self._extra._products_data[self._extra._string_name]])

    def change_pizza(self, product):
        if not any(product == i['name'] for i in self._extra._products_data[self._extra._string_name]):
            raise ValueError('invalid input')
        for i in self._extra._products_data[self._extra._string_name]:
            if product == i['name']:
                self._order.add_topping(i)

    def make_order(self):
        with open('Order.json') as file:
            database = json.load(file)
        if "Data" not in database:
            database["Data"] = {}
        order_id = str(self._order_id)
        if not (order_id in database['Data']):
            info = self._order.get_info
            database["Data"][order_id] = {
                'name': info['name'],
                'weight': info['weight'],
                'price': info['price'],
                'purchase_date': str(datetime.now())
            }
            json.dump(database, open('Order.json', 'w'), indent=4)

    @property
    def get_order_info(self):
        info = self._order.get_info
        return f'Today\'s pizza of a day is: {info["name"]}\nIngredients - ' + ', '.join([f'{i}' for i in info["ingredients"]]) +\
               f'\nWeight - {info["weight"]}\nPrice - {info["price"]}'

    def __str__(self):
        return f'{self._order_id}\n{self._order}'


your_order = Order()
print(your_order.get_order_info)
result = input("We're having a brand new deal! Want to add a sauce for a discounted price? (yes/no)\n")
if result.lower() == "yes":
    print('Which one do you want to add?')
    print(your_order.get_menu)
    your_order.change_pizza(input())
elif result.lower() != "no":
    raise IOError('invalid input')

your_order.make_order()
print(your_order)