#!/usr/bin/env python3
import globals
import os
import filetype
import img_check
import subprocess  # Deals with BASH commands

if __name__ == "__main__":
    globals.initialize()

# Updated

#############################################################
# Classes

class TextColours:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR


#############################################################
# Variables

photo_file = str
paragraph_width = 80


#############################################################
# The Definitions

def ruler_underline(ruler):
    print(ruler*paragraph_width)


#############################################################
# The Program
print("")
ruler_underline("=")
print("Photograph Timestamp to File Creation Time Script")
ruler_underline("=")

photos = os.listdir(globals.path_to_photos)

for n in photos:
    if '.JPG' in n or '.jpg' in n:
        path = globals.path_to_photos + n

        if globals.total_files_reviewed != 0:
            ruler_underline("-")

        globals.total_files_reviewed += 1
        if filetype.is_image(path):  # Is it a proper image?
            print(f"{TextColours.OK}Valid File{TextColours.RESET}")
            img_check.extract_meta(path, n, globals.valid_image, globals.successful_date_changes)

        elif filetype.is_video(path):  # Is it a proper video?
            print(f"{TextColours.WARNING}Valid video! Moving to ./Videos ...{TextColours.RESET}")

            # BASH command to move video files to ./Videos
            bashCommand = "mv -v " + path + " " + globals.path_to_videos
            print(bashCommand)
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

        else:
            print(f"{n} is {TextColours.FAIL}possibly NOT a valid video or image!{TextColours.RESET} Moved to ./other")

            # BASH code to move to ./other
            bashCommand = "mv -v " + path + " " + globals.path_to_other
            print(bashCommand)
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()


ruler_underline("=")
print(f"Total Files Reviewed: {globals.total_files_reviewed}")
print(f"Total Valid Image Files: {globals.valid_image - 1}")
print(f"Total Successful Changes to Image file Timestamps: {globals.successful_date_changes}")
ruler_underline("=")
