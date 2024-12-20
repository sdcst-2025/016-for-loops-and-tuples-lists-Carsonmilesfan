#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
import math
nums = (5,-2,12,-8,14,16)

for goober in nums:
    if goober <= 0:
        print(f"{goober} => ☠  ҉𝔱h𝔞t n𝔲m𝔟e𝔯 𝔦s n𝔬t v𝔞l𝔦d҉")
        continue
    goofer = math.sqrt(goober)
    print(f"{goober} => 💯 {goofer}")