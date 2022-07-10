import random


print("WELCOME TO DICE ROLLING SIMULATOR!!!")
is_running = True

# Roll dice function
def roll_dice():
    rolls = []
    for throw in range(num_of_dice):            
        # Roll dice
        roll = random.randint(1, 6) #Dice option is between 1and 6 (1 and 6 included)

        # Create dice appearance
        if roll == 1:
            roll = [1]
        if roll == 2:
            roll = [2]
        if roll == 3:
            roll = [3]
        if roll == 4:
            roll = [4]
        if roll == 5:
            roll = [5]
        if roll == 6:
            roll = [6]

        rolls.append(roll)
        
    
    print(rolls)

# Run loop
while is_running:
    print("Simulator is running...")
    
    # Input number of dice you want roll
    try:
        num_list = [1, 2, 3, 4, 5]
        num_of_dice = int(input("How many dice do you want to roll (maximum of 5)?\n"))
        if num_of_dice in num_list:
            roll_dice()
        else:
            if num_of_dice > 5:
                print("Option is more than maximum allowed dice")
            if num_of_dice < 1:
                print("Option is less than minimum allowed dice")
    except:
        print("Option is not a number")
    
    # Check wheather to terminate the loop
    roll_again = input("Would you like to roll again (y/n)? ")
    if roll_again == "y":
        pass 
    
    if roll_again == "n":
        print("Stopping simulator... ")
        print("THANKS FOR USING DICE ROLLING SIMULATOR!!!")
        is_running = False 
        # This is the same thing as a break.-      
