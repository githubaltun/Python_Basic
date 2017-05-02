#-*- coding: utf-8 -*-
import subprocess
print ''
print ''
print '		--------------------------------------------------'
print '		|N	İ	L	Ü	F	E	R|'
print '		--------------------------------------------------'
print ''
print ''
sonuc=subprocess.check_output("ifconfig| grep 'inet'|grep 'broad'| cut -d ' ' -f10",shell=True)
print ''
print ''
islem=str(raw_input("	'ifconfig' için 1 ! - Çıkış için '0':  "))
if (islem==str(1)):
	print ''
	print ''
	print ''
	print '		',sonuc
	print ''	
	print ''	
	print ''	
	print '-------------------------------------------------------'
	print ''
	print ''
	print ''
