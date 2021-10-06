import random

destinations = ["Fredericksburg", "Waco", "San Marcos", "San Antonio"]
restaurants = ["Olive Garden", "Chili's", "Chipotle", "McDonald's"]
transportation_modes = ["car", "horse", "uber", "motorcycle"]
entertainment_forms = ["watch a movie", "play mini golf", "go to the park", "go antiquing"]

def random_destination(list):
    destination = random.choice(list)
    return destination

def random_restaurant(list):
    restaurant = random.choice(list)
    return restaurant

def random_transportation(list):
    mode = random.choice(list)
    return mode

def random_entertainment(list):
    form = random.choice(list)
    return form

def random_daytrip():
    destination = random_destination(destinations)
    restaurant = random_restaurant(restaurants)
    mode = random_transportation(transportation_modes)
    form = random_entertainment(entertainment_forms)
    happy = input(f"Would you like go to {destination} by {mode} and eat at {restaurant} you {form}? ")
    if happy == "yes":
        print("Yay!")
    else:
        print("Oh no")

random_daytrip()