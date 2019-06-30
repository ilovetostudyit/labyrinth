import random
import numpy as np
import cv2 as cv
import time
import matplotlib.pyplot as plt
death_flag = 0

def health_check(img_2, health, x, y, text1, text2, text3):
	global death_flag

	if 1 in health:
		for each in health:
			if each == 1:
				heart = cv.imread("heart.png")
				img_2[y:y+50, x:x+50] = heart
				x = x+55
	else:
		img_2 = thedeath
		death_flag = 1
		text1 = "so, you are dead now"
		text2 = "u should learn"
		text3 = "programming better"
		cv.rectangle(img_2, (0,0), (400, 130), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (0,0), (400, 130), (255,255,255), 3)
		cv.putText(img_2,text1,(5,20), font, 0.8,(255,255,255),1,cv.LINE_AA)
		cv.putText(img_2,text2,(5,40), font, 0.8,(255,255,255),1,cv.LINE_AA)
		cv.putText(img_2,text3,(5,60), font, 0.8,(255,255,255),1,cv.LINE_AA)
		cv.imshow("DUNGEON", img_2)
	return(img_2)

   
def button_press_elf(i):
	global health
	if i:
		health.append(1)
	else:
		if 1 in health:
			health.remove(1)

def click_and_crop(event, x, y, flags, param):
	global refPt
	if (event == cv.EVENT_LBUTTONDOWN):
		refPt = [(x, y)]
  
def roll_this_question(text, x):
	if x == -1:
		x = random.randint(0, 10)
	if x == 0:
		text = "Is Python case sensitive when dealing with identifiers?"
	elif x == 1:
		text = "Is Python an interpreted language?"
	elif x == 2:
		text = "Can you convert a string to a number in Python?"
	elif x == 3:
		text = "Can you share global variables across the modules?"
	elif x == 4:
		text = "Can you use Python for web development?"
	elif x == 5:
		text = "Are there any predefined functions available in Python?"
	elif x == 6:
		text = "Can we use Python as a scripting language?"
	elif x == 7:
		text = "Can you compare Java and Python?"
	elif x == 8:
		text = "Is Python easy to learn and easy to write? "
	elif x == 9:
		text = "Do you know any programming languages which are influenced by Python?"
	elif x == 10:
		text = "Can u list some games which were developed using Python?"
	return(text, x)

def python_quiz(img2):
	img2 = cv.imread("elf.jpg")
	cv.imshow('DUNGEON', img_2)
	return(img2)
	
def basic_grid(img1, abyss, x_t, y_t):
	x_l = 1
	y_l = 1
	if abyss[x_t][y_t] != 4:
		abyss[x_t][y_t] = 1
	for x_d in abyss:
		for y_d in x_d:
			if y_d == 1:
				cv.rectangle(img_1,((y_l - 1) * 50, (x_l - 1) * 50),(y_l * 50, x_l * 50),(0,255,0), cv.FILLED)
			elif y_d == 2:
				cv.rectangle(img_1,((y_l - 1) * 50, (x_l - 1) * 50),(y_l * 50, x_l * 50),(255,255,0), cv.FILLED)
			elif y_d == 3:
				cv.rectangle(img_1,((y_l - 1) * 50, (x_l - 1) * 50),(y_l * 50, x_l * 50),(0,130,0), cv.FILLED)
			elif y_d == 4:
				cv.rectangle(img_1,((y_l - 1) * 50, (x_l - 1) * 50),(y_l * 50, x_l * 50),(0,60,0), cv.FILLED)
			cv.rectangle(img_1,((y_l - 1) * 50, (x_l - 1) * 50),(y_l * 50, x_l * 50),(0,0,0), 3)
			y_l = y_l + 1
		y_l = 1
		x_l = x_l + 1
	return(img1)

x = random.randint(2, 10)
y = random.randint(2, 10)
abyss = np.array(range(x*y))
abyss.shape = (x,y)
for each in abyss:
	ind = np.arange(len(each))
	np.put(each, ind, 0)
x1 = 0
y1 = 0
x_t = x1
y_t = y1
while (x1 == 0 and y1 == 0):
	x1 = random.randint(0, (x - 1))
	y1 = random.randint(0, (y - 1))
x_elf = 0
y_elf = 0
while ((x_elf == 0 and y_elf == 0) or (x_elf == x1 and y_elf == y1)):
	x_elf = random.randint(0, (x - 1))
	y_elf = random.randint(0, (y - 1))
