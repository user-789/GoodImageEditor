import sys
import re

def getstr(line, cursor = -1):
	str_ = ""
	for i, (r, g, b) in enumerate(line):
		char = "[]" if i == cursor else "  "
		xcolor = 255 if r+g+b <= 384 else 0
		str_ += f"\033[48;2;{r};{g};{b}m\033[38;2;{xcolor};{xcolor};{xcolor}m\033[1m{char}\033[m"
	return str_

def printimg(image):
	for i, line in enumerate(image):
		if cursor[0] == i:
			print(getstr(line, cursor[1]))
		else:
			print(getstr(line))

filename = None
if len(sys.argv) == 2:
	with open(sys.argv[1], "r") as file:
		filename = sys.argv[1]
		image = file.read()
		image = re.sub(re.compile("#.*$", flags=re.MULTILINE), "\n", image)
		image = image.replace("\n", " ")
		if image[:3] != "P3 ":
			raise Exception("Wrong file format")
		image = [int(s) for i, s in enumerate(image.split(" ")) if i != 0 and s != "" and s[0] != "#"]
		width = image[0]
		height = image[1]
		del image[0:3]
		image = [[image[3*width*i+3*j:3*width*i+3*j+3] for j in range(width)] for i in range(height)]
		file.close()
elif len(sys.argv) == 3:
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	image = [[[255, 255, 255] for j in range(width)] for i in range(height)]

cursor = [0, 0]
h4ck3rMode = False

while True:
	printimg(image)
	inp = input().lower().split(" ")
	if len(inp) == 0:
		continue
	elif len(inp) == 1:
		if inp[0] == "save":
			if filename is None:
				print("I don't know where to save. Please use \"save filename.ppm\"")
			else:
				with open(filename, "w") as savefile:
					savefile.write("P3\n" + str(width) + " " + str(height) + "\n255\n" + "\n".join(" ".join(str(i) for i in pixel) for line in image for pixel in line)+"\n")
					print(f"Saved to {filename}")
					savefile.close()
			continue
		elif inp[0] == "quit":
			print("Are you sure?")
			if input().lower() == "yes":
				exit()
		elif h4ck3rMode:
			if inp[0] == "red++":
				image[cursor[0]][cursor[1]][0] = min(255, image[cursor[0]][cursor[1]][0]+1)
			elif inp[0] == "red--":
				image[cursor[0]][cursor[1]][0] = max(0, image[cursor[0]][cursor[1]][0]-1)
			elif inp[0] == "green++":
				image[cursor[0]][cursor[1]][1] = min(255, image[cursor[0]][cursor[1]][1]+1)
			elif inp[0] == "green--":
				image[cursor[0]][cursor[1]][1] = max(0, image[cursor[0]][cursor[1]][1]-1)
			elif inp[0] == "blue++":
				image[cursor[0]][cursor[1]][2] = min(255, image[cursor[0]][cursor[1]][2]+1)
			elif inp[0] == "blue--":
				image[cursor[0]][cursor[1]][2] = max(0, image[cursor[0]][cursor[1]][2]-1)
	else:
		if inp[0] == "paint" and not h4ck3rMode:
			color = int(inp[1], base=16)
			image[cursor[0]][cursor[1]][0] = color // 256**2
			image[cursor[0]][cursor[1]][1] = color // 256 % 256
			image[cursor[0]][cursor[1]][2] = color % 256
		elif inp[0] == "move":
			if inp[1] == "down" and cursor[0] != height-1:
				cursor[0] += 1
			elif inp[1] == "up" and cursor[0] != 0:
				cursor[0] -= 1
			elif inp[1] == "right" and cursor[1] != width-1:
				cursor[1] += 1
			elif inp[1] == "left" and cursor[1] != 0:
				cursor[1] -= 1
		elif inp[0] == "toggle" and inp[1] == "h4ck3rmode":
			if h4ck3rMode:
				h4ck3rMode = not h4ck3rMode
			else:
				print("ARE YOU SURE YOU CAN HANDLE SUCH EFFICIENCY??")
				if (input().lower() == "yes"):
					h4ck3rMode = not h4ck3rMode
			continue
		elif inp[0] == "save":
			with open(inp[1], "w") as savefile:
				savefile.write("P3\n" + str(width) + " " + str(height) + "\n255\n" + "\n".join(" ".join(str(i) for i in pixel) for line in image for pixel in line)+"\n")
				print(f"Saved to {inp[1]}")
				savefile.close()
		