import random
choices = ["Rock", "Paper", "Scissors"]
player = False
cpu_score = 0
player_score = 0
while True:
    #print(computer)
    player = input("Rock, Paper or  Scissors? (type end to stop playing): ").capitalize()
    computer = random.choice(choices)
    ## Conditions of Rock,Paper and Scissors
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            cpu_score+=1
        else:
            print("You win!", player, "smashes", computer)
            player_score+=1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            cpu_score+=1
        else:
            print("You win!", player, "covers", computer)
            player_score+=1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            cpu_score+=1
        else:
            print("You win!", player, "cut", computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"Player:{player_score}")
        break


#alternative no points method:
#import random

#choice = ["no"or "NO" or "No"]

#def rock_paper_scissors():
    #player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
    #choices = ['r','s','p']
    #opponent = random.choice(choices)

    #if player == opponent:
        #return print(f"Its a Tie! My choice is {opponent}")

    #if check_win(player, opponent):
        #return print(f"Yay! you won! My choice is {opponent}")
    
    #if check_win(player, opponent) != True:
        #return print(f"You lost! My choice is {opponent}")

    
#def check_win(user, computer):
    #if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        #return True

#continue_1 = "yes"
#while continue_1 not in choice:
    #rock_paper_scissors()
    #continue_1 = str(input("Do you wish to continue?: "))
#else:
    #print("Thank you for playing with me :)")
