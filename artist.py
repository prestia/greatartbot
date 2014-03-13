import time
import autopy
from subprocess import Popen
from os import system, getcwd
from random import randrange
from rsync import *

def main():
	path = getcwd()
	artistapp = path + "/artist_mac"

	# Change this to reflect how many pictures you want made in one execution of artist.py
	this_many_pictures = 1

	# Launch ARTIST as a non-blocking subprocess
	Popen(artistapp)
	
	# Wait
	time.sleep(1)
	
	# Enter sketch mode
	autopy.key.tap('s')

	# MAKE ART
	imgnum = 0

	# Remove the yellow square/"cursor"
	time.sleep(1)
	autopy.key.tap('x')

	while imgnum < this_many_pictures:
		
		# START ALGORITHM #
		# Note: The production version of @greatartbot has evolved a lot since this code was released. The real fun of this bot is messing with this section of code until your bot is producing art that you like. Play! Have fun!

		# Select the set of keys to be used
		usearray = randrange(5)
		# Randomizes the key array so that some of the "stronger" keys (i.e. Up, Down, 'r', 't', and 'y') aren't always used.sometimes the Up and Down keys are unavailable, as they tend to make a lot of work look very similar
		if usearray == 0:
			# If you would like to use this code and always use the full set of keys, just use this array.
			keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','0','1','2','3','4','5','6','7','8','9','-','+',autopy.key.K_F1,autopy.key.K_F2,autopy.key.K_F3,autopy.key.K_F4,autopy.key.K_F5,autopy.key.K_F6,autopy.key.K_F7,autopy.key.K_F8,autopy.key.K_F9,autopy.key.K_F10,autopy.key.K_F11,autopy.key.K_F12,autopy.key.K_LEFT,autopy.key.K_RIGHT,autopy.key.K_DOWN,autopy.key.K_UP]
		elif usearray == 1 or usearray == 2:
			keys = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','y','z','0','1','2','3','4','5','6','7','8','9','-','+',autopy.key.K_F1,autopy.key.K_F2,autopy.key.K_F3,autopy.key.K_F4,autopy.key.K_F5,autopy.key.K_F6,autopy.key.K_F7,autopy.key.K_F8,autopy.key.K_F9,autopy.key.K_F10,autopy.key.K_F11,autopy.key.K_F12,autopy.key.K_LEFT,autopy.key.K_RIGHT]
		elif usearray == 3 or usearray == 4:
			keys = ['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','s','u','v','w','z','0','1','2','3','4','5','6','7','8','9','-','+',autopy.key.K_F1,autopy.key.K_F2,autopy.key.K_F3,autopy.key.K_F4,autopy.key.K_F5,autopy.key.K_F6,autopy.key.K_F7,autopy.key.K_F8,autopy.key.K_F9,autopy.key.K_F10,autopy.key.K_F11,autopy.key.K_F12,autopy.key.K_LEFT,autopy.key.K_RIGHT,'z','c','q','n','z','c','q','n','z','c','q','n','z','c','q','n','z','c','q','n']

		stop = time.time()+10
		while time.time() < stop:
			time.sleep(.25)
			keynum = randrange(len(keys))
			action = randrange(3)
			if action == 0:
				autopy.key.toggle(keys[keynum], True)
			elif action == 1:
				autopy.key.toggle(keys[keynum], False)
			elif action == 2:
				autopy.key.tap(keys[keynum])

		# END ALGORITHM #
		
		# Stop all input
		i = 0
		while i < len(keys):
			autopy.key.toggle(keys[i], False)
			i += 1

		time.sleep(2)
		# Take a screenshot of the artwork and save to file
		titleofpiece = time.strftime("%Y%m%d%H%M%S")
		system("screencapture -R400,129,640,640 " + "output/" + titleofpiece + ".png")

		# Log the title of the art in the studio file
		f = open(path + '/output/studio.log', 'a')
		f.write('\n' + titleofpiece)
		f.close

		# Increment imgnum
		imgnum += 1


	# Shutdown ARTIST
	time.sleep(1)
	autopy.key.tap(autopy.key.K_ESCAPE)
	time.sleep(1)
	autopy.key.tap(autopy.key.K_ESCAPE)

	# Sync artwork and logs to server; TODO: The studio log is always 1 line behind, but I'm not sure why. FIX.
	system('rsync -a --exclude "' + EXCLUDES + '" -e "ssh -i ' + SSH_KEY + '" ' + LOCAL_DIRECTORY + ' ' + REMOTE_DIRECTORY)

if __name__ == "__main__":
    main()
