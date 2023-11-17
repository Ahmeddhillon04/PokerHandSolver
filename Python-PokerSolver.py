# CPS109_Assignment_1
# Name: Ahmed Dhillon
# Student number: 501176485

"""Problem: This code is a poker hand solver.
 It takes in 2 completely random poker hands which are a set of 5 cards and then lets the user know which hand won and what rule they won by.
 The poker hand rankings consist of High card, Pairs, Two pairs, Three of a kind, Straight, Flush, Full house,
 Four of a kind, Straight flush, Royal flush all in increasing order. """

# Firstly I imported the random namespace in order to generate random poker hands
import random
# I created 2 variables, Values and Type which are lists containing all the suits and values of poker cards
# The values are strings as they can be indexed
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
type_ = ["C", "D", "H", "S"]
# This function takes random indexes from both lists and put them together creating random hands


def picking_cards():
    random_value = random.randrange(len(values))
    random_type = random.randrange(len(type_))
    card_input = values[random_value] + type_[random_type]
    return card_input
# Created an empty list for hand 1


hand_1 = []
# For loop to call picking cards function 5 times and appending it to the empty hand 1 list as hands consist of 5 cards
for i in range(5):
    hand_1.append(picking_cards())
# Same thing for hand 2
hand_2 = []
for i in range(5):
    hand_2.append(picking_cards())
# I am printing hand 1 to show the user what the hand 1 looks like
print(f"hand 1: {hand_1}")
# I am printing hand 2 to show the user what hand 2 looks like
print(f"hand 2: {hand_2}")
# Function to attain the suit of the card


def suit(card):
    # Returns the last index of the input which would be the suit
    return card[-1]
# Function to attain the value of the card


def value(card):
    # return the first index of the card which would be the value
    return card[0]
# Function to create a list of all the suits in a hands, this will allow me to check for things like flush


def makeSuitList(hand):
    # empty list result
    result = []
    # for loop to iterate over items in hand
    for card in hand:
        # each suit will be appended to the empty list by calling the suit function created earlier
        result.append(suit(card))
    # returns the suit list
    return result
# Function to create a list of a values in a hand, this will allow me to check for things like straights


def makeValueList(hand):
    # Empty list result
    result = []
    # For loop to iterate over items in hand
    for card in hand:
        # each value will be appended to the empty list by calling the value function created earlier
        result.append(value(card))
    # returns the value list
    return result
# Function to convert the letters such as Ace, King, Queen to numerical values


def letterConvert(hand):
    # hand is argument which would be a value list
    hand_value_list = hand
    # for loop through each index of the value list I created above
    for i in range(len(hand_value_list)):
        # Checks if hand value list at index is equal to "A"
        if hand_value_list[i] == "A":
            # change "A" to 14 since Ace has the highest value in poker
            hand_value_list[i] = "14"
        # If the value at index i is equal to "J"
        if hand_value_list[i] == "J":
            # change "J" to 11 since J comes after 10
            hand_value_list[i] = "11"
        # If something equals to "Q"
        if hand_value_list[i] == "Q":
            # change it to 12
            hand_value_list[i] = "12"
        # If something equals to "K"
        if hand_value_list[i] == "K":
            # change it to 13
            hand_value_list[i] = "13"
    # list comprehension to convert each number from a string to an integer
    hand_value_list = [int(item) for item in hand_value_list]
    # Since the comprehension converts each item the number 10 is two items, and it creates a problem
    # for loop to go over the new hand value list
    for i in range(len(hand_value_list)):
        # Checks if there is a one
        if hand_value_list[i] == 1:
            # if there is it changes it to 10 since the only way there can be a 1 is if came from a 10
            hand_value_list[i] = 10
    # returns the new value list
    return hand_value_list
# Function to count the amount of occurrences of the values, using a hashmap
# takes in hand value list


