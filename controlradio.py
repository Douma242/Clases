from radio import Radio
Mradio= Radio("Pioner")
DeseaContinuar=True
while DeseaContinuar:
	if Mradio.encendido:
		op=int(input("1.Apagar \n2.Subir/Bajar Volumen \n3.Subir/Bajar Emisora \n4.AM/FM \n\n"))
		if op==1:
			Mradio.encendido=False
		if op==2:
			opcvol=int(input("1.subir 2.bajar "))
			if opcvol==1:
				Mradio.subir_volumen()
			else:
				Mradio.bajar_volumen()	
		if op==3:
			opcEsta=int(input("1.subir estacion 2.bajar estacion "))
			if opcEsta==1:
				Mradio.subir_estacion()
			else:
				Mradio.bajar_estacion()
		if op==4:
			Mradio.cambio_emisora()
	else:
		opc=int(input("1.Encender \n2.Salir \n\n"))
		if opc==1:
			Mradio.encendido=True
		else:
			DeseaContinuar=False
print("Bai Bai")
print(Mradio.en_FM)
print(Mradio.volumen)
print(Mradio.emisora)