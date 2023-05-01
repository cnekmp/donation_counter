# donation_counter
This script will detect text of donation from live YouTube stream and count amount of donations


# Remarks
This is just concept that proves possibility of counting donations from live YouTube stream. Please feel free to fork this repo and make required improvements if you can and become a real maintaner of this code. I'm not interested in developing this script any further.
Tested on Arch Linux

# How to run

**Required packages:**

Streamlink: https://github.com/streamlink/streamlink

ffmpeg: https://github.com/FFmpeg/FFmpeg

EasyOCR: https://github.com/JaidedAI/EasyOCR

Telebot: https://pypi.org/project/pyTelegramBotAPI

1. Edit Live YouTube stream url in `save_png.sh` file
2. Run `./save_png.sh`  in terminal
3. Run `./process_png.py` in another terminal for text detection and sending messages to Telegram Bot. (do not forget to edit this file and provide correct TOKEN for bot and channel id)
