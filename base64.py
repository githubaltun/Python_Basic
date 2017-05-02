# -*- coding: utf-8 -*-
import base64
import os
import binascii
def ayrac():
	print ' '
	print '----------------------------------------------------------------------'
	print ' '
def ekran():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])
def bilgi():
    print('\033[37m')
    print('\033[37m')
    print('\033[35m' + '   1) ' + '\033[32m' + 'base64 Kriptola')
    print('\033[35m' + '   2) ' + '\033[32m' + 'base64 Kripto Çöz')
    print('\033[37m')
def nick():
	print('\033[37m')
        print('\033[1;7;37m'+'                                                                                ')
	print('\033[1;7;37m'+'                                                                                ')
        print('\033[1;7;37m'+'                                                                                ')
	print('\033[1;7;37m'+'               '+'\033[0;1;34m'+'N	İ	L	Ü	F	E	R'+'\033[1;7;37m'+'               ')
	print('\033[1;7;37m'+'                        '+'\033[0;1;36m'+'Base64 	decode 	-   encode python'+'\033[1;7;37m'+'                       ')
        print('\033[1;7;37m'+'                                                                                ')
        print('\033[1;7;37m'+'                                                                                ')
        print('\033[1;7;37m'+'                                                                                ')
        print('\033[1;7;37m'+' 	 	 	 	 	 	 	 	 	 	 ')
        print('\033[1;7;37m'+'	 	 	 	 	 	 	 	 	 ')
        print('\033[1;7;37m'+'		 	 	 	 	 	 	 ')
        print('\033[1;7;37m'+'			 	 	 	 	 ')
        print('\033[1;7;37m'+'			 	 	 	 	 ')
        print('\033[1;7;37m'+'			 	 	 	 	 ')
        print('\033[1;7;37m'+'			 	 	 	 	 ')
        print('\033[0;37m')
sayac=0
ekran()
nick()
bilgi()
secenek = raw_input('\033[1;7;37m'+' İşlem Numarası : ')
print '\033[0;37m'
if secenek == '1':
    ayrac()
    metin=raw_input("  Şifrelenecek Metin: ")
    ayrac()
    kackez=raw_input("Kaç Kere Şifrelensin: ")
    print " "
    print " "
    b64metin=base64.b64encode(metin)
    sayac=sayac+1
    print "Şifrelenmiş Metin  ",sayac," :  ",b64metin
    print " "
    print " "
    print "-----------------------------------------"
    if (int(kackez)>1):
	for i in range(int(1),int(kackez)):
		sayac=sayac+1
		b64metin=base64.b64encode(b64metin)
		print "Şifrelenmiş Metin  ",sayac," :  ",b64metin
		print " "
		print " "
		print "-----------------------------------------"
		print " "
		print " "
if secenek == '2':
    ayrac()
    metin=raw_input("     Çözülecek Metin: ")
    ayrac()
    kackez=raw_input("Kaç Kere Çözümlensin: ")
    print " "
    print " "
    b64metin=base64.b64decode(metin)
    sayac=sayac+1
    print "Çözülmüş Metin  ",sayac," :  ",b64metin
    print " "
    print " "
    print "-----------------------------------------"
    if (int(kackez)>1):
	for i in range(int(1),int(kackez)):
		sayac=sayac+1
		b64metin=base64.b64decode(b64metin)
		print "Çözülmüş Metin  ",sayac," :  ",b64metin
		print " "
                print " "
		print "-----------------------------------------"
		print " "
		print " "
