import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import os.path
from os import path



def generator(number,max_num):

	num = np.random.randint(low=1,high=max_num+1)
	generated = np.array([num])

	while len(generated) < number:
		num = np.random.randint(low=1,high=max_num+1)
		if np.any(generated == num) == False:
			generated = np.append(generated, num)

	return generated

def card_maker(numbers,name):
	plt.xlim(0,5)
	plt.ylim(0,3)
	plt.axhline(1)
	plt.axhline(2)
	plt.axvline(1)
	plt.axvline(2)
	plt.axvline(3)
	plt.axvline(4)

	count = 0
	row = 0
	while row < 3:
		column = 0
		while column < 5:
			#if (row == 2 and column == 2) == False:
			plt.text(0.3+column,0.3+row,str(numbers[int(count)]))
			count = count + 1
			column = column + 1
		row = row + 1
	plt.axis('off')
	plt.title("BINGO: "+name)
	plt.savefig("cards/"+name+"_bingocard.png",dpi=200)
	#plt.show()
	plt.close()


with open('names.txt', 'r') as f:
    names = f.read().splitlines()

font = {'weight' : 'bold',
        'size'   : 22}

matplotlib.rc('font', **font)

for name in names:
	if path.exists("cards/bingocard_"+name+".png") == False:
		print("Generating: "+name)
		card_maker(generator(15,90),name)
	else:
		print("Skipping: "+name)

