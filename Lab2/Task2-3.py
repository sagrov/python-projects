class Product:
    def __init__(self, name, price, description, *size):
        if name == '' or name == ' ':
            raise ValueError('Invalid name input')
        self._name_product = name
        if not isinstance(price, (float, int)) or price < 0:
            raise ValueError('invalid price input')
        self._price = price
        if description == '' or description == ' ':
            raise ValueError('Invalid description input')
        self._description = description
        # as a string info
        if type(size) is not tuple or len(size) != 3 or not all(isinstance(i, (int, float)) for i in size):
            raise ValueError('Invalid description input')
        self._dimensions = size

        # returning all info about the product
    @property
    def get_product_data(self):
        return self._price, self._description, self._dimensions

    @get_product_data.setter
    def get_product_data(self, data):
        if data[0] == '' or data[0] == ' ':
            raise ValueError('Invalid name input')
        self._name_product = data[0]
        if not isinstance(data[1], (float, int)) or data[1] < 0:
            raise ValueError('invalid price input')
        self._price = data[1]
        if data[2] == '' or data[2] == ' ':
             raise ValueError('Invalid description input')
        self._description = data[2]
        if type(data[3:]) is not tuple or len(data[3:]) != 3 or not all(
                isinstance(i, (int, float)) for i in data[3:]):
            raise ValueError('Invalid description input')
        self._dimensions = data[3:]

    @property
    def get_product_price(self):
        return self._price

        # printing info about the product
    def __str__(self):
        return f'{self._name_product}:\n  Price: {self._price}$\n  ' \
                f'Description: {self._description}\n  Dimensions: {self._dimensions}\n'


class Customer:
    def __init__(self, name, surname, phone_number):
        self._name = name
        self._surname = surname
        self._phone_number = phone_number

    @property
    def get_customer_data(self):
        return self._name, self._surname, self._phone_number

    @get_customer_data.setter
    def get_customer_data(self, info):
        self._name = info[0]
        self._surname = info[1]
        self._phone_number = info[3]

    # printing info about the customer
    def __str__(self):
        return f"\nCustomer:\n  Name: {self._name}\n  Surname: {self._surname}\n  Phone number: {self._phone_number}\n"


# A class describing an order from a customer and his products
class Order:
    def __init__(self, customer, **products):
        self.client = customer
        self.products = products
        self.total_price = 0

    # function for getting total price of the customers' check
    @property
    def get_total_price(self):
        for i in self.products:
            self.total_price += self.products[i]._price
        return self.total_price

    @property
    def customer_data(self):
        return self.client

    @customer_data.setter
    def customer_data(self, client_):
        self.client = client_

    #  for printing all info about the customers' products
    def product_data(self):
        return '\n'.join([i for i in list(map(str, list(self.products.values())))])


Potato = Product('Potato', 2, 'Just a potato', 23, 45, 3)
Santa = Product('Santa', 66, 'Ask him to bring a present to you', 5, 6, 3)
Book = Product('Bread', 10, 'Read it and you\'ll become the best pizza-eater ', 5, 87, 35)
Solo = Customer('Alexey', 'Berezin', '+380637894512')
order = Order(Solo, first=Potato, second=Santa, third=Book)
print(order.product_data(), order.customer_data)
print('Total price:', order.get_total_price)
