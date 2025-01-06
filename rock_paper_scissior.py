import random
def game():
    user_count=0
    computer_count=0
    print("Welcome to Rock, Paper, Scissors!")
    while True:        

        print("Enter your choice:")
        print("\n1.Start game")
        print("2.Exit game")
        try:
            user_choice=int(input("\nEnter your choice: "))
            if user_choice in [1,2]:
                if user_choice==1:
                    print("Starting game...")
                    user_count, computer_count=condition(user_count,computer_count)
                elif user_choice==2:
                    print("Exiting game.")
                    count(user_count,computer_count)
                    break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")
print("Game Over!")          

def condition(user_count,computer_count):
    while True:
        print("\nChoose your move:")
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Exit")
        try:
            user_choice=int(input("\nEnter your choice: "))
            if user_choice==4:
                print("Exiting game.")
                break
            if user_choice in [1,2,3]:
                computer_choice=random.randint(1,3)
                if user_choice==computer_choice:
                    print("It's a tie!")
                elif (user_choice==1 and computer_choice==3)or\
                    (user_choice==2 and computer_choice==1)or\
                    (user_choice==3 and computer_choice==2):
                    print("You win this round!")
                    user_count+=1    
                else:
                    print("You lose this round!")
                    computer_count+=1
                print(f"current score: User {user_count} - Computer {computer_count}")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a numeric choice.")
    return user_count,computer_count    
def count(user_count,computer_count):
    print(f"Score: User {user_count} - Computer {computer_count}")
    if user_count>computer_count:
        print("Congratulations! You win the game.")
    elif user_count<computer_count:
        print("You lose the game.")
    else:
        print("It's a tie.")
      
if __name__=="__main__":
    game()  