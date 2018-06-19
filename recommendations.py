from math import sqrt

# A dictionary of movie critics and their ratings of a small set of movies
critics = {"Lisa Rose": {"Lady in the water": 2.5, "Snakes on a plane": 3.5, "Just My Luck": 3.0,
                         "Superman Returns": 3.5, "You, Me and Dupree": 2.5, "The Night Listener": 3.0},
           "Gene Seymour": {"Lady in the water": 3.0, "Snakes on a plane": 3.5, "Just My Luck": 1.5,
                            "Superman Returns": 5.0, "You, Me and Dupree": 3.5, "The Night Listener": 3.0},
           "Michael Phillips": {"Lady in the water": 2.5, "Snakes on a plane": 3.0,
                                "Superman Returns": 3.5, "The Night Listener": 4.0},
           "Claudia Puig": {"Lady in the water": 2.5, "Snakes on a plane": 3.5, "Just My Luck": 3.0,
                            "Superman Returns": 4.0, "You, Me and Dupree": 2.5, "The Night Listener": 4.5},
           "Mick LaSalle": {"Lady in the water": 3.0, "Snakes on a plane": 4.0, "Just My Luck": 2.0,
                            "Superman Returns": 3.0, "You, Me and Dupree": 2.0, "The Night Listener": 3.0},
           "Jack Matthews": {"Lady in the water": 3.0, "Snakes on a plane": 4.0, "Just My Luck": 2.0,
                             "Superman Returns": 5.0, "You, Me and Dupree": 3.5, "The Night Listener": 3.0},
           "Toby": {"Snakes on a plane": 4.5, "Superman Returns": 4.0, "You, Me and Dupree": 1.0}
           }

print("\nRating given by Toby to movie Snakes on a plane = " + str(critics["Toby"]["Snakes on a plane"]))

print(1 / (1 + sqrt(pow(5 - 4, 2) + pow(4 - 1, 2))))


# Returns a distance based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared items
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0

    # Add up the squares of all the differences
    sum_of_squares = sqrt(sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                               for item in prefs[person1] if item in prefs[person2]]))

    return 1 / (1 + sum_of_squares)


print("\nEuclidean Distance between Lisa and Gene = " + str(sim_distance(critics, "Lisa Rose", "Jack Matthews")))


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    # Find the number of elements
    n = len(si)

    # If there are no ratings in common, return 0
    if n == 0:
        return 0

    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    # Sum up the squares
    sum1_sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2_sq = sum([pow(prefs[p2][it], 2) for it in si])

    # Sum up the products
    p_sum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    # Calculate the Pearson Score
    num = p_sum - (sum1 * sum2 / n)
    den = sqrt((sum1_sq - pow(sum1, 2) / n) * (sum2_sq - pow(sum2, 2) / n))
    if den == 0:
        return 0

    r = num / den

    return r


print("\nPearson Correlation Score = " + str(sim_pearson(critics, "Lisa Rose", "Jack Matthews")))
