import random
import subprocess
f=open("./Wordlist.csv", 'r')
rows=f.read().split("\n")
while 1:
	k=0
	print("Spell It!")
	string=""
	str1=""
	my_randoms=random.sample(range(0, len(rows)), 1)
	column=rows[my_randoms[0]].split(",")
	randcolumn=random.sample(range(0, (len(column)-1)), 1)
	column[randcolumn[0]]=column[randcolumn[0]].strip()
	answer=input(subprocess.call(["espeak","-s","100"," Spell "+column[randcolumn[0]]]))
	type(answer)
	if answer==column[randcolumn[0]]:
		subprocess.call(["espeak", "Good"])
	
	else:
		subprocess.call(["espeak","-s","100", "No you spelt wrong the answer will be "])
		for i in range(0,len(column[randcolumn[0]])): 
			print(column[randcolumn[0]][i], end='')
			subprocess.call(["espeak","-s","150", column[randcolumn[0]][i]])
		print("\n")
	u=input("Do you want to continue?")
	type(u)
	if u=="No":
		break
