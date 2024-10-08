from bs4 import BeautifulSoup
import telebot
import time
import threading
import requests
from keep import keep_alive
import os
from datetime import datetime
now = datetime.now()
from pillo import seamcombo


keep_alive()

Token = os.environ["Auth"]
bot = telebot.TeleBot(Token)

useruid = ["-1002212093901"]
adminuid = []

hamster_com = ""
hamster_chi = ""
run_b = False

def hamster():
    clist = []
    response = requests.get("https://hamsterkombo.com/")
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")
    for x in articles:
        h1_tag = x.find("h1")
        if h1_tag and h1_tag.find("span", text="Hamster Kombat"):
            date = "©®"
            combo = f"Hamster Kombat Combo\n\nDate : {date}\n"
            morse = f"Daily Cipher Code\n\nDate : {date}\n"
            combo_div = x.find_all("div", class_="relative w-full")
            for y in combo_div:
                pngu = y.find_all("div",class_="custom-aspect-ratio flex flex-col items-center justify-center bg-slate-800 w-[88%] rounded-full")
                for n in pngu:
                    clist.append(n.get("style").split(";")[-3].split("(")[-1].replace(")",""))
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
    return {"combo": combo, "morse": morse,"list": clist}


def send_msg(msg):
    for g in useruid:
        bot.send_message(g, msg)


def main():
    msg = "Testing"
    bot.send_message("1906998334", msg)
    global hamster_com, hamster_chi
    while True:
        sdate = f"{now.day} {now.strftime('%B')}"
        try:
            resp = requests.get("https://crypto-gp9d.onrender.com")
            hamster_data = hamster()
            if hamster_com == "" and hamster_chi == "":
                hamster_com = hamster_data["combo"]
                hamster_chi = hamster_data["morse"]
            elif hamster_data["combo"] != hamster_com:
                hamster_com = hamster_data["combo"]
                io = 1
                for q in hamster_data["list"]:
                    print(q)
                    img_data = requests.get(f"https://hamsterkombo.com/{q}").content
                    with open(f'pic{io}.webp', 'wb') as handler:
                        handler.write(img_data)
                    io = io +1
                zaora = hamster_com.split("\n")
                sub1 = zaora[-3].split("---->")[1]
                sub2 = zaora[-2].split("---->")[1]
                sub3 = zaora[-1].split("---->")[1]
                tag1 = zaora[-3].split("---->")[0]
                tag2 = zaora[-2].split("---->")[0]
                tag3 = zaora[-1].split("---->")[0]
                seamcombo(sdate,"pic1.webp","pic2.webp","pic3.webp",sub1,sub2,sub3,tag1,tag2,tag3)
                with open("send-combo.png", 'rb') as photo:
                    bot.send_photo("-1002212093901", photo)
                        
            elif hamster_data["morse"] != hamster_chi:
                hamster_chi = hamster_data["morse"]
                bot.send_message("-4181045120",hamster_chi.replace("©®",f"{now.day} {now.strftime('%B')}"))
                if run_b == True:
                    send_msg(hamster_data["morse"].replace("©®",f"{now.day} {now.strftime('%B')}"))
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
    bot.send_message("-4181045120",hamster_chi.replace("©®",f"{now.day} {now.strftime('%B')}"))
    bot.send_message("-4181045120",hamster_com.replace("©®",f"{now.day} {now.strftime('%B')}"))

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
