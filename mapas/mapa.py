from .associacao import Associacao
from listas import lista_ligada

class Mapa:
	def __init__(self):
		self.__elementos = lista_ligada.ListaLigada()
		self.__numero_categorias = 10
		
		for i in range(self.__numero_categorias):
			self.__elementos.inserir(lista_ligada.ListaLigada())
	
	def gerar_numero_espalhamento(self, chave):
		return hash(chave) % self.__numero_categorias
	
	def contem_chave(self, chave):
		num_espalhamento = self.gerar_numero_espalhamento(chave)
		categoria = self.__elementos.recuperar_elemento_no(num_espalhamento)

		for i in range(categoria.tamanho):
			associacao = categoria.recuperar_elemento_no(i)
			if associacao.chave == chave:
				return True
		return False

	def remover(self, chave):
		numero_espalhamento = self.gerar_numero_espalhamento(chave)
		categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)

		for i in range(categoria.tamanho):
			associacao = categoria.recuperar_elemento_no(i)
			if associacao.chave == chave:
				categoria.remover_elemento(associacao)
				return True
		return False
	def adicionar(self, chave, valor):
		if self.contem_chave(chave):
			self.remover(chave)
		num_espalhamento = self.gerar_numero_espalhamento(chave)
		categoria = self.__elementos.recuperar_elemento_no(num_espalhamento)
		associacao = Associacao(chave, valor)
		categoria.inserir(associacao)

	def recuperar(self, chave):
		num_espalhamento = self.gerar_numero_espalhamento(chave)
		categoria = self.__elementos.recuperar_elemento_no(num_espalhamento)
		for i in range(categoria.tamanho):
			associacao = categoria.recuperar_elemento_no(i)
			if associacao.chave == chave:
				return associacao.valor
		return False

	def __str__(self):
		return self.__elementos.__str__()