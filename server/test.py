from threading import Thread
import vlc, pafy, time

'''url = "https://www.youtube.com/watch?v=wuGt8wanfhE"
video = pafy.new(url)
track = video.getbestaudio()
url2 = "https://www.youtube.com/watch?v=mkgl_f-DpXc"
video2 = pafy.new(url2)
track2 = video2.getbestaudio()

song_list = [track.url]'''

def test():
    instance = vlc.Instance('--input-repeat=-1')
    for song in song_list:
        player=instance.media_player_new()
        media=instance.media_new(song)

        media.get_mrl()
        player.set_media(media)
        player.play()
        playing = set([1,2,3,4])
        time.sleep(1)
        duration = player.get_length() / 1000
        mm, ss = divmod(duration, 60)

        while True:
            state = player.get_state()
            if state not in playing:
                break
            continue

'''start_new_thread(test, ())
time.sleep(10)
song_list.append(track2.url)'''

lis = [1, 2, 3, 4]

def test2():
    try:
        time.sleep(1)
        for l in lis:
            print(l)
    except Exception as e:
        print(e)
        raise

def test3():
    global lis
    for i in range(5, 11):
        lis.append(i)


thread1 = Thread(target=test2)
thread2 = Thread(target=test3)


thread1.start()
thread2.start()