
# coding: utf-8

# In[1]:


token = '449752038:AAEZFDEWFo2XFwSR2WH9Za8wxPetINhRIoU'

import telebot
from decode_kitty_Tbot import *
from encode_kitty_Tbot import *
from crypt_class import *
import PIL.Image as Image
import pickle as pk
import random
import numpy

bot = telebot.TeleBot(token)


# In[ ]:


de_en_chs = telebot.types.ReplyKeyboardMarkup()
doit = telebot.types.ReplyKeyboardMarkup()
doit.row('/doit', '/choose')
de_en_chs.row("/Encoder","/Decoder")
rem_chs = telebot.types.ReplyKeyboardRemove()

src = ''
Img = True
text = ''

Encoder = True

def save(ob, p):
    with open(p, 'wb') as f:
        pk.dump(ob, f)
def opop(p):
    x = 0
    with open(p, 'rb') as f:
        x = pk.load(f)
    return x
def start_polling():
    try:
        @bot.message_handler(func=lambda message: True, commands=['choose'], content_types=['text'])
        def to_chs(message):
            bot.send_message(message.chat.id, "Choose an option.", reply_markup=de_en_chs)

        @bot.message_handler(func=lambda message: True, commands=['delete_sources'], content_types=['text'])
        def del_inf(message):
            try:
                sr = opop('path/imp_'+str(message.chat.id))
                wsrc = 'sendings/'+sr[7:-4]+'.bmp'
                path = os.path.join(os.path.abspath(os.path.dirname(__file__)), sr)
                os.remove(path)
                bot.send_message(message.chat.id, "Deleted all your media (on server)", reply_markup=de_en_chs)
            except:
                bot.send_message(message.chat.id, "Some of your info has damaged or not exist.", reply_markup=de_en_chs)


        @bot.message_handler(func=lambda message: True, commands=['start'], content_types=['text'])
        def stra(message):
            print('New user. Id: '+str(message.chat.id))
            bot.send_message(message.chat.id, "Choose an option. or print /help", reply_markup=de_en_chs)

        @bot.message_handler(func=lambda message: True, commands=['do_not_doit'], content_types=['text'])
        def okay(message):
            bot.send_message(message.chat.id, "Okay, okay...")


        @bot.message_handler(func=lambda message: True, commands=['help'], content_types=['text'])
        def help_mes(message):
            bot.send_message(message.chat.id, "Type /start or /choose to choose programm \n Encoder: Crypt text to img \n Decoder: Extract text from img\nCommand list:\n /start\n /choose\n /help\n /Encoder\n /Decoder\n /doit\n /do_not_doit\n\n All questions to me:\nhttps://vk.com/alvspunctualiti", reply_markup=rem_chs)

        @bot.message_handler(func=lambda message: True,commands=['Encoder'])
        def encoder(message):
            Encoder = True
            save(Encoder, 'path/en_'+str(message.chat.id))
            bot.send_message(message.chat.id, 'You`ve choosed Encoder programm\n Send him (bot) photo \n(like document, not like photo, only jpg or bmp) and text \nThen print /doit', reply_markup=doit)

        @bot.message_handler(func=lambda message: True,commands=['Decoder'])
        def decoder(message):
            Encoder = False
            save(Encoder, 'path/en_'+str(message.chat.id))
            bot.send_message(message.chat.id, 'You`ve choosed Decoder programm \nSend him (bot) photo \n(like document, not like photo, and only bmp) \nThen print /doit', reply_markup=doit)

        @bot.message_handler(func=lambda message: True, commands=['doit'])
        def coding(message):
            Encoder = opop('path/en_'+str(message.chat.id))
            a = ''
            if Encoder:
                a = 'e_'
            else:
                a = 'd_'
            if Encoder:
                try:
                    print('User '+str(message.chat.id)+' started Encoding.')
                    sr = opop('path/imp_'+a+str(message.chat.id))
                    text = opop('path/text_'+str(message.chat.id))
                    bot.send_message(message.chat.id, 'Compressing...')
                    Img = np.array(Image.open(open(sr, 'rb')))
                    to_crypt = to_bin(text)
                    Img_write = transforming_the_image(to_crypt, Img)
                    imm = Image.fromarray(Img_write)
                    wsrc = 'sendings/'+sr[7:-4]+'.bmp'
                    imm.save(wsrc)
                    bot.send_document(message.chat.id, open(wsrc, 'rb'))
                    bot.send_message(message.chat.id, 'Encoded. \nNow you can share this pic.')
                    print('User '+str(message.chat.id)+' have his pic Encoded.')
                except:
                    bot.send_message(message.chat.id, 'Some problem caused.\nTry to repeat the actions, or wait.')
            else:
                try:
                    print('User '+str(message.chat.id)+' Decompressing')
                    sr = opop('path/imp_'+a+str(message.chat.id))
                    bot.send_message(message.chat.id, 'Decompressing...')
                    ex_out = extracting_from_image(np.array(Image.open(open(sr, 'rb'))))
                    out = extract_from_extracted(ex_out, '00000000'[:-1])
                    res = to_chr(out)
                    res = dcrypt(res)
                    bot.send_message(message.chat.id, 'Crypted Text:')
                    bot.send_message(message.chat.id, res)
                    print('User '+str(message.chat.id)+' have his text Decoded.')
                except:
                    bot.send_message(message.chat.id, 'Some prouble caused.\nProbably you didn`t send me a photo.')

        @bot.message_handler(func=lambda message: True,content_types=['text'])
        def text_add(message):
            text = message.text
            print('User '+str(message.chat.id)+' added the text')
            text = crypt(text)
            with open('path/text_'+str(message.chat.id), 'wb') as f:
                pk.dump(text, f)
            bot.send_message(message.chat.id, 'Text_added')

        @bot.message_handler(content_types=['document'])
        def photo_add(message):
            Encoder = opop('path/en_'+str(message.chat.id))
            pt = ''
            a = ''
            if Encoder:
                pt = 'photos/Enc_'
                a = 'e_'
            else:
                pt = 'photos/Dec_'
                a = 'd_'
            try:
                file_info = bot.get_file(message.document.file_id)
                downloaded_file = bot.download_file(file_info.file_path)
                src = pt+message.document.file_name
                src = str(src)
                print('User '+str(message.chat.id)+' added the photo')
                with open(src, 'wb') as new_file:
                    new_file.write(downloaded_file)
                bot.reply_to(message,"Document (Photo) added")
                with open('path/imp_'+a+str(message.chat.id), 'wb') as f:
                    pk.dump(src, f)
            except Exception as e:
                bot.reply_to(message,e )

        bot.polling(none_stop=True, interval=1)
    except:
        start_polling()
        print('Trouble Caused!!!')
        
start_polling()

