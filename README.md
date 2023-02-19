# @greatartbot

What is this?

[@greatartbot](http://twitter.com/greatartbot) (also [@greatartbot@botsin.space](https://botsin.space/@greatartbot)) is a fully automated artist. This vexing virtual virtuoso uses [Michael Brough](http://smestorp.com) and [Andi McClure](http://runhello.com)'s [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987) to create artwork that is sometimes beautiful and sometimes WAY TOO BEAUTIFUL FOR YOUR STUPID HUMAN EYES. Oh, yeah, it also shares them on twitter. And now Mastodon!

Special Note:

The production version of @greatartbot has evolved significantly since the release of this code. If you follow the bot, you've likely noticed that its output has evolved over time. This evolution is largely the result of me biasing the algorithm toward output that I enjoy, but I've also been experimenting with having the bot learn from Twitter feedback. This, in my opinion, is the most interesting part of a bot like @greatartbot. I encourage you all to fiddle with this code and make great artists of your own!

Requirements:
 * Autopy
 * Twython
 * Mastodon.py
 * Probably OS X. I dunno. Actually, yes, you probably need OS X. Whatever.

How To Use:
 * Drop (or clone) the files in this repo into the directory of the post-compo [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987).
 * Edit the settings in `keys.py.example`, `rsync.py.example`, and paste your Mastodon API key into `mastodon.secret`.
 * Set up cron jobs and see if it works on your system. I don't know. I'm an attorney, not a SOFTWARE ENGINEER.
 * You will probably have to change the coordinates of the screen capture unless you are also running OS X on a 1440 x 900 display.

Gist:
 * `artist.py` generates artwork in 10 seconds using a locally-installed copy of the post-compo [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987). The artwork is saved in `/output/` and the title of each art file is stored in `studio.log`.
 * `promoter.py` talks to `curator.log` and decides which artwork to share. `promoter.py` then gets the artwork from `studio.log`, stores it in the variable `masterpiece`, and sends it to the function `promote`, which shares the masterpiece on twitter.

Notes:
 * I will (probably) make this README more complete and helpful in the future.
 * I will (maybe, but not likely) make my code a bit cleaner.
 * I will (absolutely) ask your forgiveness if you try to read this slop.

Future:
 * I'd really like to have `promoter.py` title each piece of work before tweeting it out. I'm having a hard time deciding where to draw words to assemble the titles from though. Suggestions are welcome.

License:
 * It has one.

MOST IMPORTANTLY (that's why it's at the bottom, duh):
 * Thanks to [Michael Brough](http://smestorp.com) ([@smestorp](http://twitter.com/smestorp)) & [Andi McClure](http://runhello.com) ([@mcclure111](https://twitter.com/mcclure111)) for making [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987).