x_chest = 0
y_chest = 0
while ((x_chest == 0 and y_chest == 0) or (x_chest == x1 and y_chest == y1) or (x_chest == x_elf and y_chest == y_elf)):
	x_chest = random.randint(0, (x - 1))
	y_chest = random.randint(0, (y - 1))
x_fairy = 0
y_fairy = 0
while ((x_fairy == 0 and y_fairy == 0) or (x_fairy == x1 and y_fairy == y1) or (x_fairy == x_elf and y_fairy == y_elf) or (x_fairy == x_chest and y_fairy == y_chest)):
	x_fairy = random.randint(0, (x - 1))
	y_fairy = random.randint(0, (y - 1)) 
img_1 = np.zeros([50*x,50*y,3],dtype=np.uint8)
img_1.fill(255)
img_n = img_1
cv.imshow('MAP', img_1)
img_2 = np.zeros([600,400,3],dtype=np.uint8)
img_2.fill(0)
thewall = cv.imread("end.jpg")
theexit = cv.imread("exit.jpg")
theroot = cv.imread("root.jpg")
thedeath = cv.imread("death.png")
thechest = cv.imread("chest.jpg")
thefairy = cv.imread("fairy.png")
cv.imshow("DUNGEON", img_2)
font = cv.FONT_HERSHEY_SIMPLEX
text1 = "Dark old dungeon greets you"
text2 = "with unpleasant smile"
text3 = "of cold rocks"
health = [1,1,1]
text4 = ("health: ")

