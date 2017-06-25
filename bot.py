import telepot
from telepot.loop import MessageLoop
import sys
import requests
import time

#Connection with and WebService
bot = telepot.Bot('API_BOT')

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']
	email = command.strip('/pwn3d ')
	check = '/pwn3d ' + email
	response = requests.get("http://10.0.0.50:8000/consult?query=" + email)
	if command == '/start':
		bot.sendMessage(chat_id, "Hello bro! This bot check for you if your e-mail has been leaked! Send to me a '/help' message.\n Don't forget to visit http://securityattack.com.br/")
	if command == '/about':
		bot.sendMessage(chat_id, "This bot was made for educational purposes only.\n If you want help me with more leaks, send me a pm. \n Owner: @Warflop\n Visit blog: http://securityattack.com.br")
	if command == '/help':
		bot.sendMessage(chat_id, "*/pwn3d email@email.com* - Check if your e-mail has been leaked.\n */about* - Show more information about DEV.\n */help* - Understand ours commands." ,parse_mode="MARKDOWN")
	if command == check:
		if response.status_code == 200:
			bot.sendMessage(chat_id, "*Dropbox Pass:*\n- Hash: " + resposta.content.strip('"'), parse_mode="MARKDOWN")
		else:
			bot.sendMessage(chat_id, "NOT PWN3D, YET!!! Keep Calm. We are updating our database.")

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)
