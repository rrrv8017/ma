#======{iMPORT}======#
import requests
import random
import telebot
from telebot import types
#======{START}======#
token = input("Enter token bot : ")
ID = input("Enter id Tele : ")
hit = 0
bad = 0
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
 
 bot.reply_to(message,f'''*- Hi Boss ðŸ‘‹
- Bot Check User Telegram ðŸ¤–
- Send /StHe
- Coded By : @PiPPi ðŸ“¢*''',parse_mode="markdown")

@bot.message_handler(commands=['StHe'])
def send_tool(message):
    key = types.ReplyKeyboardMarkup(row_width=1)
    but1 = types.KeyboardButton('â€¢ Check - 3 -')
    but2 = types.KeyboardButton('â€¢ Check - 4 -')
    but3 = types.KeyboardButton('â€¢ Check User - 5 -')
    
    key.add(but1,but2,but3)
    send = bot.send_message(message.chat.id , "*Hi Boss*" ,reply_markup = key,parse_mode="markdown")
@bot.message_handler(func=lambda m: True)
def trakos(message):
 global bad,hit,key
 if message.text == "â€¢ Check - 3 -": 
  start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start done").json()
  id_msg =(start_msg['result']["message_id"])
  while True:
            user = 'QWERTYUIOPASDFGHJKLZXCVNBM'
            us = str("".join(random.choice(user)for i in range(3)))
            username = us+'bot'
            url = f"https://t.me/{username}"
            req = requests.get(url)
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
                      hit+=1
                      bot.send_message(message.chat.id, text=f"@{username}",parse_mode="markdown")
            else:
                  bad+=1
                  requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=â€¢ Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\nâ€¢ Error User : {bad}\nâ€¢ Done User : {hit}\nâ€¢ In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nâ€¢ From : @ZZBoTs - @PiPPi")                 
#===============#
 if message.text == "â€¢ Check - 4 -": 
  start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start done").json()
  id_msg =(start_msg['result']["message_id"])
  while True:
            user = 'QWERTYUIOPASDFGHJKLZXCVNBM1234567890'
            us = str("".join(random.choice(user)for i in range(4)))
            username = us+'bot'
            url = f"https://t.me/{username}"
            req = requests.get(url)
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
                      hit+=1
                      bot.send_message(message.chat.id, text=f"@{username}",parse_mode="markdown")
            else:
                  bad+=1
                  requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=â€¢ Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\nâ€¢ Error User : {bad}\nâ€¢ Done User : {hit}\nâ€¢ In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nâ€¢ From : @ZZBoTs - @PiPPi")
#===============#
 if message.text == "â€¢ Check User - 5 -": 
  start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=start done").json()
  id_msg =(start_msg['result']["message_id"])
  while True:
            user = 'QWERTYUIOPASDFGHJKLZXCVNBM1234567890'
            us = str("".join(random.choice(user)for i in range(1)))
            uss = str("".join(random.choice(user)for i in range(1)))
            username = us+uss+uss+'bot'
            url = f"https://t.me/{username}"
            req = requests.get(url)
            if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
                      hit+=1
                      bot.send_message(message.chat.id, text=f"@{username}",parse_mode="markdown")
            else:
                  bad+=1
                  requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=â€¢ Hi Check Username Bot\n<~>~>~>~>~>~>~>~>~>\nâ€¢ Error User : {bad}\nâ€¢ Done User : {hit}\nâ€¢ In User : @{username}\n<~>~>~>~>~>~>~>~>~>\nâ€¢ From : @ZZBoTs - @PiPPi")
    
         
bot.polling(True)