import random
import subprocess
import time
import os
f= open("../Wordlist.csv",'r')
rows=f.read().split("\n")
while 1:
	k=0
	print("Enter one letter in a single try:")
	string=""
	str1=""
	my_randoms=random.sample(range(0, len(rows)), 1)
	column=rows[my_randoms[0]].split(",")
	randcolumn = random.sample(range(0, (len(column) - 1)), 1)
	column[randcolumn[0]]=column[randcolumn[0]].strip()
	for i in range(0, len(column[randcolumn[0]])):
		string=string+"-"
	for i in range(0,len(string)):
		str1=str1+string[i]+" "
	print (str1)
		
	str1=""
	def check(str1,l):
		print(" Input is "+l)
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
	os.system("truncate -s 0 decode.txt")
	u=input("Do you want to continue?")
	type(u)
				
	if u=="No":
		break
