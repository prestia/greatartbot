from twython import Twython
from keys import *
from os import getcwd
import linecache

# TODO: Generate titles for the artwork and set them as status.

def main():
	path = getcwd() + '/output/'

	# Open curator file to see which line of the studio log needs to be read
	f = open(path + 'curator.log', 'r+')
	bookmark = f.readline().rstrip()
	print bookmark
	index = int(bookmark)
	bookmark = int(bookmark) + 1
	f.seek(0)
	f.write(str(bookmark))
	f.truncate()
	f.close()

	# Read the title of the artwork from the specified line in the studio log, then strip the \n and save to titleofart
	titleofart = linecache.getline(path + 'studio.log', index).rstrip()

	artwork = open(path + titleofart + '.png', 'rb')
	promote(artwork)

def promote(masterpiece):

	t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	
	t.update_status_with_media(status='', media=masterpiece)

if __name__ == "__main__":
    main()