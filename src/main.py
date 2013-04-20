from map import *
from commands import *
from util import *
from os import *
from start import *
from blessings import Terminal


# Main Menu
user = (str(getlogin())).title()
t = Terminal()


def menu():
	while True:
		clear()
		print ""
		print t.red("    ___    ____ _    _________   __________  ______  ______   ____  __  ___________________")
		print t.red("   /   |  / __ \ |  / / ____/ | / /_  __/ / / / __ \/ ____/  / __ \/ / / / ____/ ___/_  __/")
		print t.red("  / /| | / / / / | / / __/ /  |/ / / / / / / / /_/ / __/    / / / / / / / __/  \__ \ / /   ")
		print t.red(" / ___ |/ /_/ /| |/ / /___/ /|  / / / / /_/ / _, _/ /___   / /_/ / /_/ / /___ ___/ // /  ")
		print t.red("/_/  |_/_____/ |___/_____/_/ |_/ /_/  \____/_/ |_/_____/   \___\_\____/_____//____//_/")
		print ""
		print t.magenta("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
		print ""
		if name == "posix":
			print "Welcome, %s!" % user
		else:
			print "Welcome!"
		print "Please select an option"
		print ""
		print "Play  -- your adventure awaits"
		print "Story -- read what the adventure is all about"
		print "Exit  -- quit the current session"
		print "About"
		print "Restart"
		print ""
		while True:
			command = prompt()
			if command in ("s", "story", "Story"):
				story()
			elif command in ("p", "play", "Play"):
				start()
			elif command in ("q", "quit", "exit"):
				break
			elif command in ("r", "restart", "Restart"):
				restart()
			elif command in ("a", "about", "About"):
				about()	
			else:
				clear()
				menu()
		break



# - - - - - - -

menu()