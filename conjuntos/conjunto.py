from tabela_espalhamento import tabela_espalhamento

class Conjunto:
	def __init__(self, categorias=10):
		self.__elementos = tabela_espalhamento.Tabela_espelhamento(categorias)

	def inserir(self, elemento):
		self.__elementos.inserir(elemento)

	#def inserir_pos(self, elemento, pos):
	#	if self.contem(elemento):
	#		return False
	#	else:
	#		self.__elementos.inserir_elemento_posicao_especifica(elemento, pos)
	#		return True
	
	def __str__(self):
		return self.__elementos.__str__()
	
	def contem(self, elemento):
		return  self.__elementos.contem(elemento)
	
	#def indice(self, elemento):
	#	return self.__elementos.indice(elemento)
	
	def esta_vazio(self, elemento):
		return self.__elementos.tamanho == 0

		
	#def recuperar_elemento_no(self, pos):
	#	return self.__elementos.recuperar_elemento_no(pos)
	
	#def recuperar_no(self, pos):
	#	return self.__elementos.recuperar_no(pos)

	#@property
	#def tamanho(self):
	#	return self.__elementos.tamanho
	
	#def remover_pos(self, pos):
	#	self.__elementos.remover_pos(pos)

	def remover(self, elemento):
		self.__elementos.remover(elemento)
