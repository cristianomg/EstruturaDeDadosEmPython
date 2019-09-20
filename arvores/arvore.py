from .no_arvore_inteiro import NoArvoreInteiro
class Arvore:
	def __init__(self, raiz=None):
		self.__raiz = raiz

	@property
	def raiz(self):
		return self.__raiz

	def inserir_elemento(self, no):
		no.no_direito = None
		no.no_esquerdo = None
		if self.__raiz is None:
			self.__raiz = no
		else:
			self.__inserir(no, self.raiz)

	def __inserir(self, no, referencia):
		if (referencia.peso() > no.peso()):
			if referencia.no_esquerdo == None:
				referencia.no_esquerdo = no
			else:
				self.__inserir(no, referencia.no_esquerdo)
		else:
			if referencia.no_direito == None:
				referencia.no_direito = no
			else:
				self.__inserir(no, referencia.no_esquerdo)