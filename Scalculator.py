#coding=UTF-8
#@Copyright 2016 Augusto Sigolo/NinjaFreud
#Este arquivo é parte do programa Scalculator
#
#Scalculator é um software livre; você pode redistribuí-lo e/ou 
#modificá-lo dentro dos termos da Licença Pública Geral GNU como 
#publicada pela Fundação do Software Livre (FSF); na versão 3 da 
#Licença, ou (na sua opinião) qualquer versão.
#
#Este programa é distribuído na esperança de que possa ser  útil, 
#mas SEM NENHUMA GARANTIA; sem uma garantia implícita de ADEQUAÇÃO
#a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a
#Licença Pública Geral GNU para maiores detalhes.
#
#Você deve ter recebido uma cópia da Licença Pública Geral GNU junto
#com este programa, Se não, veja <http://www.gnu.org/licenses/>.






print ("\033[35m\033[1m#############################################################################################################")
print ("##                                                                                                         ##")
print ("##  =======  =======  ========  ==       =======  ==   ==  ==       =======  ========  ========  ========  ##")
print ("##  =======  =======  ========  ==       =======  ==   ==  ==       =======  ========  ========  ========  ##")
print ("##  ==       ==       ==    ==  ==       ==       ==   ==  ==       ==   ==     ==     ==    ==  ==    ==  ##")
print ("##  ==       ==       ==    ==  ==       ==       ==   ==  ==       ==   ==     ==     ==    ==  ==    ==  ##")
print ("##  ==       ==       ==    ==  ==       ==       ==   ==  ==       ==   ==     ==     ==    ==  ========  ##")
print ("##  =======  ==       ========  ==       ==       ==   ==  ==       =======     ==     ==    ==  ========  ##")
print ("##  =======  ==       ========  ==       ==       ==   ==  ==       =======     ==     ==    ==  ==  ==    ##")
print ("##       ==  ==       ==    ==  ==       ==       ==   ==  ==       ==   ==     ==     ==    ==  ==   ==   ##")
print ("##       ==  ==       ==    ==  ==       ==       ==   ==  ==       ==   ==     ==     ==    ==  ==    ==  ##")
print ("##  =======  =======  ==    ==  =======  =======  =======  =======  ==   ==     ==     ========  ==    ==  ##")
print ("##  =======  =======  ==    ==  =======  =======  =======  =======  ==   ==     ==     ========  ==    ==  ##")
print ("##                                                                                                         ##")
print ("#############################################################################################################")
print ("\n\nOpções:")
print ("\033[36m\033[1m+-------------------------------------------------+")
print ("| 1. Menu de Calculadoras                         |")
print ("| 2. Créditos                                     |")
print ("| 3. Tutoriais                                    |")
print ("| 4. Versão                                       |")
print ("| 5. Restart                                      |")
print ("| 0. Sair                                         |")
print ("+-------------------------------------------------+")
escolha1 = input ("Escolha qual opção você deseja:\n")

if (escolha1 ==1):
	print ("Abrindo o menu aguarde [.........]")
	import os
	os.system ("python Menu_calculadoras.py")
if (escolha1 ==2):
	print ("\n\n+----------------------+")
	print ("|Criado por: Sigolo    |")
	print ("| Twitter: @NinjaFreud |")
	print ("| Site: ninjafreud.tk  |")
	print ("+----------------------+\n\n")


	print ("+-------------------------------------------------+")
	print ("| 1. Menu de Calculadoras                         |")
	print ("| 2. Créditos                                     |")
	print ("| 3. Tutoriais                                    |")
	print ("| 4. Versão                                       |")
	print ("| 0. Sair                                         |")
	print ("+-------------------------------------------------+\n\n")
	escolha1 = input ("Escolha qual opção você deseja:")


if (escolha1 ==3):
	print ("\n\n+----------------------------+")
	print ("|ninjafreud.tk/tutoriais.html|")
	print ("+----------------------------+\n\n")

	print ("+-------------------------------------------------+")
	print ("| 1. Menu de Calculadoras                         |")
	print ("| 2. Créditos                                     |")
	print ("| 3. Tutoriais                                    |")
	print ("| 4. Versão                                       |")
	print ("| 0. Sair                                         |")
	print ("+-------------------------------------------------+\n\n")
	escolha1 = input ("Escolha qual opção você deseja:")

if (escolha1 ==4):
	print ("+-------------------------+")
	print ("|Scalculator v0.0.1 Dreams|")
	print ("+-------------------------+")


	print ("+-------------------------------------------------+")
	print ("| 1. Menu de Calculadoras                         |")
	print ("| 2. Créditos                                     |")
	print ("| 3. Tutoriais                                    |")
	print ("| 4. Versão                                       |")
	print ("| 0. Sair                                         |")
	print ("+-------------------------------------------------+\n\n")
	escolha1 = input ("Escolha qual opção você deseja:")

if (escolha1 == 5):
	import os
	os.system("clear")
	os.system("python Scalculator.py")

if (escolha1 == 0):
	import os
	os.system("clear")