def main():  
  import random
  # import readchar
  import keyboard
  import sys
  import numpy


  # Create a list of hangman words
  wordList = ["cat","dog","mouse", "giraffe", "otter", "shark", "sheep", "car", "motorbike",
  "bus", "aeroplane", "pizza", "chips", "cheese"]

  # Intructions for the player
  print("************* game start *************\n".upper())
  print("instructions:\n".upper())
  print("* " + "Only the first letter is registered for your guess".capitalize())
  print("* " + "After 8 unsuccessful attempts you will receive a hint".capitalize())
  print("* " + "your score will be added to a leaderboard at the end of each game".capitalize())

  # Choose a word from the list at random
  wordChosen = random.choice(wordList)

  # Create an empty list to store the used letters
  used = []

  # Counter stops the game once all letters have been guessed correctly
  attempts = 0

  # Create a variable to store and display the player's guesses  
  display = wordChosen
  for i in range (len(display)):
    #replace each letter with a '_'
    display = display[0:i] + "_" + display[i+1:]
    
  # Put a space between each dash
  print(" ".join(display))

  # Keep asking the player until all letters are guessed
  while display != wordChosen:
    guess = input(str("Please enter a guess for the {} ".format(len(display)) + "letter word: "))#[0]
    guess = guess.lower()
    #Add the players guess to the list of used letters
    used.extend(guess)
    print ("Attempts: ")
    print (attempts)

    print(wordChosen) # Added for testing

    # Provide a hint if unsuccessful after 7 attempts
    if attempts >= 7 and guess != wordChosen and wordChosen in wordList[0:6]:
      print("HINT: It's an animal")
    elif attempts >= 7 and guess != wordChosen and wordChosen in wordList[7:11]:
      print("HINT: It's a vehicle!")
    elif attempts >= 7 and guess != wordChosen and wordChosen in wordList[11:14]:
      print("HINT: It's food!")  

    # Allow the player to exit the game, 
    # Currently uses temrinal function of ctrl + c

    # while True:
    #  if keyboard.read_key() == 'esc':
    #   print("Exiting...")
    #   sys.exit(0) # this exits your program with exit code 0
    #  else:
    #     break

    # Search through the letters in answer
    for i in range(len(wordChosen)):
      if wordChosen[i] == guess:
        display = display[0:i] + guess + display[i+1:]

    print("Used letters: ")
    print(used)
        
    # Print the string with guessed letters (with spaces in between))
    print(" ".join(display))

    # Create a space for formatting  
    print("\n")

    # Add +1 to attempts after each guess
    attempts = attempts + 1

  print("Well done, you guessed '" + str(wordChosen) + "' right in " + str(attempts) + " attempts!")

  # Ask the player whether they want to retry
  while display == wordChosen:
      tryAgain = str(input("Try again: (Y = yes / N = no)"))
      tryAgain = tryAgain.lower()
      if tryAgain == "y" or tryAgain == "yes":
        print(tryAgain) # for testing just to see whether its being picked up
        main()
      elif tryAgain == "n" or tryAgain == "no":
        exit()
        print("else")
      else:
        print("Invalid input. Please use (Y = yes / N = no)")
        print("\n")

main()


# TO DO -------------
# add a quit function,
# create a scoreboard to store the number of attempts, name, date and time, 
# fix the hints to reflect which word was chosen, 
# add a name for each player at the start of each game
# fix bug if 'enter' and 'esc'is pressed then error occurs 
# 

# Done list -----------
# Basic game function
# Display how many turns the player took to get the guess correct
# Setup GIT repo
#
#
#




