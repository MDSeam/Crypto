from bs4 import BeautifulSoup
import telebot
import time
import threading
import requests
from keep import keep_alive
import os

keep_alive()

Token = os.environ["Auth"]
bot = telebot.TeleBot(Token)

useruid = ["-1002212093901"]
adminuid = []

hamster_com = ""
hamster_chi = ""
run_b = False

def hamster():
    response = requests.get("https://hamsterkombo.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")
    for x in articles:
        h1_tag = x.find("h1")
        if h1_tag and h1_tag.find("span", text="Hamster Kombat"):
            date = x.find(
                "span", string=lambda text: "date" in text.lower()
            ).text.replace("Date:", "")
            combo = f"Hamster Kombat Combo\n\nDate : {date}\n"
            morse = f"Daily Cipher Code\n\nDate : {date}\n"
            combo_div = x.find_all("div", class_="relative w-full")
            for y in combo_div:
                data = y.find_all("span")
                combo = combo + f"\n{data[1].text}  ---->  {data[0].text}"
            morse_div = x.find(
                "div", class_="contents font-poppins text-[22px] text-center font-light"
            )
            word = morse_div.find("span").text
            morse = morse + f"\n\nWord: {word}\n\nMorse:\n\n"
            for z in morse_div.find_all("span", class_="font-semibold notranslate"):
                if word not in z:
                    morse = morse + f"{z.text} "
            morse = morse + f"\n\nSimplified:\n"
            for z in morse_div.find_all("div", class_="inline-block notranslate"):
                morse = (
                    morse
                    + f"\n{z.find_all('span')[0].text} {''.join(dot.text for dot in (z.find_all('span')[1:]))}"
                )

            break
    return {"combo": combo, "morse": morse}


def send_msg(msg):
    for g in useruid:
        bot.send_message(g, msg)


def main():
    msg = "Testing"
    bot.send_message("1906998334", msg)
    global hamster_com, hamster_chi
    while True:
        try:
            resp = requests.get("https://crypto-gp9d.onrender.com")
            hamster_data = hamster()
            if hamster_com == "" and hamster_chi == "":
                hamster_com = hamster_data["combo"]
                hamster_chi = hamster_data["morse"]
            elif hamster_data["morse"] != hamster_chi:
                hamster_chi = hamster_data["morse"]
                if run_b == True:
                    send_msg(hamster_data["morse"])
            elif hamster_data["combo"] != hamster_com:
                hamster_com = hamster_data["combo"]
                if run_b == True:
                    send_msg(hamster_data["combo"])
            else:
                time.sleep(5)

        except Exception as e:
            bot.send_message("1906998334", e)
            break


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(commands=["hamster"])
def send_welcome(message):
    global hamster_com, hamster_chi
    hamster_com = ""
    hamster_chi = ""

@bot.message_handler(commands=["test"])
def send_welcome(message):
    bot.send_message("-4181045120",hamster_chi)
    bot.send_message("-4181045120",hamster_com)

@bot.message_handler(commands=["ccom"])
def send_welcome(message):
    global hamster_com
    hamster_com = 'Changed'
    bot.send_message(message.chat.id,"Combo changed")

@bot.message_handler(commands=["cchi"])
def send_welcome(message):
    global hamster_chi
    hamster_chi = 'Changed'
    bot.send_message(message.chat.id,"Chiher changed")
    

@bot.message_handler(commands=["run"])
def send_welcome(message):
    global run_b
    if run_b == False:
        run_b = True
    else:
        run_b = False
    bot.send_message(message.chat.id,f"Program run {run_b}")


polling_thread = threading.Thread(target=main)
polling_thread.start()
bot.infinity_polling()
