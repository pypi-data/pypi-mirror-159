import datetime
import random

global NAME
global AGE
global QUOTE
global TITLE
global MENTAL_HEALTH_VALUE
MENTAL_HEALTH_VALUE = 20


class Parlo:
    def __init__(self, name: str = "Parlo",
                 age: int | float = datetime.datetime.now().year - datetime.date(2005, 5, 3).year):
        global NAME
        NAME = name
        global AGE
        AGE = age
        global QUOTE
        QUOTE = ["Lisa Gaming ROBLOX is a manipulative doxxing scumbag.",
                 "All my enemies are Pedophiles",
                 "Lisa Gaming ROBLOX is a threat to the ROBLOX Community.",
                 "The Dip Dip Girls and Bun Bun Girls are fake hackers.",
                 "So recently...",
                 "Make sure to like and subscribe if you are new."]
        global TITLE
        TITLE = ["Oh No. (Roblox Bun Bun Girls Hackers)",
                 "Oh No. (Roblox Free Robux Scammers)",
                 "Oh No. (Roblox Dip Dip Girls Hackers)",
                 "Oh No. (Roblox Bun Bun Girls Hackers Leader)",
                 "STOP THIS ROBLOX...",
                 "Oh No. (Lisa Gaming ROBLOX)",
                 "Oh No. (Roblox Dip Dip Girls Hackers Leader)",
                 "INAPPROPRIATE ROBLOX EATING GLUE FACE IS BACK AGAIN!"]

        print(
            f"Hello! My name is Parlo, I am a ROBLOX Youtuber, and I am a clown. I am currently {AGE} year's old. My name is {NAME}")

    class Youtube:
        def __init__(self):
            pass

        def upload(self):
            global MENTAL_HEALTH_VALUE
            title: str = random.choice(TITLE)
            opening_quote: str = random.choice(QUOTE)
            views: int = random.randint(1, 20000)
            print(f"------------------------------\n"
                  f"Youtube | Search: {NAME}.. | +#O \n"
                  f"{title} \n"
                  f"{views} Views \n"
                  f"Transcript: \n"
                  f"{opening_quote}")
            if views > 5000:
                MENTAL_HEALTH_VALUE = MENTAL_HEALTH_VALUE + 1
            else:
                MENTAL_HEALTH_VALUE = MENTAL_HEALTH_VALUE - 5

    class Mental_Health:
        def __init__(self):
            pass

        def check(self):
            if 50 > MENTAL_HEALTH_VALUE > 40:
                print("Parlo lives another day!")
            if 39 > MENTAL_HEALTH_VALUE > 30:
                print("Parlo lives another day!... but he is not so happy.")
            if 29 > MENTAL_HEALTH_VALUE > 20:
                print("Parlo lives another day!... but that's running low.")
            if 19 > MENTAL_HEALTH_VALUE > 10:
                print("Parlo will probably kill himself tomorrow.... but he'll be alive today.")
            if 9 > MENTAL_HEALTH_VALUE > 0:
                print("Parlo Killed himself.")
                quit("Parlo fucking died.")
