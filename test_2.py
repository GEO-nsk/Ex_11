import EAN_INFO

from solution_2 import Product
from solution_2 import Load
from solution_2 import Basket

Load.write('products.txt')
basket1 = Basket()
flag = True
while flag:
    ans = int(input('Доступные команды:\n'
              '1 - показать прайс-лист\n'
              '2 - добавить в корзину\n'
              '3 - убрать из корзины\n'
              '4 - показать содержание корзины\n'
                '5 - завершить работу программы\n'))

    if ans == 1:
        Product.show()
    if ans == 2:
        ean_code = str(input('введите штрих-код:'))
        basket1.add(ean_code)
    if ans == 3:
        ean_code = str(input('введите штрих-код:'))
        basket1.delete(ean_code)
    if ans == 4:
        basket1.show()
    if ans == 5:
        flag = False