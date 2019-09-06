from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=nbot=ChatBot('Prueba')
trainer = ListTrainer(bot)

for files in os.listdir('./Prueba/'): 
 data=open('./Prueba/'+files, 'r').readlines()
 trainer.train(data)
 trainer.train(data)
 trainer.train(data)

while True:
    message=input('\t\t\tYou:')
    if message.strip()!='Bye' or 'bye':
        reply=bot.get_response(message)
        print('disfrutomisalud:', reply)
    if message.strip()=='Bye':
        print('Disfrutomisalud: Bye')
        break