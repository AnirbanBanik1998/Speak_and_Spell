import xlrd
import random
import subprocess
file_loc="./Words.xlsx"
workbook=xlrd.open_workbook(file_loc)
sheet=workbook.sheet_by_index(0)
print("Press CTRL+Z to quit")
while 1:
	my_randoms = random.sample(range(1, sheet.nrows), 1)
	rand=sheet.cell_value(my_randoms[0], 0)
	answer=input(subprocess.call(["espeak","-s","100"," Spell "+rand]))
	type(answer)
	if answer==rand:
		subprocess.call(["espeak", "Good"])
	
	else:
		subprocess.call(["espeak","-s","100", "No you spelt wrong the answer will be "])
		for i in range(0,len(rand)): 
			subprocess.call(["espeak","-s","150", rand[i]])
			

