# Мне показывает ошибку Expression expected. Нашел, из-за чего может быть, нужно вместо index использовать enumerate
# но так как мы его не проходили, так делать не стал. Но с index могу быть проблемы, если элементы в списке будут
# повторяться
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = PRICE_LIST.split()

# =====Цикл, от которого отталкивался=====
# for x in new_list:
#     if new_list.index(x) % 2 == 0:
#         goods.append(x)
# =====Фильтр и лямбда для тренировки=====
#goods = list(filter(lambda x: new_list.index(x) % 2 == 0, new_list))

goods = [x for x in new_list if new_list.index(x) % 2 == 0]

# =====Второй цикл, от которого отталкивался=====
# for x in new_list:
#     if new_list.index(x) % 2 != 0:
#         price.append(int(x[:-1]))
# =====Фильтр и лямбда для тренировки, НО НЕ ПОНЯЛ, КУДА ВСТАВИТЬ (int(x[:-1])) вместо х после lambda не дает=====
#price = list(filter(lambda x: new_list.index(x) % 2 != 0, new_list))

price = [(int(x[:-1])) for x in new_list if new_list.index(x) % 2 != 0]
list_goods_price = dict(zip(goods, price))
print(list_goods_price)
