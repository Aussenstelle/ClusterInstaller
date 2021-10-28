import os
import sys

print('FontLoader initalisiert...')
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
    d = open('/home/administrator/config.txt', 'r')	
except:
    print('Failed to read config.txt')
    sys.exit(0)
path = d.readline()
if path.endswith('\n'):
            path = path[:-1]
print(']' + path + '[')

while True:
        link = d.readline()
        if link == '':
            break
        if link.endswith('\n'):
            link = link[:-1]
        print('Holen von: ' + link + ' nach ' + path)
        befehl = 'wget -O ' + path + 'schrift.zip' + ' ' + link
        print(befehl)
        os.system(befehl)
        if link.find('/'):
            print(link[-4:])
            if link.endswith('.zip'):
                print('Entpacken von: ' + link.rsplit('/', 1)[1])
                os.system('unzip ' + path + 'schrift.zip')
            else:
                print('Fehler')
        else:
            print('Fehler')
            if path.endswith('.zip'):
                print('Entpacken von: ' + link.rsplit('/', 1)[1])
                os.system('unzip ' + path)
            print('Wird entpackt:' + link)
print('Fertig')
#        os.system('cp /home/administrator/schriften/fuellerschrift/BlackSignature_PERSONAL_USE_ONLY.otf /usr/share/fonts/truetype/')
                
