import numpy as np
import random
import pandas as pd
import sys   #sys.exit()
import time
from IPython.display import Image
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

def poker (number):                                 # Takes number 1~52 as inputs, output card's face value and suit.
    suit = "suit"
    card = "card"
    if (number % 13) <= 10 and (number % 13) > 1:   # Face value
        card = str((number % 13))
    elif (number % 13) == 11:
        card = "J"
    elif (number % 13) == 12:
        card = "Q"
    elif (number % 13) == 0:
        card = "K"   
    elif (number % 13) == 1:
        card = "A" 
        
    if number % 13 == 0:                            # So that 1-13, 14-26, 27-39, 40-53 have the same suit
        if (number // 13)-1 % 4 == 0:
            suit = "Spades"
        elif (number // 13)-1 % 4 == 1:
            suit = "Hearts"
        elif (number // 13)-1 % 4 == 2:
            suit = "Diamonds"
        elif (number // 13)-1 % 4 == 3:
            suit = "Clubs"
    else:                                           # Suit
        if (number // 13) % 4 == 0:
            suit = "Spades"
        elif (number // 13) % 4 == 1:
            suit = "Hearts"
        elif (number // 13) % 4 == 2:
            suit = "Diamonds"
        elif (number // 13) % 4 == 3:
            suit = "Clubs"
    output = card + " of " + suit
    return output

def find_first_one (num):     # used in card_value() 
    index = 1
    boo = [0] * len(num)
    for i in range(0, len(num)):
        if num[i] == 1 :
            boo[i] = index
            index = index + 1
    return int(boo.index(1))


def card_value (num):     # Take numbers as input, output face value of the card
    if type(num) == int:
        value = 0
        if num == 0:
            value = 0
        elif num % 13 == 0:
            value = 10
        elif num % 13 < 10:
            value = num % 13
        elif num % 13 >= 10:
            value = 10
        return value
    elif type(num) == np.ndarray or type(num) == list:   # takes list or array as input
        number_of_As = num.count(1) + num.count(14) + num.count(27) + num.count(40)      # calculate the number of As
        value = [0] * len(num)
        for i in range(0, len(num)):
            if num[i] == 0:
                value[i] = 0
            elif num[i] % 13 == 0:
                value[i] = 10
            elif num[i] % 13 < 10:
                value[i] = num[i] % 13
            elif num[i] % 13 >= 10:
                value[i] = 10
        # every number in value is a number between 1-10
        for i in range(0, len(num)):                
            if number_of_As == 1 and sum(value) <= 11:       # only one A, the A has a face value of 11
                index = find_first_one(value)
                value[index] = 11    
            elif number_of_As == 2 and sum(value) <= 11:     # two As, the first A has a face value of 11
                index = find_first_one(value)
                value[index] = 11                                      
            elif number_of_As == 3 and sum(value) <= 11:     # three As, the first A has a face value of 11
                index = find_first_one(value)
                value[index] = 11 
            elif number_of_As == 4 and sum(value) <= 11:     # four As, the first A has a face value of 11
                index = find_first_one(value)
                value[index] = 11  
            elif number_of_As == 5 and sum(value) <= 11:     # five As, the first A has a face value of 11
                index = find_first_one(value)
                value[index] = 11  
        return np.array(value)

deck = list(range(1,53))
ordered_deck = list(range(1,53))

# Game starts here
print("*******************************")
print ("Welcome to Blackjack!")
print("*******************************")
name = input("What is your name? ")
game = 0
win = 0

play = True
while play == True:
    status = True
    computer = True
    deck = list(range(1,53))
    random.shuffle(deck)
    deck = np.array(deck)
    player_deck = [0] * 5
    computer_deck = [0] * 5
    player_deck[0:2] = deck[0:2]
    computer_deck[0:2] = deck[2:4]
    print("These are your two first cards: {} & {}.".format(poker(player_deck[0]), poker(player_deck[1])))
    Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(player_deck[0]), width = 56, height = 85) 
    Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(player_deck[1]), width = 56, height = 85) 
    player_points = sum(card_value(player_deck))
    computer_points = sum(card_value(computer_deck))
    print ("Your points: {}".format(player_points))
    # print ("Computer points: {}".format(computer_points))
    print("==========================")
    if sum(card_value(player_deck)) == 21:  # player gets a blackjack in the beginning.
        print ("Blackjack! Congratulations, {}!! You Win!!!".format(name))
        print("==========================")
        game = game + 1
        win = win + 1
        status = False
        computer = False

    while status == True:
        third = input("Hit(Y) or Stand(N)? ")                                       # player takes the third card (hit for the first time)
        if third == "Hit" or third == "Y":
            player_deck[2] = deck[4]
            player_points = sum(card_value(player_deck))
            print("Your third card is: {}.".format(poker(player_deck[2])))
            Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(player_deck[2]), width = 56, height = 85) 
            print("Now you hold 3 cards: {},  {} and {}.".format(poker(player_deck[0]), poker(player_deck[1]), poker(player_deck[2])))
            print ("Your points: {}".format(player_points))
            player_points = sum(card_value(player_deck))
            add = 1
            if player_points > 21:                                                  # player busted at the third card
                print("==========================")
                print("Busted! You Lose!")
                game = game + 1
                status = False
                computer = False
                break
            elif player_points == 21:
                print("==========================")
                print ("Blackjack! Congratulations, {}!! You Win!!!".format(name))
                game = game + 1
                win = win +1
                status = False
                computer = False
                break
            break
        elif third == "Stand" or third == "N":                                        # player decides to stand with 2 cards
            add = 0
            status = False
            break

    while status == True:
        print("==========================")
        fourth = input("Hit(Y) or Stand(N)? ")
        if fourth == "Hit" or fourth == "Y":                                          # player takes the fourth card
            player_deck[3] = deck[5]
            player_points = sum(card_value(player_deck))
            print("Your fourth card is: {}.".format(poker(player_deck[3])))
            Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(player_deck[3]), width = 56, height = 85) 
            print("Now you hold 4 cards: {},  {}, {} and {}.".format(poker(player_deck[0]), poker(player_deck[1]), poker(player_deck[2]), poker(player_deck[3])))
            print ("Your points: {}".format(player_points))
            player_points = sum(card_value(player_deck))
            add = 2
            if player_points > 21:                                                     # player busted at the fourth card
                print("==========================")
                print("Busted! You Lose!")
                status = False
                computer = False
                game = game + 1
                break
            elif player_points == 21:
                print("==========================")
                print ("Blackjack! Congratulations, {}!! You Win!!!".format(name))
                status = False
                computer = False
                game = game + 1
                win = win + 1
                break
            break
        elif fourth == "Stand" or fourth == "N":                                         # player decides stand with 3 cards
            print("==========================")
            add = 1
            status = False
            break
    print("==========================")
    while status == True:
        fifth = input("Hit(Y) or Stand(N)? ")
        if fifth == "Hit" or fifth == "Y":
            player_deck[4] = deck[6]
            player_points = sum(card_value(player_deck))
            print (player_deck)
            print("Your fifth card is: {}.".format(poker(player_deck[4])))
            Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(player_deck[4]), width = 56, height = 85) 
            print("Now you hold 5 cards: {},  {}, {}, {} and {}.".format(poker(player_deck[0]), poker(player_deck[1]), poker(player_deck[2]), poker(player_deck[3]), poker(player_deck[4])))
            print ("Your points: {}".format(player_points))
            player_points = sum(card_value(player_deck))
            add = 3
            if player_points > 21:
                print("==========================")
                print("Busted! You Lose!")                                                  # player busted at the fifth card
                game = game + 1
                status = False
                computer = False
                break
            elif player_points == 21:
                print("==========================")
                print ("Blackjack! Congratulations, {}!! You Win!!!".format(name))
                game = game + 1
                win = win + 1
                status = False
                computer = False
                break
            elif player_points < 21:
                print("==========================")
                print ("Congratulations, {}!! You got a Charlie! You Win!!!".format(name))
                game = game + 1
                win = win + 1
                status = False
                computer = False
                break
            break
        elif fifth == "Stand" or fifth == "N":                                                  # player stands with 4 cards
            print("==========================")
            status = False
            add = 2
            break

     # computer's turn       
    while computer == True:
        time.sleep(1)
        print("computer cards: {} & {}".format(poker(computer_deck[0]), poker(computer_deck[1])))
        Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(computer_deck[0]), width = 56, height = 85)
        Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(computer_deck[1]), width = 56, height = 85)
        if sum(card_value(computer_deck)) == 21:  # the computer gets a blackjack with the first two cards
            print ("Computer got a Blackjack! Sorry, {}. You lose.".format(name))
            print("==========================")
            game = game + 1
            status = False
            computer = False
            break
        
        print("computer points: {}".format(computer_points))
        if (computer_points < 17) or (computer_points < player_points):  # Computer's face value is less than 17 or less than player's face value, has to hit
            print("==========================")
            time.sleep(1)
            print("Computer decides to take a card.")
            computer_deck[2] = deck[4+add]
            Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(computer_deck[2]), width = 56, height = 85)
            computer_points = sum(card_value(computer_deck))
            print("computer cards: {}, {} & {}".format(poker(computer_deck[0]), poker(computer_deck[1]), poker(computer_deck[2])))
            print("computer points: {}".format(computer_points))
            if computer_points > 21:
                print("==========================")
                print ("Computer has busted! {}, you win!".format(name))  # computer busted on the third card
                game = game + 1
                win = win + 1
                computer = False
                break
            elif computer_points == 21:  # computer gets a blackjack with 3 cards
                print("==========================")
                print ("Computer got a Blackjack! Sorry, {}. You lose.".format(name))
                game = game + 1
                status = False
                computer = False
                break
            elif computer_points >= player_points:
                print("==========================")
                print("Your points: {}. Computer points: {}.".format(player_points, computer_points))
                print ("Computer got a higher score! Sorry, {}. You lose.".format(name))
                game = game + 1
                status = False
                computer = False
                break
            else:                                                                              # computer did not bust with three cards
                break
        else:
            print("==========================")                          #  computer stands with three cards. (computer > player and computer > 17), computer wins
            print("Computer holds.")
            print("Your points: {}. Computer points: {}.".format(player_points, computer_points))
            print("==========================")
            print("Sorry, {}. You lose.".format(name))
            game = game + 1
            computer = False
            break

    while computer == True: 
        time.sleep(2)
        print("==========================")
        print("Computer decides to take another card.")                 # computer takes the fourth card
        computer_deck[3] = deck[4+add+1]
        Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(computer_deck[3]), width = 56, height = 85)
        computer_points = sum(card_value(computer_deck))
        print("computer points: {}".format(computer_points))
        print("computer cards: {}, {}, {} and {}".format(poker(computer_deck[0]), poker(computer_deck[1]), poker(computer_deck[2]), poker(computer_deck[3])))
        if computer_points > 21:
            print("==========================")
            print ("Computer has busted! {}, you win!".format(name))  # computer busted on the fourth card
            game = game + 1
            win = win + 1
            computer = False
            break
        elif computer_points == 21:  # computer gets a blackget on the fourth card
            print("==========================")
            print ("Computer got a Blackjack! Sorry, {}. You lose.".format(name))
            game = game + 1
            status = False
            computer = False
            break 
        elif computer_points >= player_points:                              # computer wins on the forth card
            print("==========================")                       
            print("Your points: {}. Computer points: {}.".format(player_points, computer_points))
            print("Sorry, {}. You lose.".format(name))
            game = game + 1
            computer = False
            break
        else: 
            computer = True                                               # computer still hasn't win after four cards
            break


    while computer == True:
        time.sleep(2)
        print("Computer decides to take the fifth card.")                 # computer takes the fifth card.
        computer_deck[4] = deck[4+add+2]
        computer_points = sum(card_value(computer_deck))
        Image(filename = "/Users/IanChuang/Desktop/Poker/{}.png".format(computer_deck[4]), width = 56, height = 85)
        if computer_points > 21:
            print("==========================")
            print("New Card: {}".format(poker(computer_deck[4])))
            print("computer cards: {}, {}, {}, {} and {}".format(poker(computer_deck[0]), poker(computer_deck[1]), poker(computer_deck[2]), poker(computer_deck[3]), poker(computer_deck[4])))
            print("Computer points: {}".format(computer_points))
            print ("Computer has busted! {}, you win!".format(name))       # computer busted on the fifth card.
            game = game + 1
            win = win + 1
            break
        elif computer_points == 21:
            print("==========================")                              # computer gets a blackjack on the fifth card.
            print ("Computer got a Blackjack! Sorry, {}. You lose.".format(name))
            game = game + 1
            status = False
            computer = False
            break 
        else:
            print("==========================")
            print("Computer draws a Charlie.")
            print("Sorry, {}. You lose.".format(name))
            game = game + 1
            break

    time.sleep(0.5)
    again = input("Play again? (Y / N) ")
    if again == "Y":
        print("==========================")
        play = True
    elif again == "N":
        play = False
        break
    else:
        while True:
            again = input("Play again? (Y / N) ")
            if again == "Y":
                print("==========================")
                play = True
                break
            elif again == "N":
                play = False
                break
time.sleep(0.5)                
print("==========================")
print ("Games played: {}".format(game))
print ("Games won: {}".format(win))
print ("Your winning percentage: {0:.2f}%". format((win/game) * 100))
print("==========================")
time.sleep(0.5)
print("{}, thank you for playing!".format(name))



"""
About the game:
This is a one player vs computer blackjack. Player wins by one of the following condition:
1) getting a blackjack (21 points)
2) getting 5 cards without busting 
3) getting higher points than the computer (which is impossible in this game)

Because the computer plays according to the player's point, computer has an advantage over the player. 
The computer will always hit when it has fewer points than the player.

"""