cv.putText(img_2,text1,(5,20), font, 0.8,(255,255,255),1,cv.LINE_AA)
cv.putText(img_2,text2,(5,40), font, 0.8,(255,255,255),1,cv.LINE_AA)
cv.putText(img_2,text3,(5,60), font, 0.8,(255,255,255),1,cv.LINE_AA)
cv.putText(img_2,text4,(5,80), font, 0.5,(255,255,255),1,cv.LINE_AA)
cv.setMouseCallback("DUNGEON", click_and_crop)
fexit = 0
number = -1
number2 = -1
number3 = -1
while True:
	img_1 = basic_grid(img_1, abyss, x_t, y_t)
	cv.rectangle(img_2, (0,0), (400, 130), (0,0,0), cv.FILLED)
	cv.rectangle(img_2, (0,0), (400, 130), (255,255,255), 3)
	cv.putText(img_2,text1,(5,20), font, 0.6,(255,255,255),1,cv.LINE_AA)
	cv.putText(img_2,text2,(5,40), font, 0.6,(255,255,255),1,cv.LINE_AA)
	cv.putText(img_2,text3,(5,60), font, 0.4,(255,255,255),1,cv.LINE_AA)
	cv.putText(img_2,text4,(5,85), font, 0.6,(255,255,255),1,cv.LINE_AA)
	img_2 = health_check(img_2, health, 60, 70, text1, text2, text3)
	cv.imshow('MAP', img_1)
	cv.imshow('DUNGEON', img_2)
	if (cv.waitKey(30) == ord('a') and death_flag == 0):
		if (y_t - 1 >= 0):
			abyss[x_t][y_t] = 3
			y_t = y_t - 1
			img_2 = theroot
			text1 = "where will you go?"
			text2 = "and when"
			text3 = "will you stop"
		else:
			img_2 = thewall
			text1 = "The wall."
			text2 = "You should search"     
			text3 = "another way"
	if cv.waitKey(30) == ord('d'):
		if (y_t + 1 < y):
			abyss[x_t][y_t] = 3
			y_t = y_t + 1
			img_2 = theroot
			text1 = "where will you go?"
			text2 = "and when"
			text3 = "will you stop"
		else:
			img_2 = thewall
			text1 = "The wall."
			text2 = "You should search"     
			text3 = "another way"
	if (cv.waitKey(30) == ord('w') and death_flag == 0):
		if (x_t - 1 >= 0):
			abyss[x_t][y_t] = 3
			x_t = x_t - 1
			img_2 = theroot
			text1 = "where will you go?"
			text2 = "and when"
			text3 = "will you stop"
		else:
			img_2 = thewall
			text1 = "The wall."
			text2 = "You should search"     
			text3 = "another way"
	if cv.waitKey(30) == ord('s'):
		if (x_t + 1 < x):
			abyss[x_t][y_t] = 3
			x_t = x_t + 1
			img_2 = theroot
			text1 = "where will you go?"
			text2 = "and when"
			text3 = "will you stop"
		else:
			img_2 = thewall
			text1 = "The wall."
			text2 = "You should search"     
			text3 = "another way"
	if (x_t == x1 and y_t == y1 and death_flag == 0):
		fexit = 1
		img_2 = theexit
		text1 = "The exit."
		text2 = "This is the way out"     
		text3 = "of this dead cave"
	if (x_t == x_elf and y_t == y_elf and death_flag == 0):
		img_2 = python_quiz(img_2)        
		text1 = "from the mist the blind lady"
		text2 = "appears and asks you a question:"
		text3, number = roll_this_question(text3, number)
		yes_zone = cv.rectangle(img_2, (50,500), (150, 550), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (50,500), (150, 550), (255,255,255), 3)
		cv.putText(img_2,"YES",(75,530), font, 0.8,(255,255,255),1,cv.LINE_AA)
		no_zone = cv.rectangle(img_2, (250,500), (350, 550), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (250,500), (350, 550), (255,255,255), 3)
		cv.putText(img_2,"NO",(275,530), font, 0.8,(255,255,255),1,cv.LINE_AA)
		if ((50 <= refPt[0][0] <= 150) and (500 <= refPt[0][1] <= 550)):
			button_press_elf(1)
			abyss[x_elf][y_elf] = 1
			x_elf = -1
			y_elf = -1
		if ((250 <= refPt[0][0] <= 350) and (500 <= refPt[0][1] <= 550)):
			button_press_elf(0)
			abyss[x_elf][y_elf] = 1
			x_elf = -1
			y_elf = -1
		refPt = [(0, 0)]
	if (x_t == x_chest and y_t == y_chest and death_flag == 0):
		img_2 = thechest       
		text1 = "Oh! Lucky! The treasure ahead"
		text2 = "to open the chest, answer:"
		text3, number2 = roll_this_question(text3, number2)
		yes_zone = cv.rectangle(img_2, (50,500), (150, 550), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (50,500), (150, 550), (255,255,255), 3)
		cv.putText(img_2,"YES",(75,530), font, 0.8,(255,255,255),1,cv.LINE_AA)
		no_zone = cv.rectangle(img_2, (250,500), (350, 550), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (250,500), (350, 550), (255,255,255), 3)
		cv.putText(img_2,"NO",(275,530), font, 0.8,(255,255,255),1,cv.LINE_AA)
		if ((50 <= refPt[0][0] <= 150) and (500 <= refPt[0][1] <= 550)):
			button_press_elf(1)
			abyss[x_chest][y_chest] = 1
			x_chest = -1
			y_chest = -1
		if ((250 <= refPt[0][0] <= 350) and (500 <= refPt[0][1] <= 550)):
			button_press_elf(0)
			abyss[x_chest][y_chest] = 1
			x_chest = -1
			y_chest = -1
		refPt = [(0, 0)]
	if (x_t == x_fairy and y_t == y_fairy and death_flag == 0):
		img_2 = thefairy       
		text1 = "The fairy awaited for you, mortal"
		text2 = "get the gift from her:"
		text3, number3 = roll_this_question(text3, number3)
		yes_zone = cv.rectangle(img_2, (50,500), (150, 550), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (50,500), (150, 550), (255,255,255), 3)
		cv.putText(img_2,"YES",(75,530), font, 0.8,(255,255,255),1,cv.LINE_AA)
		no_zone = cv.rectangle(img_2, (250,500), (350, 550), (0,0,0), cv.FILLED)
		cv.rectangle(img_2, (250,500), (350, 550), (255,255,255), 3)
		cv.putText(img_2,"NO",(275,530), font, 0.8,(255,255,255),1,cv.LINE_AA)
		if ((50 <= refPt[0][0] <= 150) and (500 <= refPt[0][1] <= 550)):
			button_press_elf(1)
			abyss[x_chest][y_chest] = 1
			x_fairy = -1
			y_fairy = -1
		if ((250 <= refPt[0][0] <= 350) and (500 <= refPt[0][1] <= 550)):
			button_press_elf(0)
			abyss[x_fairy][y_fairy] = 1
			x_fairy = -1
			y_fairy = -1
		refPt = [(0, 0)]
	if fexit:
		abyss[x1][y1] = 4
	img_1 = basic_grid(img_1, abyss, x_t, y_t)  
	cv.imshow('MAP', img_1)
	cv.imshow('DUNGEON', img_2)
cv.waitKey(0)
cv.destroyAllWindows()
