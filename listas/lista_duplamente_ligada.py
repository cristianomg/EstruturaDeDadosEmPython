from .no_duplo import No

class ListaDuplamenteLigada:
	def __init__(self):
		self.__primeiro_no = None
		self.__ultimo_no = None
		self.__tamanho = 0

	@property
	def tamanho(self):
		return self.__tamanho

	def __str__(self):
		no = self.__primeiro_no
		elementos = ''
		for i in range(self.__tamanho):
			elementos = f'{elementos}{no.elemento} '
			no = no.proximo
		return elementos

	def inserir(self, elemento):
		novo_no = No(elemento)
		if self.__primeiro_no == None:
			self.__primeiro_no = novo_no
			self.__ultimo_no = novo_no
		else:
			self.__ultimo_no.proximo = novo_no
			novo_no.anterior = self.__ultimo_no
			self.__ultimo_no = novo_no
		self.__tamanho += 1

	def inserir_elemento_posicao_especifica(self, elemento, posicao):
		if posicao == 0:
			novo_no = No(elemento)
			novo_no.proximo = self.__primeiro_no
			self.__primeiro_no = novo_no
		elif posicao == self.__tamanho:
			novo_no = No(elemento)
			self.__ultimo_no.proximo = novo_no
			novo_no.anterior = self.__ultimo_no
			self.__ultimo_no = novo_no
		else:
			no_atual = self.recuperar_no(posicao)
			no_anterior = no_atual.anterior
			novo_no = No(elemento)
			no_atual.anterior = novo_no
			novo_no.anterior = no_anterior
			novo_no.proximo = no_atual
			no_anterior.proximo = novo_no
		self.__tamanho += 1

	def recuperar_no(self, posicao):
		resultado = 0
		for i in range(posicao + 1):
			if i == 0:
				resultado = self.__primeiro_no
			else:
				resultado = resultado.proximo
		return resultado

	def recuperar_elemento_no(self, posicao):
		no = self.recuperar_no(posicao)
		if no != None:
			return no.elemento
		else:
			return None

	def contem(self, elemento):
		for i in range(self.__tamanho):
			if elemento == self.recuperar_elemento_no(i):
				return True
		return False

	def indice(self, elemento):
		for i in range(self.__tamanho):
			if elemento == self.recuperar_elemento_no(i):
				return i
		return None
	def remover_pos(self, posicao):
		if posicao == 0:
			proximo_no = self.__primeiro_no.proximo
			self.__primeiro_no.proximo = None
			self.__primeiro_no.anterior = None
			self.__primeiro_no = proximo_no
			self.__tamanho -= 1
		elif posicao == (self.__tamanho-1):
			penultimo_no = self.__ultimo_no.anterior
			penultimo_no.proximo = None
			self.__ultimo_no = None
			self.__ultimo_no = penultimo_no
			self.__tamanho -= 1
		elif posicao >= self.__tamanho:
			print('Posição invalida')
		else:
			no_atual = self.recuperar_no(posicao)
			no_anterior = no_atual.anterior
			no_posterior = no_atual.proximo
			no_anterior.proximo = no_posterior
			no_posterior.anterior = no_anterior
			no_atual.proximo = None
			no_atual.anterior = None
			self.__tamanho -= 1

	def remover_elemento(self, elemento):
		if self.indice(elemento) != None:
			self.remover_pos(self.indice(elemento))
		else:
			print('ELemento não existe na lista')
