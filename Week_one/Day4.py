# #Day 4 -Randomization and Python Lists
#Randomization 
import random
random_integer  = random.randint(1, 10)
print(random_integer)

random_float = random.random()
print(random_float)
print(random_float * 5)

#Day 4.1 Heads or Tails Exercise
import random
random.seed()
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
random_int = random.randint(0, 1)
if random_int == 1:
    print("Heads")
else:
    print("Tails")

#4.2 Banker Roulette - Who will pay the bill?
import random
random.seed()
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
namesAsCSV = input("Give me everybody's names, separated by a comma. ")
names = namesAsCSV.split(", ")
person_who_pays = random.choice(names)
print(person_who_pays, "will be paying for the meal")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

#Day 4.3 -Treasure Map/
row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to place the treasure? ")
first_position = position[0]
second_position = position[1]
map = first_position[0]
