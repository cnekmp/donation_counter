#!/usr/bin/python

import re
import time
import easyocr
import telebot

chat_id = "-23213821312"                # Telegram channel id
# Load EasyOCR engine. It requires to be loaded only once
reader = easyocr.Reader(['en', 'ru'])
# Timeout between checking new png images that has been gathered by save_png.sh
timeout = 6
filename = 'live.png'                   # Target file
message_id = 0
donation_count = 0
new_donation = 0
old_donation = 0
firstRun = True
donator_name = ""
new_donator_name = ""
bot = telebot.TeleBot("13879231:AAsadasd0d-SYOOsasdqweqwd79xZhaJVeM",
                      parse_mode=None)  # Telegram Bot Token
while True:
    try:
        # Detect text from live.png
        result = reader.readtext(filename, detail=0, paragraph=True)
    except:
        # In case if reading file fails
        continue
    for x in result:
        print(x)
        # Find out donation text. Sometimes OCR may detect text falsely so we're extracting different matches with regex
        # Text may be like: Donator Name - 100 RUB, Donator Name - 100 RIBB and so on
        str = re.search(
            '\d+\s?\d+(\s|\/)?(R.B?|R[UI]BB|TRY?|USD?)', x)
        if str:
            # Filter out digits from the found pattern before
            new_donation = int(re.findall('\d+\s?\d+', x)
                               [-1].strip())
            new_donator_name = x.split()[0]
            if new_donator_name == donator_name or new_donation == old_donation:
                # In this case we're ignoring if next image detection processed same donation text for avoiding duplicates
                break
            if new_donator_name != donator_name or new_donation != old_donation:
                donation_count += new_donation
                old_donation = new_donation
                donator_name = new_donator_name
                print("new", new_donator_name, donator_name)
                print(new_donation, old_donation)
            print(re.findall('\d+\s?\d+', x)[-1])

            match firstRun:
                case True:
                    print(f'New: {donation_count}')
                    # Sending message via Telegram Bot to Channel
                    message = bot.send_message(
                        chat_id=chat_id, text=donation_count, disable_web_page_preview=True, disable_notification=True)
                    message_id = message.message_id
                    firstRun = False
                case False:
                    print(
                        f'Edit: {donation_count} Message id: {message_id}')
                    # Editing message via Telegram Bot in channel if the message already has been posted by bot
                    message = bot.edit_message_text(
                        chat_id=chat_id, message_id=message_id, disable_web_page_preview=True, text=donation_count)
            print(
                f'Final is {donation_count} Message id: {message_id}')
    # Waiting here for some time for avoiding duplicate donation screenshot
    time.sleep(timeout)
