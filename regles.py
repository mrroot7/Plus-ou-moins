#!/usr/bin/python3
from tkinter import *
class Gui():
	def __init__(self):
		self.gui= Tk()
		self.gui.title("Regles-A-Suivre du Jeu Plus ou moins")
		self.gui.geometry("400x200")
		self.gui.config(background="#01070E")
		self.create_labels()
	def	create_labels(self):
		label1 = Label(self.gui, text=""" Merci de jouer a Plus ou moins!!
Les regles sont simple vous devez juste devinez un nombre!!
Bien sur Generer par L'IA Bonne Chances!!!!! """,font=("Arial", 10),bg="#01070E", fg="grey")
		label1.pack()
		label2 = Label(self.gui, text="MADE BY MR.ROOT", font=("Arial", 20),bg="#01070E", fg="grey")
		label2.place(x=70, y=150)



