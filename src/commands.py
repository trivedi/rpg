from util import *
from router import *
from blessings import Terminal

t = Terminal()

def fly():
	clear()
	""" if character has demon wings:
			fly
		else:
			print "You have no wings" """
	print "You have no wings"
	sleep(2)

def pray():
	while True:
		clear()
		gods = ["Lord of Justice", "Lord of Death"]
		print "Who do you pray to?"
		print ""
		for g in gods:
			print t.magenta(g)
		print ""
		c = prompt()
		while True:
			if c in ("1", "Lord of Justice"):
				print "You kneel down to pray"
				sleep(1.8)
				print ""
				print t.bold("Awaka reh kils htreo. Hetr slok sown patudef. Lorsn epes tea jontasa ok te.")
				sleep(2)
				print ""
				print "She has answered your prayers. You have been given {t.red}the Horn of Justice{t.normal}!".format(t=t)
				wait()
				break
			elif c in ("2", "Lord of Death"):
				print "You kneel down to pray"
				sleep(1.8)
				print ""
				print t.bold("Awaka reh kils htreo. Hetr slok sown patudef. Lorsn epes tea jontasa ok te.")
				sleep(2)
				print ""
				print "He is pleased with your devotion. You have been given {t.red}Demon Wings{t.normal}!".format(t=t)
				wait()
				break
		break

def transform():
	animals = ["Wolf", "Dragon", "Tiger", "Fox"]
	while True:
		clear()
		print "What would you like to transform in to?"
		print ""
		for a in animals:
			print t.magenta(a)
		print ""
		cmd = prompt()
		if cmd == "Wolf":
			print "You have transformed in to a wolf!"
			wait()
			break
		elif cmd == "Dragon":
			print "You are not a dragonborne...are you?"
			wait()
			transform()
		elif cmd == "Tiger":
			print "Your stripes strike fear"
			wait()
			break
		elif cmd == "Fox":
			print "Sly and cunning you are!"
			wait()
			break
		else:
			break
		break




