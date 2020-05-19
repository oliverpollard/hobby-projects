import numpy as np

def generate_number(drawn, max_num):
	num = np.random.randint(low=1,high=max_num+1)
	while np.any(drawn == num) == True:
		num = np.random.randint(low=1,high=max_num+1)

	drawn = np.append(drawn,num)
	return num, drawn


def write_html(num,drawn):
	f = open("bingo.html", "w")
	f.write('<!DOCTYPE html>\n')
	f.write('<html>\n')
	f.write('<head>\n')
	f.write('<link rel="stylesheet" href="bingo.css">\n')
	f.write('</head>\n')
	f.write('<body>\n')
	f.write('<div class="titlecontainer"><h1 class="title">BINGO!</h1></div>\n')
	f.write('<div class="container"><h1 class="rainbow rainbow_text_animated">'+str(num)+'</h1></div>\n')
	f.write('<div class="drawncontainer"><h4 class="drawn">'+str(drawn[1:])[1:-1]+'</h4></div>\n')
	f.write('</body>\n')
	f.write('</html>\n')
	f.close()

max_num = 90
drawn = np.array([0])



with open('callouts.txt', 'r') as f:
    callouts = f.read().splitlines()

while len(drawn) <= max_num:
	x = input('Press enter to generate bingo number (or q to quit)...\n')
	if x == 'q':
		print("Finished!")
		print("Drawn numbers:", drawn)
		break
	num, drawn = generate_number(drawn, max_num)
	write_html(num,drawn)
	print(str(num)+"!\n")
	print(callouts[int(num-1)])

if len(drawn) == max_num+1:
	print("All numbers drawn!")
	print(np.sort(drawn))

