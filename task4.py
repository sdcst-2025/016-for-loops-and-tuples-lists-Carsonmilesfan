# Task 4
# Access list values

"""
Ask the user to enter in a number less than 10
Print out the list element that corresponds to that
position in the tuple
"""

people=("John","Tyler","Dash","Kieran","Jayson","Tomoki","Minji","Dawson","Hewitt","Josh","Anson","Cole")

robbee = int(input("enter a number from 1 to 12 => "))
robber = robbee - 1
print(f" The person in position {robbee} is {people[robber]}")