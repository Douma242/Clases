from radio import Radio
Mradio= Radio("Pioner")
DeseaContinuar=True
while DeseaContinuar:
	if Mradio.encendido:
		op=int(input("1.Apagar \n2.Subir/Bajar Volumen \n3.Subir/Bajar Emisora \n4.AM/FM \n"))
		if op==1:
			Mradio.encendido=False	
	else:
		opc=int(input("1.Encender \n2.Salir \n"))
		if opc==1:
			Mradio.encendido=True
		else:
			DeseaContinuar=False
print("Bai Bai")