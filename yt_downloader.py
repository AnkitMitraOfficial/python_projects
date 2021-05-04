import pytube

# url_video = 'https://youtu.be/ioNng23DkIM'

# youtube = pytube.YouTube(url_video)
# streams = youtube.streams.all()

# for i in streams:
#     print(i)

url = 'https://youtu.be/ioNng23DkIM'


try:
    youtube = pytube.YouTube(url).streams.get_by_itag(18).download(r'C:\Users\Ankit Mitra\Desktop\downloads')
    print('Video successfully downloaded')

except Exception as e:
    print('Error:',e)
