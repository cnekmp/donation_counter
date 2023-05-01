#!/bin/bash
#
# Remove live.png so ffmpeg won't complain that live.png file is already exist
rm -rf ./live.png
# Following command will get screenshot every 6 seconds from YouTube live stream and save it as live.png for EasyOCR text detection and processing
streamlink "https://www.youtube.com/watch?v=FSNic3wcdzM" best -O | ffmpeg -i pipe:0 -vf fps=1/6 -update 1 ./live.png