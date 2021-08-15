import random

choice = ["no"or "NO" or "No"]

def rock_paper_scissors():
    player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
    choices = ['r','s','p']
    opponent = random.choice(choices)

    if player == opponent:
        return print(f"Its a Tie! My choice is {opponent}")

    if check_win(player, opponent):
        return print(f"Yay! you won! My choice is {opponent}")
    
    if check_win(player, opponent) != True:
        return print(f"You lost! My choice is {opponent}")

    
def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True

continue_1 = "yes"
while continue_1 not in choice:
    rock_paper_scissors()
    continue_1 = str(input("Do you wish to continue?: "))
else:
    print("Thank you for playing with me :)")