def makeHashMap(hand):
    # empty dictionary called mapValue
    mapValue = {}
    # for loop to go through hand value list through index
    for i in range(len(hand)):
        # each item becomes the key for the hashmap
        # The value for the hashmap is the time the items is found in the list which is found by .count method
        mapValue[hand[i]] = hand.count(hand[i])
    # returns a hashmap of items in value list and amount of times the items occur
    return mapValue


# using the function the creates a value list, I create a value list for hand 1
hand1Values = makeValueList(hand_1)
# Create value list for hand 2
hand2Values = makeValueList(hand_2)
# using function that creates the suit list, I create a suit list for hand 1
hand_1_suit_list = makeSuitList(hand_1)
# create a suit list for hand 2
hand_2_suit_list = makeSuitList(hand_2)

# Pass both value lists through the letter converter function to change letters to numerical values
hand_1_value_list = letterConvert(hand1Values)
hand_2_value_list = letterConvert(hand2Values)
# create hashmap for hand one 1 by passing through to the hand hashmap function
valueMap1 = makeHashMap(hand_1_value_list)
# create hashmap for hand one 1 by passing through to the hand hashmap function
valueMap2 = makeHashMap(hand_2_value_list)


# checks if there is a flush ( all suit are the same)
# takes it 1 argument, suit list
def check_flush(hand_1):
    # checks if all but the last element are the same as everything but the first element
    if hand_1[:-1] == hand_1[1:]:
        # if they are all the same element it returns True meaning it's a flush
        return True
    # else its a False
    else:
        return False
# checks if hand is a straight ( the values go up in a consecutive order )
def check_striaght(hand_1):
    # sorts the hand
    hand_1.sort()
    r = 1
    # for loop goes through elements backwards
    for l in range(len(hand_1)-1):
        # checks if hand at r is not equal to hand at l + 1 which means it is not consecutive
        if hand_1[r] != hand_1[l] + 1:
            # not consecutive, returns False
            return False
        # if it is true it adds 1 to r and continues checking
        r = r + 1
    # returns True if all is consecutive
    return True
# checks for 3 of kind ( if there are 3 occurrences of a value)
def check_3OfKind(mapValue):
    # checks if 3 is found in values of hashmap
    if 3 in mapValue.values():
        return True
    return False
# checks for 4 of a kind ( if there are 4 occurrences of a value)
def check_4OfKind(mapValue):
    # checks if 3 is found in values of hashmap
    if 4 in mapValue.values():
        return True
    return False
# checks for a pair ( pair of value )
def check_pairs(mapValue):
    # if 2 is found in value of hashmap
    if 2 in mapValue.values():
        return True
    return False
# checks for full house ( 3 occurences of a value and a pair )
def check_fullHouse(mapVal):
    # checks if the pairs function is True and the 3 of the kind function is also True
    if check_pairs(mapVal) == True and check_3OfKind(mapVal) == True:
        return True
    return False
# checks for 2 pairs of values
def check_twoPairs(mapValue):
    # counter
    counter = 0
    # goes through keys and values
    for key, value in mapValue.items():
        # if the value is 2
        if value == 2:
            # adds to the counter
            counter = counter + 1
    # returns True if counter is 2 meaning 2 pairs and returns False otherwise
    return True if counter == 2 else False

# Check if al the cards are royals ( not a poker hand rank but to make life easier )
def check_royal(hand_1):
    # Checks if all values are greater than or equal to 10
    for i in hand_1:
        if i >= 10:
            return True
    return False

# function to check it is a royal flush ( all royal cards including 10 and a flush)
# takes in 2 arguments
def check_royalFlush(hand, suit):
    # Using the function created (check_royal, check_straight, check_flush) it checks if all are True
    if check_royal(hand) == True and check_striaght(hand) == True and check_flush(suit) == True:
        # if they are it returns True meaning it is a royal flush
        return True
    # otherwise it returns False
    return False

