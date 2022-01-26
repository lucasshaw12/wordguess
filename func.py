import random
import csv

def enter_name():
  global myName
	# Ask the a player for their username
  print("What is your username:")
  myName = input()[0:6]
  print("\n")
  while myName.isspace() or myName.isdigit() or myName == "":
      print("Invalid character, please use letters!\n")
      myName = input()[0:6]
  print("Hi, " + str(myName) + ", welcome to the Word Guessing Game!")
  print("\n")

def retry_game():
	# Ask the player whether they want to retry
	# Choose a word from the list at random
	tryAgain = str(input("Try again: (Y = yes / N = no)"))
	tryAgain = tryAgain.lower()
	if tryAgain == "y" or tryAgain == "yes":
	  from wordguess import main
	elif tryAgain == "n" or tryAgain == "no":
	  exit()
	  print("else")
	else:
	  print("\n")
	  print("Invalid input. Please use (Y = yes / N = no)")
	  print("\n")

def choose_word():
	# Create a list of hangman words
	global wordList
	wordList = []
	with open('worddict.csv', encoding='utf-8-sig') as outputFile:
	  outputReader = csv.reader(outputFile)
	  for row in outputReader:
	    wordList.append(row[0])  
	outputFile.close()


