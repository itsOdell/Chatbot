import time
import socket
import random
from art import LOGO, success_style, input_style
print(LOGO)
from data import OAUTHS, MESSAGES


SERVER = ("irc.chat.twitch.tv", 6667)
channel = input(input_style + "Enter your channel name: ")
min_interval = int(input(input_style + "Enter minimum seconds bot should wait: "))
max_interval = int(input(input_style + "Enter maximum seconds bot should wait: "))

while True:
    random_oauth_token = random.choice(OAUTHS)
    random_message = random.choice(MESSAGES)
    random_sleep_time = random.uniform(min_interval, max_interval)
    time.sleep(random_sleep_time)

    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    irc.connect(SERVER)

    print(success_style + f"[{time.strftime('%X')}] Sending message: {random_message}")
    irc.send(f"PASS {random_oauth_token}\n".encode("utf-8"))
    irc.send(f"NICK {channel}\n".encode("utf-8"))
    irc.send(f"JOIN #{channel}\n".encode("utf-8"))
    irc.send(f"PRIVMSG #{channel} :{random_message}\n".encode("utf-8"))
    irc.close()