# checks or a straight flush (both consecutive and a flush )
def check_striaghtFlush(hand, suit):
    if check_striaght(hand) and check_flush(suit):
        return True
    return False


# high card , gets the max card
def find_highCard(hand):
    return max(hand)


# uses hashmap to output result
hand1_is = {"hand": "", "value": 0}
hand2_is = {"hand": "", "value": 0}

# if statements to check which hand ranking it is
# checks in order
# since royal flush is the highest ranking I gave it the highest value
# also changes key to poker hand ranking
# checks all ranking for hand 1
if check_royalFlush(hand_1_value_list, hand_1_suit_list):
    hand1_is["hand"] = "Royal Flush"
    hand1_is["value"] = 10
elif check_striaghtFlush(hand_1_value_list, hand_1_suit_list):
    hand1_is["hand"] = "Straight Flush"
    hand1_is["value"] = 9
elif check_4OfKind(valueMap1):
    hand1_is["hand"] = "4 of a kind"
    hand1_is["value"] = 8
elif check_fullHouse(valueMap1):
    hand1_is["hand"] = "Full House"
    hand1_is["value"] = 7
elif check_flush(hand_1_suit_list):
    hand1_is["hand"] = "Flush"
    hand1_is["value"] = 6
elif check_striaght(hand_1_value_list):
    hand1_is["hand"] = "Straight"
    hand1_is["value"] = 5
elif check_3OfKind(valueMap1):
    hand1_is["hand"] = "3 Of a Kind"
    hand1_is["value"] = 4
elif check_twoPairs(valueMap1):
    hand1_is["hand"] = "2 of a kind"
    hand1_is["value"] = 3
elif check_pairs(valueMap1):
    hand1_is["hand"] = "1 pair"
    hand1_is["value"] = 2
else:
    hand1_is["hand"] = "High card"
    hand1_is["value"] = 1

# checks all hand ranking for hand 2
# same code
if check_royalFlush(hand_2_value_list, hand_2_suit_list):
    hand2_is["hand"] = "Royal Flush"
    hand2_is["value"] = 10
elif check_striaghtFlush(hand_2_value_list, hand_2_suit_list):
    hand2_is["hand"] = "Straight Flush"
    hand2_is["value"] = 9
elif check_4OfKind(valueMap2):
    hand2_is["hand"] = "4 of a kind"
    hand2_is["value"] = 8
elif check_fullHouse(valueMap2):
    hand2_is["hand"] = "Full House"
    hand2_is["value"] = 7
elif check_flush(hand_2_suit_list):
    hand2_is["hand"] = "Flush"
    hand2_is["value"] = 6
elif check_striaght(hand_2_value_list):
    hand2_is["hand"] = "Straight"
    hand2_is["value"] = 5
elif check_3OfKind(valueMap2):
    hand2_is["hand"] = "3 Of a Kind"
    hand2_is["value"] = 4
elif check_twoPairs(valueMap2):
    hand2_is["hand"] = "2 pairs"
    hand2_is["value"] = 3
elif check_pairs(valueMap2):
    hand2_is["hand"] = "1 pair"
    hand2_is["value"] = 2
else:
    hand2_is["hand"] = "High card"
    hand2_is["value"] = 1

# compares both hands values and tells who won and what they won by
if hand1_is["value"] > hand2_is["value"]:
    print("Hand 1 won by", hand1_is["hand"])
elif hand2_is["value"] > hand1_is["value"]:
    print("Hand 2 won by", hand2_is["hand"])
elif hand1_is["value"] == hand2_is["value"] and hand1_is["value"] != 1:
    print("TIE, by", hand1_is["hand"])
# since high card is a special case, I compared which high card has a higher value
else:
    if find_highCard(hand_1_value_list) > find_highCard(hand_2_value_list):
        print("Hand 1 won by high card")
    elif find_highCard(hand_1_value_list) < find_highCard(hand_2_value_list):
        print("Hand 2 won by high card")
    else:
        print("TIE by same high card")
