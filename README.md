#What's that?

You might wanna play your music through your Hifi system or sth similar and want to control the music remotely since this is more convenient. Alexa and Google Home are great, but unfortunately they cannot play YouTube or Soundcloud. Afaik they also can't build up an individual queue which was created spontanously, only playlists.

This might be a nice addition. You can connect the stationary machine (in my case a Raspberry Pi) which plays the music and can add Audio from YouTube and Soundcloud. If the Player is running a song, every additional Song will added to the queue.
E.g. if you have guests, everyone can add (his/her recommended) music to the queue via the network. No matter which device.

Clientside: Should be a webpage still (in development; current task/goal)
Serverside: Plays the music via VLC player

### Prerequisites
***Python3***, ***python-pip*** and ***VLC Player*** should be also available for Windows
##### Arch Linux
`sudo pacman -S python python-pip vlc` 
##### Rasperian (/ Debian), usually pre-installed:
`sudo apt-get install python3 python-pip vlc`
#### Python Packages
These are necessary to fetch the meta data (title etc.) from youtube links
***pafy*** `pip install pafy`
***youtube-dl*** 'pip install youtube-dl'


###Set IP-address within network so other devices can acces the server
Set `host` in `server.py` to public available IP address
#### How to determine available IP address for the server
Open a terminal and type in following commands (see under). Choose the interface which connects the device where the server is running to the internet.
##### Debian (Tested on Raspberian): `ifconfig` 
##### Arch Linux: `ip addr` 
##### Windows (in cmd): `ipconfig`

#### Demo / Example on getting an IP address
![Alt Text](https://github.com/nEihTfool2/yt-remote/blob/master/how-to-set-public-IP/preview.gif?raw=true)

Since my machine is connected via WiFi, I am choosing the interface `wlo1` 
For testing purposes, it is of course more convenient to use `localhost`instead.

After that, just run `server.py`:
`python server.py # If you're using Arch`
or
`python3 server.py # If you're using Debian`

(Dunno how on Windows)