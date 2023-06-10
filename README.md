# Dice_Rolling_Simulator
This code is a simple dice rolling game implemented in Python. It allows the user to roll a virtual six-sided die as many times as they want. Here's a summary of how the code works:

The random module is imported, which provides functions for generating random numbers.

The welcome message is printed to the console, greeting the player.

The code enters an infinite loop using while (True):. This means the following code block will keep executing repeatedly until a break statement is encountered.

Inside the loop, random.randint(1, 6) generates a random integer between 1 and 6, simulating a dice roll. The result is printed to the console.

The code prompts the user for input with the message "If you want to roll the dice again, press 'y'; otherwise, press 'n'".

The input from the user is stored in the variable roll_again using the input() function.

If the value of roll_again is equal to 'y', the code uses the continue statement to go back to the beginning of the loop, allowing the user to roll the dice again.

If the value of roll_again is anything other than 'y', the code uses the break statement to exit the loop, terminating the program.

In summary, this code provides a simple interactive experience where the user can roll a virtual die repeatedly until they choose to stop.
