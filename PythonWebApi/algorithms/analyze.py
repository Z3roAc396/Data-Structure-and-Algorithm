import random

def GenerateRandomArray(number_of_elements):
    return random.sample(range(-500,501), number_of_elements)

print(GenerateRandomArray(5))

