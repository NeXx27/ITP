
import sys
import os

# Add the parent directory of 'itp' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import file
import function
from itp import min
# print(file.studnet1)
# print(file.studnet2)
# print(file.studnet3)
# print(file.studnet4)
# print(function.even_odd(5))
# print(function.prime(5))
# print(function.finb(5))

print(min)