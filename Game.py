import os
while 1:
	p=input("Enter Name of Game to play or Quit to quit: ")
	type(p)
	if p=="Hangman":
		os.system("python3 hangman.py")
	elif p=="Spell It":
		os.system("python3 Spell_It.py")	
	elif p=="Quit":
		print("Goodbye")
		break
