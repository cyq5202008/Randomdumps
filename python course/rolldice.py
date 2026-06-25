import random
def rolldice():
    return random.randint(1, 6)

def main():
    print("Welcome to Dice Roll Simulator!")
    while True:
        input("Press Enter to roll the dice...")
        result =rolldice()
        print(f"You have Rolled a {result}!")
        roll_again = input("Do you want to reroll? (yes/no):").strip() .lower()
        if roll_again != 'yes':
            print("Thanks For Playing!")

if __name__=="__main__":
    main()       