import drawHangman
import time
from time import sleep
import random


#These are the key words:
keys = ["nepal" , "about", "education", "handsome", "country"]
heart = 5
trys = ""
cans = []
wans = ""
number = "1234567890-=+/.,"
score = 0



question = random.choice(keys)
q_len = len(question)

arr = []
arr.append('-'*len(question))
print("\n")
print(arr)

print("Our question have {} words".format(q_len))
#print("_ "*q_len)
#Display the question:
for i in arr:
	for h in i:
		cans.append(h)
print(question)
print("Our Word:" ,' '.join(arr))

while True:
	if len(trys) == len(question):
		print("You won! Word: {} Your score: {}".format(question, score))
		print("Please press 'Enter' to quit..")
		break
	if heart == 0:
		print("\n You loose...")
		sleep(0.9)
		print("Your Score is {}".format(score))
		sleep(0.9)
		print("The word you could not answer is: {}".format(question))
		sleep(0.9)
		print("please press 'Enter' to quit..")
		break
	

	x = input("\n Please enter a letter: ")
	if 1 <len(x):
		print("\n You can enter only 1 letter")
		continue
	if x in number:
		print("\n Its not even a letter")
		continue
	if x in trys:
		print("\n You used this letter")
		continue
	if x in question:
		index = question.index(x)
		for i,char in enumerate(question):
			cans[index] = x
						



#print(question)
