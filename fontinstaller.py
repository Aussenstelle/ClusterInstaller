import os
import sys

print('FontLoader initalisiert... Bitte warten...')
if sys.platform == 'linux' or platform == 'linux2':
    print('Linux erkannt.')
else:
    if sys.platform == 'darwin':
        betriebssystem = 'Mac OS'
    if sys.platform == 'win32':
        betriebssystem = 'Windows'
    print('Dieser installer funktioniert nur auf Ubuntu. Auf ' + betriebssystem + 'Funktioniert dieses Programm nicht. Exiting...')
    sys.exit(0)
# Standart Benutzer
benutzer = 'administrator'
# Gebe den Pfad wohin die Schriften kopiert werden sollen
Schriften_pfad = '/usr/share/fonts/truetype/'
try:
    d = open('r', 'config.txt')
except:
    print('Failed to read config.txt')
    sys.exit(0)
path = d.readline()
while True:
        link = d.readline()
        if link == '':
            break
        befehl = 'wget -O' + path + ' ' + link
        os.system(befehl)
        os.system('unzip ' + path)
        os.system('cp /home/administrator/schriften/fuellerschrift/BlackSignature_PERSONAL_USE_ONLY.otf /usr/share/fonts/truetype/')
