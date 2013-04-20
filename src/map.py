from commands import *
from util import *
from blessings import Terminal

t = Terminal()

def village():
	while True:
		clear()
		print "You are in the {t.red}Village{t.normal}".format(t=t)
		command = prompt()
		if command == "help":
			help()
		elif command == "travel":
			map()
		elif command == "fly":
			fly()
			village()
		elif command == "transform":
			transform()
		elif command in ("quit", "exit"):
			break
		elif command == "restart":
			restart()
		elif command == "map":
			map()
		elif command == "temple":
			temple()
		else:
			help()
			village()

def mountains():
	while True:
		clear()
		print "You are in the {t.red}Shivering Mountains{t.normal}".format(t=t)
		command = prompt()
		if command == "help":
			help()
		elif command == "travel":
			map()
		elif command == "fly":
			fly()
			mountains
		elif command == "transform":
			transform()
		elif command in ("quit", "exit"):
			break
		elif command == "restart":
			restart()
		elif command == "map":
			map()
		else:
			help()
			mountains()


def desert():
	while True:
		clear()
		print "You are in the {t.red}Mirage Desert{t.normal}".format(t=t)
		command = prompt()
		if command == "help":
			help()
		elif command == "travel":
			map()
		elif command == "fly":
			fly()
			desert()
		elif command == "transform":
			transform()
		elif command in ("quit", "exit"):
			break
		elif command == "restart":
			restart()
		elif command == "map":
			map()
		else:
			help()
			desert()


# Sublocations
# ------------


def temple():
	clear()
	print "You are at the {t.red}Temple{t.normal}".format(t=t)
	c = prompt()
	if c == "pray":
		pray()


def help():
	while True:
		print ""
		print "You can: "
		print ""
		h = ["travel", "fly", "transform", "exit/quit", "restart"]
		for c in h:
			print t.magenta(c)
		print ""
		command = prompt()
		if command == "travel":
			map()
			break
		elif command == "fly":
			fly()
			break
		elif command == "transform":
			transform()
			break
		elif command in ("exit", "quit"):
			quit()
		elif command == "restart":
			restart()
		else: help()
		raw_input("What would you like to do? ")
		break




def map():
	while True:
		clear()
		print ""
		print "                             / \\"
		print "                              | "
		print ""
		print "                              N "
		print ""
		print "                           Desert  "
		print ""
		print ""
		print ""
		print "/							    \\"
		print "  -- W   Village                            Mountains   E --"
		print "\\						            /"
		print ""
		print ""
		print ""
		print ""
		print "			   Dungeon  "
		print ""
		print "                              S "
		print ""
		print "                              | "
		print "			     \\ /"
		print ""
		print "Where would you like to go?"
		print "N / W / S / E"
		command = prompt()
		if command == "N":
			desert()
			break
		if command == "E":
			village()
			break
		if command == "S":
			dungeon()
			break
		if command == "E":
			mountains()
			break
		break



