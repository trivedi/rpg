from time import *
from sys import *
from os import *
from blessings import Terminal

t = Terminal()
user = (str(getlogin())).title()


def prompt():
	x = raw_input(t.yellow("> "))
	return x


def story():
	s = ["Lorem ipsum dolor sit amet, consectetur adipiscing som random thig", "there was a hevufd floq fdthe rejkfdkjhtrkhekjerkjreer", 
		"fere if there wa no other kind of thing in the ends howvee there is none in the ened there fore tolla", "rtrhwewhn there is none the dragon was awesome with mighy like no other",
		"even though all attempts to dissuade were colossal mistakes in his life there want nafd.", "hoever is thiere any but so close thosdsdhtnerehnn trht dhtrotrtr skhkh erhe khkhkhtr.", 
		"thus, all of fate and the people lie in your hands. what shall you do hero..."]
	clear()
	print "The story so far..."
	print ""
	for lines in s:
		sleep(1)
		print lines
		sleep(.3)
	sleep(1)
	if name == "posix":
		print "It is up to you, %s, to save the world!" % user
	else:
		print "It is up to you to save the world!"
	sleep(1.5)
	print ""
	print "Press {t.magenta}m{t.normal} to go back to the main menu".format(t=t)
	while True:
		if prompt() == "m":
			restart()





def clear():
	system("clear")


def quit():
	print ""
	print "Until next time..."
	sleep(2)
	clear()
	system("exit")

		

def restart():
	system("python main.py")

def wait():
	raw_input()


def about():
	while True:
		clear()
		print "Author: Nishad Trivedi"
		print "Build: 1"
		print "Press 'm' to go back to the main menu"
		print ""
		wait()
		break
   
