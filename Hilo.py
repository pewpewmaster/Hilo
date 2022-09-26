import random


class Card:

    def __init__(self, value):
        self.value = value

    def show(self):
        print ("The card is: " + str(self.value))
    
    def show_next(self):
        print ("Next card was: " + str(self.value))


class Person:

    def __init__(self, point):
        self.point = point
        self.player_choice = "y"

    def guess(self, card, card_1):
        
        # Use while loop prevent typeing random stuff
        while True:
            
            guess = str(input("Higher or lower? [h/l] "))

            if (card_1.value > card.value and guess == "h") or (card_1.value < card.value and guess == "l"):
                #print ("You win!")
                self.point += 100
                break
            elif (card_1.value > card.value and guess == "l") or (card_1.value < card.value and guess == "h"):
                #print ("You lose!")
                self.point -= 75
                if self.point < 0:
                    quit()
                break
            elif card_1.value == card.value:
                #print ("Draw!")
                self.point += 0
                break
            else:
                continue

    def choice(self):
        choice = str(input("Play again? [y/n] "))
        self.player_choice = choice


# Player start with 300 points 
player = Person(300)

# creat a new card
k = random.randint(1,13)
card = Card(k)

while True:

    print()

    # show card
    card.show()

    k_1 = random.randint(1,13)
    card_1 = Card(k_1)

    # player guess the card
    player.guess(card, card_1)

    # show card_1
    card_1.show_next()

    #change card to card_1
    card = card_1

    print("The score is " + str(player.point))

    # player choose if continue
    player.choice()

    if player.player_choice == "y":
        continue

    elif player.player_choice == "n":
        #print ("GG")
        break

    else:
        break







        

        








