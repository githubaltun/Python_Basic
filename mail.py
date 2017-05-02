# -*- coding: utf-8 -*-
import requests
import smtplib
import os

def ekran():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
ekran()
islem=raw_input("Mail Gönderilsin mi? (e/h) :   ")
if islem=="e":
	try:
            gonderici = '*******@gmail.com'
            alici = 'alıcı adresini giriniz'
            mesaj = "'Subject: Neden: junk mail ? \n\n Bla Bla Bla Bla "
            username = '**********@gmail.com'
            password = '**********'
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.login(username, password)
            server.sendmail(gonderici, alici, mesaj)
            server.quit()
            print "Mail gönderildi"
        except:
            print "Mail gönderilemedi"
else:
	print " Hayır seçildi İşlem iptal edildi. "
