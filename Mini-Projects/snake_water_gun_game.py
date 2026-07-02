# Day 38- Snake Water Gun Game
# A menu-driven Python implementation of the classic Snake-Water-Gun game where the user plays against the computer. The program validates user input, determines the winner based on game rules, maintains cumulative scores across multiple rounds, and provides a scoreboard to track wins, losses, and draws.



import random

def play_game():
    user_choice = input("Enter Snake, Water, Gun: ").lower()
    computer_choice = random.choice(["snake", "water","gun"])

    print("You chose:",user_choice)
    print("Computer chose:",computer_choice)


    if user_choice not in ["snake", "water", "gun"]:
        print("Invalid choice")
        return 0,0,0

    if user_choice == computer_choice:
        print("Draw")
        return 1,0,0
       
    elif(
        (user_choice =="water" and computer_choice =="gun")
        or (user_choice =="snake" and computer_choice =="water") 
        or (user_choice =="gun" and computer_choice =="snake")
        ):
        print("Winner is user")
        return 0,1,0
        
    else:
        print("Winner is computer")
        return 0,0,1
        


def view_score(draw,user_score,computer_score):
    print("\nScore Board")
    print("Draws",draw)
    print("User score",user_score)
    print("Computerscore",computer_score)
    
    
def main():
    draw = 0
    user_score = 0
    computer_score = 0
    while True:
        try:
            choice = int(input("Menu\n1-Play game\n2-View Score\n3-Exit\n"))

            match choice:
                case 1:
                    round_draw, round_user,round_computer = play_game()
                    draw+=round_draw
                    user_score+=round_user
                    computer_score+=round_computer
                    
                case 2:
                    view_score(draw,user_score,computer_score)
                case 3:
                    print("Exit")
                    break
                case _:
                    print("Wrong choice")
        
        except ValueError:
            print("Non-numeric constant")
            

main()