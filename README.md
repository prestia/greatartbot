# @greatartbot

What is this?

[@greatartbot](http://twitter.com/greatartbot) is a fully automated artist. This vexing virtual virtuoso uses [Michael Brough](http://smestorp.com) and [Andi McClure](http://runhello.com)'s [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987) to create artwork that is sometimes beautiful and sometimes WAY TOO BEAUTIFUL FOR YOUR STUPID HUMAN EYES. Oh, yeah, it also shares them on twitter.

Requirements:
 * Autopy
 * Twython
 * Probably OS X. I dunno. Actually, yes, you probably need OS X. Whatever.

How To Use:
 * Drop (or clone) the files in this repo into the directory of the post-compo [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987).
 * Edit the settings in `keys.py.example` and `rsync.py.example`.
 * Set up cron jobs and see if it works on your system. I don't know. I'm an attorney, not a SOFTWARE ENGINEER.
 * You will probably have to change the coordinates of the screen capture unless you are also running OS X on a 1440 x 900 display.

Gist:
 * `artist.py` generates artwork in 10 seconds using a locally-installed copy of the post-compo [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987). The artwork is saved in `/output/` and the title of each art file is stored in `studio.log`.
 * `promoter.py` talks to `curator.log` and decides which artwork to share. `promoter.py` then gets the artwork from `studio.log`, stores it in the variable `masterpiece`, and sends it to the function `promote`, which shares the masterpiece on twitter.

Notes:
 * I will (probably) make this README more complete and helpful in the future.
 * I will (maybe, but not likely) make my code a bit cleaner and mess with the algorithm for generating art.
 * I will (absolutely) ask your forgiveness if you try to read this slop.

Future:
 * I'd really like to have `promoter.py` title each piece of work before tweeting it out. I'm having a hard time deciding where to draw words to assemble the titles from though. Suggestions are welcome.
 * ~~Make the bot a MUCH BETTER ARTIST by adding in [these keys](https://twitter.com/smestorp/status/408015839078539264).~~

License:
 * It has one.

MOST IMPORTANTLY (that's why it's at the bottom, duh):
 * Thanks to [Michael Brough](http://smestorp.com) ([@smestorp](http://twitter.com/smestorp)) & [Andi McClure](http://runhello.com) ([@mcclure111](https://twitter.com/mcclure111)) for making [Become a Great Artist in Just 10 Seconds](http://www.ludumdare.com/compo/ludum-dare-27/comment-page-1/?action=preview&uid=4987).