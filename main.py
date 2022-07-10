import random


is_running = True

# Run loop
while is_running:
    # Roll dice
    roll = random.randint(1, 6) #Dice option is between 1and 6 (1 and 6 included)

    # Print roll result
    if roll == 1:
        print("[0]")

    if roll == 2:
        print("[00]")
    
    if roll == 3:
        print("[000]")
    
    if roll == 4:
        print("[0000]")
    
    if roll == 5:
        print("[00000]")
    
    if roll == 6:
        print("[000000]")
    
    

    # Check wheather to terminate the loop
    roll_again = input("Would you like to roll again (y/n)? ")
    if roll_again == "y":
        pass 
    
    if roll_again == "n":
        is_running = False 
        # This is the same thing as a break.-      