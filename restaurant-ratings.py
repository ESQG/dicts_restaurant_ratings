import sys
import random


def print_rating(restaurant, rating):
    """Formats and prints rating information."""

    print "%s is rated at %i" % (restaurant, rating)


def get_ratings_from_file(filename):
    """Puts ratings from a file into a dictionary.

    File format must have one entry per line, in the form "restaurant:rating"."""

    ratings = {}

    with open(filename) as data_file:

        for line in data_file:
            key, value = line.rstrip().split(":")
            ratings[key] = int(value)

    return ratings


if len(sys.argv) == 1:
    filename = raw_input("Please enter filename to read from: ").strip()
else:
    filename = sys.argv[1]

ratings = get_ratings_from_file(filename)


def pick_option():
    """Print a menu and get a choice of options from the user."""

    print """
Choose an option:
1) See all restaurant ratings
2) Rate another restaurant
3) Update a random restaurant's rating
4) Update a restaurant's rating of your choice
5) Quit
"""
    return int(raw_input("Your choice: "))


def get_new_rating(restaurant):
    """Get a new rating for the chosen restaurant, from the user."""

    print "%s is currently rated at %i." % (restaurant, ratings[restaurant])

    rating = int(raw_input("Choose a new rating for %s: " % restaurant))
    return rating


while True:
    choice = pick_option()  # Throws an error if an int is not given

    # display all restaurant ratings
    if choice == 1:
        for restaurant, rating in sorted(ratings.items()):
            print_rating(restaurant, rating)

    # get a new restaurant and its rating from user, update dictionary
    elif choice == 2:
        new_restaurant = raw_input("Please enter the name of a new restaurant: ").strip()
        new_rating = int(raw_input("Please rate this restaurant from 1 to 5: "))
        ratings[new_restaurant] = new_rating

    # get a random restaurant and a user rating of it, update dictionary
    elif choice == 3:
        restaurant = random.choice(ratings.keys())
        ratings[restaurant] = get_new_rating(restaurant)

    # update a chosen restaurant's rating
    elif choice == 4:
        restaurant = raw_input("Which restaurant would you like to update? ").strip()

        # if input isn't in the dictionary, pick a random restaurant
        if restaurant not in ratings:
            print "We couldn't find that restaurant. Since you can't spell we're selecting randomly for you! "
            restaurant = random.choice(ratings.keys())

        ratings[restaurant] = get_new_rating(restaurant)

    elif choice == 5:
        break

    else:
        print "Sorry, your options are more limited than that!  Please enter a valid number."
        # loop will ask again
