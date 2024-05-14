import EAN_INFO

class Load:
    '''
    class loads products from file

    Methods:
        write: load to data
    '''
    @classmethod
    def write(cls, file_name):
        '''
        load to data
        param: file_name: name of file
        '''
        with open(file_name, 'r', encoding='utf-8') as ptr:
            for line in ptr:
                line_list = []
                for item in line.split(';'):
                    line_list.append(item)
                for k, v in EAN_INFO.EAN_INFO.items():
                    if line_list[2][0:3] == k:
                        country = v
                    if line_list[2][3:9] == k:
                        company = v
                product = Product(line_list[0], line_list[1], line_list[2], country, company)
                Product.data.append(product)


class Product:
    '''
    class with products

    attributes:
        __name: name of product
        __price: price of product
        __ean_code: ean_code of product
        __country: country that produce product
        __company: company that produce product
        data: list with all products

    methods:
        show: shows all products
    '''

    data = []

    def __init__(self, name, price, ean_code, country, company):
        self.__name = name
        self.__price = price
        self.__ean_code = ean_code
        self.__country = country
        self.__company = company

    name = property()
    price = property()
    ean_code = property()
    country = property()
    company = property()

    @name.getter
    def name(self):
        return self.__name

    @price.getter
    def price(self):
        return self.__price

    @ean_code.getter
    def ean_code(self):
        return self.__ean_code

    @country.getter
    def name(self):
        return self.__country

    @ean_code.getter
    def company(self):
        return self.__company

    @classmethod
    def show(cls):
        '''
        shows all products
        '''
        for item in cls.data:
            print(item)

    def __repr__(self):
        return f'Название: {self.__name} | Цена: {self.__price} | Страна: {self.__country} | Изготовитель: {self.__company} | Штрих-код: {self.__ean_code}'

class Basket:
    '''
    calss of product basket

    attributes:
        total_price: price of all products in basket

    methods:
        add: adds product to basket
        delete: remove product from basket
        show: shows product in basket
    '''

    def __init__(self):
        self.total_price = 0
        with open('basket_data.txt', 'w', encoding='utf-8') as f:
            pass

    def add(self, ean_code):
        '''
        adds product to basket
        param: ean_code: ean_code that client can add to basket
        '''
        for item in Product.data:
            if item.ean_code == ean_code:
                self.total_price += float(item.price)
        with open('basket_data.txt', 'a', encoding='utf-8') as f:
            f.write(f'{ean_code}\n')

    def delete(self, ean_code):
        '''
        remove product from basket
        param: ean_code: ean_code that client can remove from basket
        '''
        ean_list = []
        with open('basket_data.txt', 'r', encoding='utf-8') as ptr:
            for line in ptr:
                if int(line) != int(ean_code):
                    ean_list.append(line)
        with open('basket_data.txt', 'w', encoding='utf-8') as f:
            for item in ean_list:
                f.write(f'{item}\n')
        for item in Product.data:
            if int(item.ean_code) == int(ean_code):
                self.total_price -= float(item.price)


    def show(self):
        '''
        shows product in basket
        '''
        print('Товары в корзине:')
        with open('basket_data.txt', 'r', encoding='utf-8') as ptr:
            for line in ptr:
                for item in Product.data:
                    if line !='\n':
                        if int(item.ean_code) == int(line):
                            print(item)
        print(f'Общая стоимость: {self.total_price}')
