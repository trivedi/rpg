from map import *
from util import *
from time import sleep
import fish
from blessings import Terminal


t = Terminal()

def start():
	clear()
	print t.yellow("Starting game")
	print ""
	print "Type {t.magenta}help{t.normal} for a list of commands".format(t=t)
	print ""
	bird()
	"""for i in range(0,18):
		sleep(.1)
		print t.on_yellow(" "),
		stdout.flush()"""
	print ""
	print ""
	clear()
	village()


def bird():
	bird = fish.Bird()
	i = 24
	while i > 0:
		sleep(.3)
		bird.animate()
		i = i - 1
