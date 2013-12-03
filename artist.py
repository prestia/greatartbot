import time
import autopy
from subprocess import Popen
from os import system, getcwd
from random import randrange
from rsync import *

def main():
	path = getcwd()
	artistapp = path + "/artist_mac"

	# Launch ARTIST as a non-blocking subprocess
	Popen(artistapp)
	
	# Wait
	time.sleep(1)
	
	# Enter sketch mode
	autopy.key.tap('s')

	# MAKE ART
	imgnum = 0
	keys = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z',autopy.key.K_LEFT,autopy.key.K_RIGHT,autopy.key.K_DOWN,autopy.key.K_UP]

	# Remove the yellow square
	time.sleep(1)
	autopy.key.tap('x')

	while imgnum < 1:
		stop = time.time()+10
		while time.time() < stop:
			time.sleep(.5)
			keynum = randrange(len(keys))
			action = randrange(3)
			if action == 0:
				autopy.key.toggle(keys[keynum], True)
			elif action == 1:
				autopy.key.toggle(keys[keynum], False)
			elif action == 2:
				autopy.key.tap(keys[keynum])

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