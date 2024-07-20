from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://www.youtube.com/watch?v=WCM8FZlFTas"

yt = YouTube(url, use_oauth=True, allow_oauth_cache=True, on_progress_callback=on_progress)

print("Title:", yt.title)

video_streams = yt.streams.filter(file_extension='mp4', only_video=True)

resolutions = sorted(set(s.resolution for s in video_streams if s.resolution), reverse=True)
print("Available resolutions:")
for idx, res in enumerate(resolutions):
    print(f"{idx + 1}: {res}")

selection = int(input("Enter the number corresponding to the desired resolution: ")) - 1

if 0 <= selection < len(resolutions):
    selected_res = resolutions[selection]
    selected_stream = next(s for s in video_streams if s.resolution == selected_res)
    print(f"Selected Resolution: {selected_res}")
    selected_stream.download()
else:
    print("Invalid selection")
