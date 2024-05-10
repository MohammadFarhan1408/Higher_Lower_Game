import os
import random
from art import logo, vs
from game_data import data_list


def get_random_person():
    return random.choice(data_list)


def check_answer(guess, search_a, search_b):
    if search_a > search_b:
        return guess == 'a'
    else:
        return guess == 'b'


total_score = 0
person_b = get_random_person()
user_pass = True

print(logo)
while user_pass:
    # Get two random people
    person_a = person_b
    person_b = get_random_person()

    # Ensure that person_a and person_b are different
    while person_a == person_b:
        person_b = get_random_person()

    # Ask user for their guess
    print(f"Compare A: {person_a['name']}")
    print(vs)
    print(f"Against B: {person_b['name']}")

    # Ask user for their guess
    user_guess = input("Who is most searched person in 2024? Type 'A' or 'B': ").lower()

    # Get the search counts of both persons
    searches_a = person_a['searches']
    searches_b = person_b['searches']
    is_right = check_answer(user_guess, searches_a, searches_b)

    os.system('cls')
    # Check if the user's guess is correct
    print(logo)
    if is_right:
        total_score += 1
        print(f"Correct! Your Current Score: {total_score}")
    else:
        print(f"Sorry, you lose! Final Score: {total_score}")
        user_pass = False
