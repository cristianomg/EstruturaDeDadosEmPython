from abc import ABC, abstractmethod

class NoArvore(ABC):

	def __init__(self, valor, no_esquerdo=None, no_direito=None):
		self.__valor = valor
		self.__no_esquerdo = no_esquerdo
		self.__no_direito = no_direito

	@property
	def valor(self):
		return self.__valor
	
	@property
	def no_esquerdo(self):
		return self.no_esquerdo
	
	@property
	def no_direito(self):
		return self.no_direito

	@no_esquerdo.setter
	def no_esquerdo(self, no_esquerdo):
		self.no_esquerdo = no_esquerdo

	@no_direito.setter
	def no_direito(self, no_direito):
		self.no_direito = no_direito
		
	@abstractmethod
	def peso(self):
		pass
