import youtube_dl
# 動画
ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s','format':'137'})

with ydl:
    result = ydl.extract_info(
        'https://www.youtube.com/watch?v=sr--GVIoluU',
        download=True # We just want to extract the info
    )

# 音声のみ ffmpeg必須
# ydl_opts = {
#     'format': 'bestaudio/best',
#     'outtmpl':  "sample_music" + '.%(ext)s',
#     'postprocessors': [
#         {'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#          'preferredquality': '192'},
#         {'key': 'FFmpegMetadata'},
#     ],
# }

# ydl = youtube_dl.YoutubeDL(ydl_opts)
# info_dict = ydl.extract_info("https://www.youtube.com/watch?v=sr--GVIoluU", download=True)