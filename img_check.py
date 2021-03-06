from exif import Image  # Doesn't play nice with Pillow
import globals
import subprocess  # Deals with BASH commands

if __name__ == "__main__":
    globals.initialize()


#############################################################
# Classes

class TextColours:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR

#############################################################


def extract_meta(path, n, valid_image, successful_date_changes):

    with open(path, "rb") as file:
        photo_file = Image(file)

    images = [photo_file]

    try:  # In case the file is corrupt or unreadable by exif
        for index, image in enumerate(images):

            if image.has_exif:
                state = image.get('datetime_original', 'Unknown')
                print(f"Filename:                {n}")
                print(f"Make:                    {image.get('make', 'Unknown')}")
                print(f"Model:                   {image.get('model', 'Unknown')}")
                print(f"Date:                    {image.get('datetime_original', 'Unknown')}")
                print(f"EXIF Photo Count:        {globals.valid_image}")

                if (state != 'Unknown'):
                    print(f"{TextColours.OK}File Creation Time: Re-stamped{TextColours.RESET}")
                    globals.successful_date_changes += 1

                    # BASH code to timestamp the file
                    stamp = image.get('datetime_original')
                    year = stamp[0:4]
                    month = stamp[5:7]
                    day = stamp[8:10]
                    time = stamp[11:19]
                    timestamp = year + "-" + month + "-" + day + " " + time
                    print(timestamp)

                    bashCommand = 'sudo touch -d ' + timestamp + " " + n
                    print(bashCommand)
                    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
                    output, error = process.communicate()
            else:
                print(f"Filename:                {n}")
                print(f"No EXIF information found. No action taken.")
                globals.valid_image -= 1
        globals.valid_image += 1
    except:
        print(f"{n} could be a {TextColours.FAIL}CORRUPTED FILE!{TextColours.RESET}")

        # BASH code to move the corrupted file to ./corrupted
        bashCommand = "mv -v " + path + " " + globals.path_to_corrupted
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

    return globals.valid_image
    return globals.successful_date_changes