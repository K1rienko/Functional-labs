# Задача 3
import random

rn1 = random.randint(0, 10)
print(rn1)

rn2 = random.randrange(50, 100, 2)
print(rn2)

rn3 = random.random()
print(rn3)


list = ['one', 'two', 'three']
for i, value in enumerate(list):
    print(f'{i+1}: {value}')