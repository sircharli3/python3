#!/usr/bin/python3
import shelve

fruit = shelve.open("shelveTest_fruit")

fruit["lime"] = "a green thing"
fruit["orange"] = "an orange thaang"
fruit["apple"] = "a bit tart"
fruit["kiwi"] = "it has lil peeeewwbs"

# while True:
#     fruit_key = input("Enter a fruit: ")
#     if fruit_key == 'quit':
#         break
#
#

ordered_fruit_keys = list(fruit.keys())
ordered_fruit_keys.sort()
#print(ordered_fruit_keys)

#for f in fruit:
for f in ordered_fruit_keys:
    print(f + " - " + fruit[f])

    #no bueno code but works
    #fruit_description = fruit[fruit_key]

    #Better code, built-in error handling (e.g Tr/Catch)
    # fruit_description = fruit.get(fruit_key, "we do not have: " + fruit_key)
    # print(fruit_description)

fruit.close()

#print(fruit["lime"])

# for i in fruit:
#     print(i)
#     print(fruit[i])
























'''
import random

highest = 100
outcome_num = random.randint(1, highest)
found = False

while not found:
    print("Enter your guess, from 1 to {0}".format(highest))
    guess = int(input())

    if guess == outcome_num:
        print("You guessed it!")
        found = True
        break
    elif guess > outcome_num:
        print("Guess lower...")
    else:
        print("Guess higher...")
'''
#
# list1 = [4,3,1]
# #list1.sort()
# print(list1.sort())
