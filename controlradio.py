from radio import Radio
Mradio= Radio("Pioner")
DeseaContinuar=True
while DeseaContinuar:
	if Mradio.encendido:
		op=int(input("1.Apagar \n2.Subir/Bajar Volumen \n3.Subir/Bajar Emisora \n4.AM/FM \n"))
		if op==1:
			Mradio.encendido=False	
		if op==4:
			Mradio.en_FM=cambio_emisora(Mradio)
	else:
		opc=int(input("1.Encender \n2.Salir \n"))
		if opc==1:
			Mradio.encendido=True
		else:
			DeseaContinuar=False
print("Bai Bai")
print(Mradio.en_FM)