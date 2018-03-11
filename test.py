import vlc, pafy

url = "https://www.youtube.com/watch?v=wuGt8wanfhE"
video = pafy.new(url)
track = video.getbestaudio()
url2 = "https://www.youtube.com/watch?v=mkgl_f-DpXc"
video2 = pafy.new(url2)
track2 = video2.getbestaudio()

playlist = [track.url, track2.url]



for song in playlist:
    instance = vlc.Instance()
    media = instance.media_new(song)
    player = instance.media_player_new()
    player.set_media(media)
    player.play()
    print(song)