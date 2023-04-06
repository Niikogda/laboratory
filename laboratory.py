
import random

random_list = random.sample(range(-50, 50), 20)
even_numbers = []
odd_numbers = []
negative_numbers = []
positive_numbers = []

for num in random_list:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
        
    if num < 0:
        negative_numbers.append(num)
    elif num > 0:
        positive_numbers.append(num)
print(random_list)
print("even: ", even_numbers)
print("odd: ", odd_numbers)
print("neg: ", negative_numbers)
print("pos: ", positive_numbers)
