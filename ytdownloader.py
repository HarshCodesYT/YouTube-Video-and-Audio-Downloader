from pytube import YouTube
while True:
    link = input("Enter video link: ")
    
    if link == "":
        print("Exiting...")
        break
    if link != "":
        yt = YouTube(link)

        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Length of video: " + str(yt.length) + "s")
        print("Rating: ", yt.rating)
        a = input("Enter 'd' to download, else enter 'r' for new link: ")
        
        if a =='d':
            b = input("MP3 or MP4: ")
            if b == "mp4":
                ys = yt.streams.get_highest_resolution()
                print("Downloading....")
                ys.download('Youtube Downloads (Video)')
                print("Download Complete!")
            if b == "mp3":
                ys = yt.streams.get_audio_only()
                print("Downloading....")
                ys.download('Youtube Downloads (Audio)')
                print("Download Complete!")


        if a =='r':
            continue
