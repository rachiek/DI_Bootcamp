# Here is a python code that generates a list of 20000 random numbers, called list_of_numbers, and a target number.
# Copy this code, and create a program that finds, within list_of_numbers all the pairs of number that sum to the target number

import random
list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number   = 3728

def find_pairs_with_sum(numbers, target):
    pairs = []
    seen = set()
    
    for number in numbers:
        complement = target - number
        if complement in seen:
            pairs.append((complement, number))
        seen.add(number)
    
    return pairs

print(find_pairs_with_sum(list_of_numbers, target_number))