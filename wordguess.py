def main():  
  import random
  import datetime, time
  import sys
  import csv
  import keyboard
  
  # Create a list of hangman words
  wordList = ["cat","dog","mouse", "giraffe", "otter", "shark", "sheep", "car", "motorbike",
  "bus", "aeroplane", "pizza", "chips", "cheese"]

  # Intructions for the player
  print("""\n
************* GAME START *************\n
INSTRUCTIONS:\n
* Only the first letter is registered for your guess
* After 10 unsuccessful attempts you will receive a hint
* You will be prompted to include a username for each game (min of 3 characters - max of 6 characters)
* Your score will be added to a leaderboard at the end of each game""")


  # Choose a word from the list at random
  wordChosen = random.choice(wordList)

  # Create an empty list to store the used letters
  used = []

  # Counter stops the game once all letters have been guessed correctly
  attempts = 1

  # Create a variable to store and display the player's guesses  
  display = wordChosen
  for i in range (len(display)):
    #replace each letter with a '_'
    display = display[0:i] + "_" + display[i+1:]
  # Put a space between each dash
  print(" ".join(display))

  # Ask the a player for their username - WORKS - COMMENTED FOR TESTING SPEED
  print("What is your username (Max 6 letters): ")
  myName = input()[0:6]
  print("\n")
  while len(myName)==0:
    print("Please enter your username (Max 6 characters in length):")
    myName = input()
  print("Hi, " + str(myName) + ", welcome to the Word Guessing Game!")
  print("\n")

  # # Set the allowed chars for the myName input
  specChar = "`[];'./§~`{}|:?><"
  # while len(myName) == 0:
  #   print("Please enter your username (Max 6 letters):")
  #   myName=input()
  # print("Hi, " + str(myName) + ", welcome to the Word Guessing Game!")
  # print("\n") 

  # Keep asking the player until all letters are guessed
  while display != wordChosen:
    guess = input(str("Please enter a guess for the {} ".format(len(display)) + "letter word: "))[0:1]
    if guess.isspace() or guess.isdigit() or guess == "" or guess == specChar:
      print("Invalid character, please use a single letter\n")
      continue
    guess = guess.lower()
    #Add the players guess to the list of used letters
    used.extend(guess)
    print("Attempts: ")
    print(attempts)

    print(wordChosen) # Added for testing

    # Provide a hint if unsuccessful after 7 attempts
    if attempts >= 10 and guess != wordChosen and wordChosen in wordList[0:6]:
      print("HINT: It's an animal")
    elif attempts >= 10 and guess != wordChosen and wordChosen in wordList[7:11]:
      print("HINT: It's a vehicle!")
    elif attempts >= 10 and guess != wordChosen and wordChosen in wordList[11:14]:
      print("HINT: It's food!")  

      # # Allow the player to exit the game, 
      # # Currently uses temrinal function of ctrl + c
      # if keyboard.read_key() == 'p':
      #   print("Exiting...")
      #   sys.exit(0) # this exits your program with exit code 0
      # else:
      #   break

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

    # Capture date and time of sucessful attempt
    if display == wordChosen:
      dt = datetime.datetime.now()
      dtFullDate = dt.day, dt.month, dt.year
      print('\n')

      # When successful, add the username to the scoreboard.csv file list and display (Excel)
      # Run a function that displays the scoreboard 
      # Add the round to the scoreboard
      with open('scoreboard.csv', 'a', newline='') as outputFile:
        outputWriter = csv.DictWriter(outputFile, ['Name', 'Date', 'Attempts', 'Word Chosen'])
        #outputWriter.writeheader()
        outputWriter.writerow({'Name' : myName, 'Date' : dtFullDate, 'Attempts' : attempts, 'Word Chosen' : wordChosen})
        #outputWriter.writerow([myName, dtFullDate, attempts, wordChosen])
        outputFile.close()

        # Display the scoreboard from the scoreboard.csv file
        print(("************* scoreboard *************\n".upper()))
        print("""Name     Date       Atmpt Word""")
        outputFile = open('scoreboard.csv')
        outputDictReader = csv.DictReader(outputFile, ['Name', 'Date', 'Attempts', 'Word Chosen'])
        for row in outputDictReader:
          print(row['Name'], row['Date'], row['Attempts'], row['Word Chosen'])
        outputFile.close()

  print("Well done " + myName.capitalize() + ", you guessed '" + str(wordChosen) + "' right in " + str(attempts) + " attempts!")

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
        print("\n")
        print("Invalid input. Please use (Y = yes / N = no)")
        print("\n")

main()


# TO DO -------------
# add a quit function,
# Add a header to the scoreboard.csv file without it writing after each gameround
# for the name input, ensure that a minimum of 3 characters are provided and only letters
# Refactor code = add classes, functions etc

# Done list -----------
# Basic game function
# Display how many turns the player took to get the guess correctly
# Setup GIT repo
# fix the hints to reflect which word was chosen, 
# add a name for each player at the start of each game - link that to the scoreboard
# Clean up the instruction, cleaner way to write multiple lines of 'print'
# Create a scoreboard to store the number of attempts, name, date and time, (currently prints the scoreboard each gameround)
# Remove operators from the printed text from the csv file
# fix bug if 'enter' and 'esc' is pressed on the guess stage then error occurs 
# Ensure no numbers are allowed within input() when guessing a letter