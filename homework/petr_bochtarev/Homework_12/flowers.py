from statistics import mean


class Flowers:
    def __init__(self, name, price, color, withering_time, freshness, stem_length):
        self.name = name
        self.price = price
        self.color = color
        self.withering_time = withering_time
        self.freshness = freshness
        self.stem_length = stem_length


class Roses(Flowers):
    pass


class Tulips(Flowers):
    pass


class Lilies(Flowers):
    pass


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def price_bouquet(self):
        return sum(flower.price for flower in self.flowers)

    def withering_time(self):
        return mean(flower.withering_time for flower in self.flowers)

    def sort_freshness(self):
        return sorted(flower.freshness for flower in self.flowers)

    def sort_stem_length(self):
        return sorted(flower.stem_length for flower in self.flowers)

    def sort_color(self):
        return sorted(flower.color for flower in self.flowers)

    def sort_price(self):
        return sorted(flower.price for flower in self.flowers)

    def search_flower(self, withering):
        # for flower in self.flowers:
        #     if withering == flower.withering_time:
        #         list_flowers.append(flower.name)
        list_flowers = [flower.name for flower in self.flowers if withering == flower.withering_time]
        if list_flowers:
            print(f'Найдены цветы: {list_flowers}')
        else:
            print('Необходимые цветы в букете не обнаружены')


rose_white = Roses('Роза', 150, 'Белый', 3, '90%', '30см')
chinese_rose = Roses('Роза', 200, 'Красный', 4, '89%', '40см')
damask_rose = Roses('Роза', 250, 'Розовый', 2, '91%', '45см')
green_tulips = Tulips('Тюльпан', 90, 'Зеленый', 3, '78%', '37см')
fringed_tulips = Tulips('Тюльпан', 120, 'Желтый', 7, '98%', '38см')
golden_lily = Lilies('Лилия', 120, 'Золотой', 9, '59%', '41см')
orange_lilies = Lilies('Лилия', 140, 'Оранжевый', 8, '88%', '35см')

boquet1 = Bouquet()
boquet1.add_flower(rose_white)
boquet1.add_flower(green_tulips)
boquet1.add_flower(golden_lily)

print('Букет состоит из цветов:')
for flower in boquet1.flowers:
    print(
        f'Цветок: {flower.name}, '
        f'Цена: {flower.price}, '
        f'Цвет: {flower.color}, '
        f'Время увядания цветка: {flower.withering_time}'
    )
print('=' * 70)
print(f'Стоимость букета: {boquet1.price_bouquet()}')
print('=' * 70)
print(f'Время увядания букета: {round(boquet1.withering_time(), 1)} дней')
print('=' * 70)
print(f'Сортировка по свежести: {boquet1.sort_freshness()}')
print('=' * 70)
print(f'Сортировка по длине стебля: {boquet1.sort_stem_length()}')
print('=' * 70)
print(f'Сортировка по цене: {boquet1.sort_price()}')
print('=' * 70)
print(f'Сортировка по цвету: {boquet1.sort_color()}')
print('=' * 70)
boquet1.search_flower(3)
