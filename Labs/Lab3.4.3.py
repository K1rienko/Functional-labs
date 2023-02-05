# Задача 4.3

# A > B
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i)  