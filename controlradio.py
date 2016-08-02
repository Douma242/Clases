from radio import Radio
Mradio= Radio("Pioner")
while Radio.encendido==False:	
	opc1= input("1.Encender\n 2.Salir")
	if opc1==2:
		Radio.encendido="n"
	else:
		Radio.encendido=True
		while Radio.encendido:
			opc2=input("1.subir volumen 2.bajar volumen\n3. ")

