# Задача 4.4

n = int(input("Общее количество карт: "))
remaining_cards = sum(range(1, n + 1))

for sum in range(n - 1):
   remaining_cards = remaining_cards - int(input("Оставшиеся карты: "))
print("Потерянная карточка это: %s" % remaining_cards)