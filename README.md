Facebookland
============

Game we did for HackFMI's 0100'th edition. <br>
<br>
The game is top view 2D shooter.<br>
The difference from the other shooters is the idea that it uses your facebook friend list to generate unique levels(background, movement speeds, number of enemies, damage you deal and ect.).<br>
The name comes from facebook + crimsonland (http://www.crimsonland.com/).

Controls:<br>
W - forward<br>
S - flip backwords<br>
A, D - rotate left or right. You can rotate all the way up to 360 degrees.<br>

Game rules:<br>
At the begining are spawn zombies for every letter in your friend's name + one boss zombie, which holds the whole name.<br>
The game is over when you kill them or they kill you. Simple. BUT! On every X seconds, calculated depending on the level - more zombies are spawn.<br>

We did this game literally for ~~ 24 hours, so it is not finished.<br>

Future plans:<br>
Scoring system - killin one of the firs spawn zombies gives you +x points, the boss +y > |x| points.<br>
The zombies spawn after the beggining of the game give you -x points. So the idea is to finish the level as fast as possible.<br>

Cons:<br>
The facebook API is still not integraded (that goes to the future plans^), but you can still play with some build in names.<br>

We first thought to use C++ with SFML to make the game, but switched to Python + PyGame (3.4.*), because we only had about 2 days.<br>

For the levels menu we use PyQt4, so if you want to play - you need Python, PyGame, PyQt4. Yeah, I know, it's a lot, but they are installed literally for 10 minutes(+ downloading time).

So, have fun!!!
