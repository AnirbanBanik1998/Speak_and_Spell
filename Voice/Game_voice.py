import random
import subprocess
import os
import time
with open("Sample_words.txt",'r') as f:
	rows=f.read().split("\n")
	while 1:
		p=input("Enter Name of Game to play or Quit to quit: ")
		type(p)
		if p=="Hangman":
		
			while 1:
				k=0
				print("Enter one letter in a single try:")
				string=""
				str1=""
				my_randoms=random.sample(range(0, len(rows)), 1)
				column=rows[my_randoms[0]].split(",")
				randcolumn=random.sample(range(0, len(column)), 1)
				column[randcolumn[0]]=column[randcolumn[0]].strip()
				for i in range(0, len(column[randcolumn[0]])):
					string=string+"-"
				for i in range(0,len(string)):
					str1=str1+string[i]+" "
				print (str1)
		
				str1=""
				def check(str1,l):
					for j in range(0, len(string)):
						if l==column[randcolumn[0]][j] and string[j]=="-":
							str1=str1+l
						else:
							str1=str1+string[j]
					return str1
				while k<10:
					time.sleep(3)
					k=k+1
					str1=""
					letter=""
					print("Enter letter: ")
					#os.system("cd ~/speech_recognition2.7; pocketsphinx_continuous -inmic yes -lm 9731.lm -dict 9731.dic > decode.txt")
					with open('decode.txt','r') as r:
						
						arr=r.read().split("\n")
						n=len(arr)-1
						while arr[n]=="" and n>0:
							n=n-1
						letter=arr[n]
					print(letter)
					lt=letter
					try:
						string=str(check(str1,lt))
						print(string)
					except:
						print("Not Possible")
			
					str1=""
					for j in range(0, len(string)):
						str1=str1+string[j]+" "
					print(str1)
					if string==column[randcolumn[0]]:
						subprocess.call(["espeak","You win"])
						break
					elif k==10:
						subprocess.call(["espeak","You lose"])
						print(" Answer is: "+column[randcolumn[0]])
					f=open("decode.txt", "r+")
					f.truncate()
					f.close()
				u=input("Do you want to continue?")
				type(u)
				
				if u=="No":
					break
		elif p=="Speak":
			while 1:
				k=0
				print("Spell It!")
				string=""
				str1=""
				my_randoms=random.sample(range(0, len(rows)), 1)
				column=rows[my_randoms[0]].split(",")
				randcolumn=random.sample(range(0, len(column)), 1)
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
		elif p=="Quit":
			print("Goodbye")
			break
