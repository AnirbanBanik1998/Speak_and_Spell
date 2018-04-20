import random
import subprocess
import time
import os
f= open("../Wordlist.csv",'r')
rows=f.read().split("\n")
while 1:
	k=0
	j=0
	print("Spell It!")
	string=""
	str1=""
	answer=""
	my_randoms=random.sample(range(0, len(rows)), 1)
	column=rows[my_randoms[0]].split(",")
	randcolumn=random.sample(range(0, (len(column)-1)), 1)
	column[randcolumn[0]]=column[randcolumn[0]].strip()
	subprocess.call(["espeak","-s","100"," Spell "+column[randcolumn[0]]])
	while j<len(column[randcolumn[0]]):
		time.sleep(3)
		with open('decode.txt','r') as r:
						
			arr=r.read().split("\n")
			n=len(arr)-1
			while arr[n]=="" and n>0:
				n=n-1
			letter=arr[n]
		print(letter)
		answer=answer+letter
		j=j+1
	print(answer)
	if answer.lower()==column[randcolumn[0]]:
		subprocess.call(["espeak", "Good"])
	
	else:
		subprocess.call(["espeak","-s","100", "No you spelt wrong the answer will be "])
		for i in range(0,len(column[randcolumn[0]])): 
			print(column[randcolumn[0]][i], end='')
			subprocess.call(["espeak","-s","150", column[randcolumn[0]][i]])
		print("\n")
	os.system("truncate -s 0 decode.txt")
	u=input("Do you want to continue?")
	type(u)
	if u=="No":
		break
