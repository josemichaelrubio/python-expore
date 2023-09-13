import passer as add_two_numbers
import random
import balls as two_numbers
import math

addition = add_two_numbers.adder(random.choice(two_numbers.numbers),
                                 random.choice(two_numbers.numbers))
square_root = math.sqrt(addition)
print(addition)
print(square_root)