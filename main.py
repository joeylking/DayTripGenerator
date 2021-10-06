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


def change_choice(elem, list):
    list.remove(elem)
    new_elem = random.choice(list)
    check = input(f"Switch to {new_elem}? ")
    if check == 'yes':
        print('OK!')
        return new_elem
    else:
        try:
            change_choice(new_elem, list)
        except:
            print("I'm out of ideas!")

# TODO: make daytrip generator that can be reused with random values or new chosen values

def random_daytrip():
    destination = random_destination(destinations)
    restaurant = random_restaurant(restaurants)
    mode = random_transportation(transportation_modes)
    form = random_entertainment(entertainment_forms)
    happy = input(f"Would you like go to {destination} by {mode} and eat at {restaurant} after you {form}? ")
    if happy == "yes":
        print("Yay!")
    else:
        change_destination = input("Do you want to change the destination? ")
        if change_destination == 'yes':
            new_destination = change_choice(destination, destinations)
        change_mode = input("Do you want to change the mode of transportation? ")
        if change_mode == 'yes':
            new_mode = change_choice(mode, transportation_modes)
        change_restaurant = input("Do you want to change the restaurant? ")
        if change_restaurant == 'yes':
            new_restaurant = change_choice(restaurant, restaurants)
        change_form = input("Do you want to change the form of entertainment? ")
        if change_form == 'yes':
            new_form = change_choice(form, entertainment_forms)


    


random_daytrip()