# Easily Download Youtube videos as .mp3 files
## Needs the following modules in order to work:
- ffmpeg
- youtube_dl
- tkinter
> Can be installed by using pip install 'module name'

## Documentation:
- ytmp3.py has the main download related source code and is capable of running independently via command line
- ytmp3UI.py has the UI related code and uses ytmp3 as a module to allow users easily download their videos.
- Opening ytmp3UI.py should open a UI frame asking for the video's URl. On clicking Download, the download will begin and the UI will show the status once the download is complete.
- The downloaded .mp3 file will be present in the same folder/directory as the python files.
