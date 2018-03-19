
# CheckSum.py
# By: LawlietJH

def GetChecksum(Pin):
	
	Acc = 0									# Se Inicializa Un Acumulador.
	
	if not Pin.isdigit() or not len(Pin) == 7: return 'Error'
	else: Pin = int(Pin)
	
	Pin = Pin * 10							# Se Agrega un Cero, Octavo Digito.
	
	Acc = Acc + 3 * ((Pin//10000000) % 10)	# Extrae El Primer  Digito (De Izq. a Der.), Se Multiplica por 3 y Se Acumula.
	Acc = Acc + 	((Pin//1000000) % 10)	# Extrae El Segundo Digito (De Izq. a Der.) y Se Acumula.
	Acc = Acc + 3 * ((Pin//100000) % 10)	# Extrae El Tercer  Digito (De Izq. a Der.), Se Multiplica por 3 y Se Acumula.
	Acc = Acc + 	((Pin//10000) % 10)		# Extrae El Cuarto  Digito (De Izq. a Der.) y Se Acumula.
	Acc = Acc + 3 * ((Pin//1000) % 10)		# Extrae El Quinto  Digito (De Izq. a Der.), Se Multiplica por 3 y Se Acumula.
	Acc = Acc + 	((Pin//100) % 10)		# Extrae El Sexto   Digito (De Izq. a Der.) y Se Acumula.
	Acc = Acc + 3 * ((Pin//10) % 10)		# Extrae El Septimo Digito (De Izq. a Der.), Se Multiplica por 3 y Se Acumula.
	
	Digito = Acc % 10						# Se Extrae el Ultimo Digito del Valor Acumulado.
	CheckSum = (10 - Digito) % 10			# Se Le Resta al Numero 10 el Digito, Si el Resultado Fuera 10 se toma como 0.
	
	return Pin + CheckSum					# Se Devuelve el PIN ya Completo.

if __name__ == "__main__":
	
	# Ejemplos Para Pruebas:
	
	#	Completo		  PIN     CHECKSUM		Verificación
	#
	#	20128227		2012822		 7			Correcto
	#	09386044		0938604		 4			Correcto
	#	12345670		1234567		 0			Correcto
	#	01234565		0123456		 5			Correcto
	#	12332112		1233211		 2			Incorrecto	(Checksum Correcto: 3)
	
	PIN = GetChecksum('2012822')
	
	print('\n\n PIN:', PIN)
	
