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

print ("Menu de Calculadoras\n\n")
print ("\033[36m\033[1m+----------------------------------+")
print ("| 1. Calculadora de porcentagens   |")
print ("| 2. Calculadora de juros simples  |")
print ("|                                  |")
print ("|                                  |")
print ("|                                  |")
print ("+----------------------------------+")

escolha2 = input ("\n\nEscolha qual calculadora deseja usar:")

if (escolha2 == 1):
	import os
	os.system ("clear")
	os.system ("python Calculadora_de_porcentagem.py")

if (escolha2 == 2):
	import os
	os.system ("clear")
	os.system ("python Calculadora_de_juros_simples.py")
