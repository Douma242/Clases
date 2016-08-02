class Radio():
	def __init__(self, marca):
		self.marca=marca
		self.encendido=False
		self.emisoraFM=87
		self.emisoraAM=300
		self.volumen=0
		self.en_FM=True

	def encender(self):
		self.encendido=True

	def apagar(self):
		self.encendido=False

	def subir_volumen(self):
		if volumen>=100:
			self.volumen=100
		else:
			self.volumen+=5

	def bajar_volumen(self):
		if volumen<=0:
			self.volumen=0
		else:
			self.volumen-=5

	def subir_estacion(self):
		if self.en_FM:
			if self.emisoraFM>107:
				self.emisoraFM=87
			else:
				self.emisoraFM+=0.5
		else:
			if self.emisoraAM>1300:
				self.emisoraAM=300
			else:
				self.emisoraAM+=40
	def cambio_emisora(self):
		if self.en_FM:
			self.en_FM=False
		else:
			self.en_FM=True