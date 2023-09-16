import os
import time
import sys
from art import light_magenta, error_style


OAUTHS_LIST = f"{os.getcwd()}/oauths.txt"
MESSAGES_LIST = f"{os.getcwd()}/messages.txt"
OAUTHS = []
MESSAGES = []

if os.path.exists(OAUTHS_LIST) and os.path.getsize(OAUTHS_LIST) > 0:
    print(light_magenta + f"oauths.txt file detected. Appending accounts...")
    with open(OAUTHS_LIST, "r") as f:
        new_oauths = f.readlines()
        OAUTHS.extend(new_oauths)
else:
    print(light_magenta + f"{OAUTHS_LIST} file is empty or doesn't exist. Please create it and paste the oauth keys there.")
    time.sleep(10)
    sys.exit(-1)

if os.path.exists(MESSAGES_LIST) and os.path.getsize(MESSAGES_LIST) > 0:
    with open(MESSAGES_LIST, "r") as f:
        messages = f.readlines()
        MESSAGES.extend(messages)
elif os.path.exists(MESSAGES_LIST) is False:
    print(error_style + f"{OAUTHS_LIST} file not detected. Please create and write messages into it...")
    time.sleep(10)
    sys.exit(-1)
else:
    print(error_style + f"{MESSAGES_LIST} file detected but no content within it. Please add messages into it...")
    time.sleep(10)
    sys.exit(-1)
