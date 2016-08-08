class Radio():
	def __init__(self, marca):
		self.marca=marca
		self.encendido=False
		self.volumen=0
		self.emisora=0
		self.en_FM=True
		if self.en_FM:
			self.emisora=87
		else:
			self.emisora=300

	def encender(self):
		self.encendido=True

	def apagar(self):
		self.encendido=False

	def subir_volumen(self):
		if self.volumen>=100:
			self.volumen=100
		else:
			self.volumen+=5

	def bajar_volumen(self):
		if self.volumen<=0:
			self.volumen=0
		else:
			self.volumen-=5

	def subir_estacion(self):
		if self.en_FM:
			if self.emisora>107:
				self.emisora=87
			else:
				self.emisora+=0.5
		else:
			if self.emisora>1300:
				self.emisora=300
			else:
				self.emisoraAM+=40

	def bajar_estacion(self):
		if self.en_FM:
			if self.emisora<87.0:
				self.emisora=107
			else:
				self.emisora-=0.5
		else:
			if self.emisora<300.0:
				self.emisora=1300
			else:
				self.emisoraAM-=40

	def cambio_emisora(self):
		if self.en_FM:
			self.en_FM=False
		else:
			self.en_FM=True