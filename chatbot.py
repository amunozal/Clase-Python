#esta funcion
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def crearbot(): #crear una funcion llamada crearbot
    proyecto = input('Nombre del chatbot: ')
    os.mkdir(proyecto)
    os.mkdir(proyecto+'/'+proyecto)
    namechatbot = './'+proyecto+'/'+proyecto+'.yml'
    file = open(namechatbot, 'w')

    categoria = input('Escriba una categoria: ')
    file.write('categoria:' + os.linesep)
    file.write('-' + categoria + os.linesep)

    while True:
        continuar = input('Desea agregar otra: \n 1 - Agregar \n 2 - Terminar ')
        if continuar == '1':
            pregunta = input('Pregunta')
            respuesta = input('Respuesta')

            file.write('-- '+pregunta + os.linesep)
            file.write(' - '+respuesta + os.linesep)

        if continuar == '2':
            file.close()
            break
    namechatbot =  './'+proyecto+'/'+proyecto+'.py'
    file = open(namechatbot, 'w')
    file.write("from chatterbot import ChatBot\nfrom chatterbot.trainers import ListTrainer\nimport os\nbot=nbot=ChatBot('"+proyecto+"')\ntrainer = ListTrainer(bot)\n" + os.linesep)
    file.write("for files in os.listdir('./"+proyecto+"/'): \n data=open('./"+proyecto+"/'+files, 'r').readlines()\n trainer.train(data)\n trainer.train(data)\n trainer.train(data)\n"+os.linesep)
    file.close()



crearbot()

'''while True:
    message=input('\t\t\tYou:')
    if message.strip()!='Bye' or 'bye':
        reply=bot.get_response(message)
        print('disfrutomisalud:', reply)
    if message.strip()=='Bye':
        print('Disfrutomisalud: Bye')
        break'''