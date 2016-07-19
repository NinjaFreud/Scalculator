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

print ("\033[36m\033[1m+----------------------------------+")
print ("| 1. Calcular o valor dos juros    |")
print ("| 2. Calcular o tempo              |")
print ("| 3. Calcular a taxa de juros      |")
print ("| 4. Calcular o montante           |")
print ("| 5. Conversor dia/mês/ano         |")
print ("| 6. Voltar ao menu inicial        |")
print ("| 7. Sair                          |")
print ("+----------------------------------+")

escolha =  input ("")

if (escolha == 1):
	c = input ("\nCapital = ")
	i = input ("\nTaxa de juros [Em %  e em dias] = ")
	t = input ("\nTempo [Em dias] = ")

	j = i / 100 * c *  t

	print ("O valor dos juros é igual a: %f" %j)

if (escolha == 2):
	j = input ("\nJuros = ")
	c = input ("\nCapital = ")
	i = input ("\nTaxa de juros [Em %  e em dias] = ")

	# 200 = 100 * 1 * t

	t1 = i / 100 * c 
	if (j > t1):
		t = j / t1

	if (j < t1):
		t = t1 / j

	print ("O valor numérico do tempo em dias é igual a: %i" %t)

if (escolha == 3):
	j = input ("\nJuros = ")
	c = input ("\nCapital = ")
	t = input ("\nTempo [Em dias] = ")
	i1 = t * c 
	x = j / i1 * 100
	print ("O valor numérico da taxa em dias e em porcentagem é igual a : %f" %x)

if (escolha == 4):
	c = input ("\nCapital = ")
	j = input ("\nJuros = ")

	m = j + c

	print ("O valor do montante é: %f" %m)

if (escolha == 5):
	print ("+-------------------------+")
	escolha1 = input ("| 1. Mês/Dia              |\n| 2. Ano/Dia              |\n| 3. Mês/Ano              |\n| 4. Ano/Mês              |\n| 5. Dia/Ano              |\n| 6. Dia/Mês              |\n+-------------------------+\n")

	if (escolha1 == 1):
		m = input ("Meses = ")
		d = m * 30

		print ("Convertido de %i mês(es) para %i dia(s)" %(m ,d))
		print ("\n+---------------------------------------------+")
		escolha2 = input ("| 1. Voltar ao menu inicial                   |\n| 2. Sair                                     |\n| 3. Voltar para a calculadora de juros       |\n+---------------------------------------------+\n")

		if (escolha2 == 1):
			import os
			os.system("clear")
			os.system("python Scalculator.py")
		if (escolha2 == 2):
			import os
			os.system("clear")
		if (escolha2 == 3):
			import os
			os.system("clear")
			os.system("python Calculadora_de_juros_simples.py")

	if (escolha1 == 2):
		a = input ("Anos = ")
		d = a *360
		
		print ("Convertido de %i ano(s) para %i dia(s)" %(a, d))
		escolha2 = input ("| 1. Voltar ao menu inicial                   |\n| 2. Sair                                     |\n| 3. Voltar para a calculadora de juros       |\n+---------------------------------------------+\n")

		if (escolha2 == 1):
			import os
			os.system("clear")
			os.system("python Scalculator.py")
		if (escolha2 == 2):
			import os
			os.system("clear")
		if (escolha2 == 3):
			import os
			os.system("clear")
			os.system("python Calculadora_de_juros_simples.py")

	if (escolha1 == 3):
		m = input ("Meses = ")
		a = m / 12

		print ("Convertido de %i mês(es) para %i ano(s)" %(m, a))
		escolha2 = input ("| 1. Voltar ao menu inicial                   |\n| 2. Sair                                     |\n| 3. Voltar para a calculadora de juros       |\n+---------------------------------------------+\n")

		if (escolha2 == 1):
			import os
			os.system("clear")
			os.system("python Scalculator.py")
		if (escolha2 == 2):
			import os
			os.system("clear")
		if (escolha2 == 3):
			import os
			os.system("clear")
			os.system("python Calculadora_de_juros_simples.py")

	if (escolha1 == 4):
		a = input ("Anos = ")
		m = a * 12

		print ("Convertido de %i anos para %i mês(es)" %(a, m))
		escolha2 = input ("| 1. Voltar ao menu inicial                   |\n| 2. Sair                                     |\n| 3. Voltar para a calculadora de juros       |\n+---------------------------------------------+\n")

		if (escolha2 == 1):
			import os
			os.system("clear")
			os.system("python Scalculator.py")
		if (escolha2 == 2):
			import os
			os.system("clear")
		if (escolha2 == 3):
			import os
			os.system("clear")
			os.system("python Calculadora_de_juros_simples.py")

	if (escolha1 == 5):
		d = input ("Dias = ")
		a = d / 360

		print ("Converido de %i dia(s) para %i ano(s)" %(d, a))
		escolha2 = input ("| 1. Voltar ao menu inicial                   |\n| 2. Sair                                     |\n| 3. Voltar para a calculadora de juros       |\n+---------------------------------------------+\n")

		if (escolha2 == 1):
			import os
			os.system("clear")
			os.system("python Scalculator.py")
		if (escolha2 == 2):
			import os
			os.system("clear")
		if (escolha2 == 3):
			import os
			os.system("clear")
			os.system("python Calculadora_de_juros_simples.py")

	if (escolha1 == 6):
		d = input ("Dias = ")
		m = d / 30
		print ("Convertido de %i dia(s) para %i mês(es)" %(d, m))
		escolha2 = input ("| 1. Voltar ao menu inicial                   |\n| 2. Sair                                     |\n| 3. Voltar para a calculadora de juros       |\n+---------------------------------------------+\n")

		if (escolha2 == 1):
			import os
			os.system("clear")
			os.system("python Scalculator.py")
		if (escolha2 == 2):
			import os
			os.system("clear")
		if (escolha2 == 3):
			import os
			os.system("clear")
			os.system("python Calculadora_de_juros_simples.py")
if (escolha == 6):
	import os
	os.system ("clear")
	os.system ("python Scalculator.py")

if (escolha == 7):
	import os
	os.system ("clear")