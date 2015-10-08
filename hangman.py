#!/usr/bin/python


import sys


from termcolor import colored


# hides user input
import getpass



# hang matrix
hang =  ([[ "  ,------,",       "",  "",  "" ],
          [ "  |      !",       "",  "",  "" ],
          [ "  |      ",        "",  "",  "" ],
          [ "  |     ",         " ",  "",  "" ],
          [ "  |      ",        "",  "",  "" ],
          [ "  |     ",         " ",  "",  "" ],
          [ "  |     ",         "",  "",  "" ],
          [ "----------------", "",  "",  "" ],
          [ "----------------", "",  "",  "" ]])





print "###############################"
print "###", 
print (colored ("Welcome to hangman game" , "cyan")),
print "###"
print "###############################\n"

# read word without displying characters and split to list
word = list(getpass.getpass("Please write word you wan to guess:\n"))


# initialize word
guess_word = ""


# word for adding guess letter
temp_guess_word = "-" * len(word)
temp_guess_word = list(temp_guess_word)



#print "Word has %i characters: \"%s\" \n" %  (len(word), ''.join(temp_guess_word))
#rint "Word has %i characters: \"%s\" \n" %  (len(word), ''.join(temp_guess_word))


print( "Word has " + (colored(len(word), "cyan" )) + " characters: \"" + (colored( ''.join(temp_guess_word), "cyan" )) + "\"\n" )


# initialize number of guesses
bad_guess = 0

# loop for guessing
while temp_guess_word != word:

	
	guess_letter = raw_input("Write your guess letter: ")


	# loop fo quessing whole word
	if len(guess_letter) > 1:
		if word == list(guess_letter):
			print ( colored("WIN! You guessed the whole word\n" , "green"))
			sys.exit()
		else:
			print (colored ("You typed wrong word, guess by one letter or by whole word", 'red'))
			#bad_guess = bad_guess+1


	# initialize switch
	letter_found = 0
	# loop for quessing by letter
	for i in xrange(len(word)):
		if  word[i] == guess_letter:
			temp_guess_word[i] = guess_letter
#			print "Letter found"
			print(colored("Letter found", "green"))
			letter_found = 1


	# print word with aklready found letters
	print ( "Guessing word: \"" + colored(''.join(temp_guess_word), "cyan") + "\"" ) 
#	print "Guessing word: \"%s\"" % ''.join(temp_guess_word)


	if letter_found == 1:
		pass
	else:
		bad_guess = bad_guess+1
		print (colored ("Wrong letter", 'red'))

      
#	for i in xrange(len(hang)):

	if bad_guess == 1:
		hang[2][2]="@"
	if bad_guess == 2:
		hang[3][2]="|"
	if bad_guess == 3:
		hang[3][1]="/"
	if bad_guess == 4:
		hang[3][3]="\\"
	if bad_guess == 5:
		hang[4][2]="|"
	if bad_guess == 6:
		hang[5][1]="/"
	if bad_guess == 7:
		hang[5][3]=" \\"
		print (colored ("You lost, you are hanged", 'red'))
	        for i in xrange(len(hang)):
			pic = (hang[i][0] +  hang[i][1] + hang[i][2] + hang[i][3])
			pic = colored(pic, 'red')
			print (pic)
#	                print "%s" % (hang[i][0] +  hang[i][1] + hang[i][2] + hang[i][3])		
		print( "Hidden word was: "  + colored( ''.join(word), "cyan" ))
       	        sys.exit()		



	# print show array
	for i in xrange(len(hang)):
		print "%s" % (hang[i][0] +  hang[i][1] + hang[i][2] + hang[i][3])
	print "\n"



print (colored ("YOU WIN!\n", 'green'))
