
class Download:
    def getaudio(url):
        from pytube import YouTube
        import os

        # url input from user
        yt = YouTube(str(url))

        # extract only audio
        video = yt.streams.filter(only_audio=True).first()

        # check for destination to save file
        _dirname = os.getcwd()
        destination = os.path.join(_dirname, "Download")
        # print("Enter the destination (leave blank for current directory)")
        # destination = str(input(">> ")) or '.'

        # download the file
        out_file = video.download(output_path=destination)

        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        try:
            os.rename(out_file, new_file)
        except:
            pass

        # result of success
        #print(yt.title + " has been successfully downloaded.")
        #print("File : " + new_file)
        return yt.title + ".mp3"
