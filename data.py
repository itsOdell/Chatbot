import os
import time
import sys
from art import light_magenta, error_style


OAUTHS_LIST = f"{os.getcwd()}/oauths.txt"
MESSAGES_LIST = f"{os.getcwd()}/messages.txt"
OAUTHS = [
    "oauth:9cv3cpgl09su330syw4wn4yp5dp7ye",
    "oauth:96cv60oq6fz5w4uy49a4jsz4i9r35l",
    "oauth:r7oltjudmb6tjxw8s3l1367lwjaz9n",
    "oauth:7703k5u3tu446rlwmt5xcca1htk5xg",
    "oauth:zkqrs0gq6lctwciv2edfy17t913o7q",
    "oauth:8bw8lxmgqywlhjrt2lmf0biyxcv962",
    "oauth:9f5rpr4f0et9f6mg170at29jr3afbm",
    "oauth:a7yzfavnrwolxw15s1m9eft3ksjhq4",
    "oauth:o1cfbjbhb7kfom8677ghl2nnzqlg6j",
    "oauth:8sb9259358gmiun3qpnen491344vm9",
    "oauth:7nn5oze5f7pion0qyq2vxzpdll7kwp",
    "oauth:lfrwqqy3oqu96u546hteg6u9a92ynj",
    "oauth:a7yzfavnrwolxw15s1m9eft3ksjhq4",
    "oauth:o1cfbjbhb7kfom8677ghl2nnzqlg6j",
    "oauth:8sb9259358gmiun3qpnen491344vm9",
    "oauth:cq5b6aiz5pifjb9nphd3gbcdooc9cw",
    "oauth:r7oltjudmb6tjxw8s3l1367lwjaz9n",
    "oauth:7703k5u3tu446rlwmt5xcca1htk5xg",
    "oauth:zkqrs0gq6lctwciv2edfy17t913o7q",
    "oauth:ed3v982tm9lekfd8f24bzsdadt201l",
    "oauth:io6qomg901bh5ujla70b64ehdltjza",
    "oauth:l2pjv6pqu92ed947hrz6noxh1oz85n",
    "oauth:k8is25dkzgkwoi7wbl1xb43w60tm4a",
    "oauth:ntxs0kt7unvzbodav9r2t9q5j1kxqc"
]
MESSAGES = []

if os.path.exists(OAUTHS_LIST) and os.path.getsize(OAUTHS_LIST) > 0:
    print(light_magenta + f"oauths.txt file detected. Appending accounts...")
    with open(OAUTHS_LIST, "r") as f:
        new_oauths = f.readlines()
        OAUTHS.extend(new_oauths)
else:
    print(light_magenta + f"{OAUTHS_LIST} file not detected. Using {len(OAUTHS)} accounts provided by Horizons Edge as default")

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
