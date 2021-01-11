#!/usr/bin/python3
#coding:utf-8
# Ce qui peuvent arranger le code avec de l'objet !! sa serai plus perfecto
import regles as rule
from tkinter import *
import random 
import time
# Action a declencher!!!
numb = range(1, 500)
aleatoire = random.choice(numb)
def game():
	global aleatoire
	gaming = True
	entry1.delete(0, END)
	number = entry2.get()
	number = int(number)
	if number == aleatoire:
		entry1.delete(0, END)
		time.sleep(2)
		entry1.insert(0, "Ta gagner !!")
		gaming= False
	elif number > aleatoire:
		entry1.delete(0, END)
		time.sleep(2)
		entry1.insert(0, "MOINS QUE SA !!!")
	elif number < aleatoire:
		entry1.delete(0, END)	
		time.sleep(2)
		entry1.insert(0, "PLUS QUE SA!!!!!!")
		



root = Tk()
rules = rule.Gui()

root.title("Jeu du : Plus ou moins")	
root.geometry("400x200")
root.config(background="#01070E")
root.maxsize(400, 200)
root.minsize(400, 200)	
frame1 = Frame(root , bg="#01070E",border=1 , relief=SUNKEN)
frame1.place(x=50, y=100)


# Creation des widgets!!
button1 = Button(root, text="Submit", font=60,command=game)
button1.place(x=300 , y=150)
entry2 = Entry(frame1, font=20)
entry1 = Entry(root, font=50)
entry1.place(x=150, y=25)
label1 = Label(frame1, text="""Entrez Votre proposition:(1 /a/500)""", bg="#01070E",fg='white')	
label1.pack()
entry2.pack(pady=10)
rules.gui.mainloop()
root.mainloop()

