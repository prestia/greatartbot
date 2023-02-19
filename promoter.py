from twython import Twython
from mastodon import Mastodon
from twitter_keys import *
from os import getcwd
import linecache

def main():
	path = getcwd() + '/output/'

	# Open curator file to see which line of the studio log needs to be read
	f = open(path + 'curator.log', 'r+')
	bookmark = f.readline().rstrip()
	index = int(bookmark)
	bookmark = int(bookmark) + 1
	f.seek(0)
	f.write(str(bookmark))
	f.truncate()
	f.close()

	# Read the title of the artwork from the specified line in the studio log, then strip the \n and save to titleofart
	titleofart = linecache.getline(path + 'studio.log', index).rstrip()

	tweet(open(path + titleofart + '.png', 'rb'))
	toot(open(path + titleofart + '.png', 'rb'))

def toot(masterpiece):

	m = Mastodon(access_token='mastodon.secret', api_base_url='https://botsin.space')
	art = m.media_post(masterpiece, "image/png")
	m.status_post("", media_ids=art["id"])
	
def tweet(masterpiece):

	t = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	t.update_status_with_media(status='', media=masterpiece)

if __name__ == "__main__":
    main()
