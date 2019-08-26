#/usr/bin/python
# -*- coding: utf-8 -*-
#Copyright 2019 ssh-priv 
#Written by: Adrian Guillermo
#Facebook: Adrian Guillero
#Github: https://www.github.com/AdrMXR

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

import os
import time
from sys import exit
from distutils.dir_util import copy_tree
import webbrowser 
from getch import pause



os.system('clear')


print ('''

         ██████╗ ███████╗███╗   ██╗    ███████╗███████╗██╗  ██╗    
	██╔════╝ ██╔════╝████╗  ██║    ██╔════╝██╔════╝██║  ██║    
	██║  ███╗█████╗  ██╔██╗ ██║    ███████╗███████╗███████║    
	██║   ██║██╔══╝  ██║╚██╗██║    ╚════██║╚════██║██╔══██║    
	╚██████╔╝███████╗██║ ╚████║    ███████║███████║██║  ██║    
 	 ╚═════╝ ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚══════╝╚═╝  ╚═╝  ''').format(WHITE)
print '{}------------------------------------------------------'.format(WHITE).center(77)
print '{}GENERADOR DE SERVIDORES SSH'.format(RED).center(76)
print '{0}Creado por: {3}Adrian Guillermo {2}({1}AdrMXR{2}) {0}Version: {3}1.0{2}{3}'.format(YELLOW, RED, YELLOW, BLUE).center(117)
print '{}------------------------------------------------------'.format(WHITE).center(77)


def private():
	
	print("Instalando requerimientos...")
	time.sleep(4)
	os.system('sudo apt-get install openssh-server')
	time.sleep(2)
	os.system('service ssh stop')
	user = raw_input("Ingrese un nombre de usuario: ")
	os.system('adduser {}'.format(user))
	time.sleep(3)
	print("Configurando usuario en servidor ssh...")
	time.sleep(3)
	directory = os.getcwd()
	os.system('echo AllowUsers {0} >> {1}/sshd_config'.format(user, directory))
	port = input("Digite el puerto que desea configurar (default 22): ")	
	
	if port == 22:
		print("Configurando puerto por default...")
		time.sleep(2)
		os.system('echo Port 22 >> {0}/sshd_config && cp {0}/sshd_config /etc/ssh/sshd_config'.format(directory))
		print("Poniendo en marcha servidor ssh...")
		time.sleep(3)
		os.system("service ssh start")

		if raw_input("¿Desea acceder a su servidor ssh? (y/n)\n--> ").upper() != "Y":
			print("GRACIAS POR UTILIZAR GEN SSH.")
		os.system('ssh -p {0} {1}@localhost'.format(port, user))
		exit(0)

	print("Configurando puerto...")
	time.sleep(3)
	os.system('echo Port {0} >> {1}/sshd_config'.format(port, directory))
	print("Espere un momento...")
	time.sleep(3)
	os.system('cp {}/sshd_config /etc/ssh/sshd_config'.format(directory))
	print("Poniendo en marcha servidor ssh...")
	time.sleep(4)
	os.system('service ssh start')

	if raw_input("¿Desea acceder a su servidor ssh? (y/n)\n--> ").upper() != "Y":
		print("GRACIAS POR UTILIZAR GEN SSH.")
		exit(0)
	os.system('ssh -p {0} {1}@localhost'.format(port, user))


def public():
	if raw_input("¿Ya cuenta con un servidor ssh local existente? (y/n)\n--> ").upper() != "Y":
		print("Creando servidor ssh local...")
		time.sleep(3)
		private()
	
	servidor = raw_input("Introduzca su gateway(puerta de enlace predeterminada de su router) \n--> ")
	time.sleep(3)
	print ("\nA continuacion se abrira la puerta de enlace de su router, configure los puertos correspondientes.")
	time.sleep(4)
	webbrowser.open("http://{}".format(servidor))
	time.sleep(3)
	pause("Una vez terminado, presione una tecla para continuar...")
	os.system('service ssh restart')
	print("Tu servidor ssh publico deberìa de estar listo.\nRecuerda que para accesar debes hacerlo desde otra red diferente a la tuya.")
	time.sleep(3)
	print("\nGRACIAS POR UTILIZAR GEN SSH.")
	exit(0)


def menu():
	option = input("¿Que tipo de servidor ssh desea? \n\n #1 --- Local \n\n #2 --- Publico \n\n--> ")
	if option == 1:
		private()
	elif option == 2:
		public()
	else:
		os.system('clear')
		return menu()

menu()
