# Author: Nathan
# Thanks to : x9
# Date: 15 Feb 2024
# Decrypt : SSH ( HTTP CUSTOM )
# Telegram: https://t.me/JustNathCh
##############################################
# Edit Token ( line 42 )
##############################################
import telepot
from telepot.loop import MessageLoop
import sys

def dec_ssh(ld):
    userlv = [i for i in ld.split('.')][::2]
    userld = [i for i in ld.split('.')][1::2]
    newld = ""
    for x in range(len(userld)):
        v = int(userlv[x]) - len(userlv)
        w = int(userld[x]) - len(userlv)
        m = (v // (2**w)) % 256
        newld += chr(m)
    return newld

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    command = msg['text']

    if command.startswith('/start'):
        welcome_message = "Welcome to SSH Decryptor Bot! Send your SSH in the format 'server:port@user:password' to decrypt.\n\nExample :\n\n/ssh ghoib.yassvpn.my.id:80@1816222515.26.-311413773.26.2084410589.15.1860953566.29.-571366538.8:1634639683.18.2103174923.19.-1303003589.28.-619656904.14.1037451608.17"

        bot.sendMessage(chat_id, welcome_message)
      
    if command.startswith('/ssh'):
        encrypted_data = command.split(' ', 1)[1]
        server = encrypted_data.split('@')[0].split(':')[0]
        port = encrypted_data.split('@')[0].split(':')[1]
        user = dec_ssh(encrypted_data.split('@')[1].split(':')[0])
        passw = dec_ssh(encrypted_data.split('@')[1].split(':')[1])

        response = f'╭──────────────────────\n│𝙎𝙎𝙃 𝘿𝙚𝙘𝙧𝙮𝙥𝙩𝙤𝙧\n├──────────────────────\n├ • 𝙎𝙚𝙧𝙫𝙚𝙧 : {server}\n├ • 𝙋𝙤𝙧𝙩 : {port}\n├ • 𝙐𝙨𝙚𝙧𝙣𝙖𝙢𝙚: {user}\n├ • 𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙: {passw}\n├──────────────────────\n├ ◉ 𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧 : @Nathanaeru\n├ ◉ 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 : @JustNathCh\n├ ◉ 𝘽𝙤𝙩 : @Clara_Agatha_bot\n╰──────────────────────'
        bot.sendMessage(chat_id, response)

bot = telepot.Bot('INPUT_BOT_TOKEN') # input your bot token
MessageLoop(bot, handle).run_as_thread()

print('Bot Activate by Nathan')

while True:
    pass
      
