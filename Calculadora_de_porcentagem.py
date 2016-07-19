#coding=UTF-8
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




#Apresentacao
print ("\033[36m\033[1m+---------------------------+")
print ("|                           |")
print ("|          Porcentagem      |")
print ("|                           |")
print ("+---------------------------+\n\n\n\n\n")

print ("+---------------------------+")
print ("|            Uso            |")
print ("|                           |")
print ("|                           |")
print ("|                           |")
print ("+---------------------------+")
print ("|   w        =           x% |")
print ("|                           |")
print ("|   y        =          100%|")
print ("+---------------------------+\n\n")

#=================================================================
print ("Opções:\n")
print ("+---------------------------+")
escolha =  input ("| 0. Calcular o valor de w  | \n| 1. Calcular o valor de y  | \n| 2. Calcular o valor de x  |\n| 3. Voltar ao menu inicial |\n+---------------------------+\n")
#Achar o valor da equivalente a porcentagem
if (escolha == 0):
#Recebe valores de variaveis
	y = input ("\ny = ")
	float (y)

	x = input ("\nx = ")
	float (x)

	resultadoMultiplicacao1 = 1 * 100
	float (resultadoMultiplicacao1)

	resultadoMultiplicacao2 = y * x
	float (resultadoMultiplicacao2)
	#==================================================================

	#Apresenta Dados
	print ("%f * %f = %f" %(y, x, resultadoMultiplicacao2))
	print ("x * 100 = %fx" %(resultadoMultiplicacao1))

	#===================================================================

	#Contas Finais
	w = resultadoMultiplicacao2 / resultadoMultiplicacao1

	#===================================================================

	#Apresenta Resultados
	print("O resultado do valor numérico de w é: %f " %w)
	print ("\n\n+-------------------------------+")
	escolha2 = input ("| 0. Sair                       |\n| 1. Voltar ao menu principal   |\n+-------------------------------+\n")

	if (escolha2 == 0):
		import os
		os.system("clear")

	if (escolha2 == 1):
		import os
		os.system("clear")
		os.system("python Scalculator.py")

#Equivalente a 100%
if (escolha == 1):
	#Recebe valores de variaveis

	x = input ("\nx =  ")
	float (x)

	w = input ("\nw =  ")
	float (w)

	resultadoMultiplicacao1 = w * 100
	float (resultadoMultiplicacao1)

	resultadoMultiplicacao2 = 1 * x
	float (resultadoMultiplicacao2)
	#==================================================================

	#Apresenta Dados
	print ("w * %f = %fx" %(x, resultadoMultiplicacao2))
	print ("%f * 100 = %f" %(w, resultadoMultiplicacao1))

	#===================================================================

	#Contas Finais
	y = resultadoMultiplicacao1 / resultadoMultiplicacao2

	#===================================================================

	#Apresenta Resultados
	print("O resultado do valor numérico de y é:: %f " %y)
	print ("\n\n+-------------------------------+")
	escolha2 = input ("| 0. Sair                       |\n| 1. Voltar ao menu principal   |\n+-------------------------------+\n")

	if (escolha2 == 0):
		import os
		os.system("clear")

	if (escolha2 == 1):
		import os
		os.system("clear")
		os.system("python Scalculator.py")
#Valor da porcentagem equivalente a x
if (escolha == 2):
	#Recebe valores de variaveis
	y = input ("\ny =  ")
	float (y)

	w = input ("\nw =  ")
	float (w)

	resultadoMultiplicacao1 = w * 100
	float (resultadoMultiplicacao1)

	resultadoMultiplicacao2 = y * 1
	float (resultadoMultiplicacao2)
	#==================================================================

	#Apresenta Dados
	print ("%f * x = %fx" %(y, resultadoMultiplicacao2))
	print ("%f * 100 = %f" %(w, resultadoMultiplicacao1))

	#===================================================================

	#Contas Finais
	x = resultadoMultiplicacao1 / resultadoMultiplicacao2

	#===================================================================

	#Apresenta Resultados
	print("O resultado do valor numérico de x é: %f " %x)
	print ("\n\n+-------------------------------+")
	escolha2 = input ("| 0. Sair                       |\n| 1. Voltar ao menu principal   |\n+-------------------------------+\n")

	if (escolha2 == 0):
		import os
		os.system("clear")

	if (escolha2 == 1):
		import os
		os.system("clear")
		os.system("python Scalculator.py")

if (escolha == 3):
	import os 
	os.system("python Scalculator.py")