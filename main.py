import random

destinations = ["Fredericksburg", "Waco", "San Marcos", "San Antonio"]
restaurants = ["Olive Garden", "Chili's", "Chipotle", "McDonald's"]
transportation_modes = ["car", "horse", "uber", "motorcycle"]
entertainment_forms = ["watch a movie", "play mini golf", "go to the park", "go antiquing"]

r_destination = random.choice(destinations)
r_restaurant = random.choice(restaurants)
r_mode = random.choice(transportation_modes)
r_form = random.choice(entertainment_forms)


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

def daytrip_generator(destination, mode, restaurant, form):
    confirm = input(f"Would you like go to {destination} by {mode} and eat at {restaurant} after you {form}? ")
    if confirm == "yes":
        print("Have fun!")
    else:
        change_destination = input("Do you want to change the destination? ")
        if change_destination == 'yes':
            new_destination = change_choice(destination, destinations)
        else:
            new_destination = destination
        change_mode = input("Do you want to change the mode of transportation? ")
        if change_mode == 'yes':
            new_mode = change_choice(mode, transportation_modes)
        else:
            new_mode = mode
        change_restaurant = input("Do you want to change the restaurant? ")
        if change_restaurant == 'yes':
            new_restaurant = change_choice(restaurant, restaurants)
        else:
            new_restaurant = restaurant
        change_form = input("Do you want to change the form of entertainment? ")
        if change_form == 'yes':
            new_form = change_choice(form, entertainment_forms)
        else:
            new_form = form
        print("Great, let's make sure this is correct...")
        daytrip_generator(new_destination, new_mode, new_restaurant, new_form)

daytrip_generator(r_destination, r_mode, r_restaurant, r_form)