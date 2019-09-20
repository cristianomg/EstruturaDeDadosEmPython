class Vetor:
	def __init__(self, tamanho):
		self.__tamanho = tamanho
		self.__elementos = [None] * self.__tamanho
		self.__posicao = 0

	@property
	def tamanho(self):
		return len(self.__elementos)

	def contem(self, elemento):
		for i in self.__elementos:
			if elemento == i:
				return True
		return False


	def contem_bin(self,elemento):
		meio = round((len(self.__elementos))/2)
		elementos_organizados = self.__elementos.copy()
		elementos_organizados.sort()
		if elemento == elementos_organizados[meio]:
			return True
		elif elemento < elementos_organizados[meio]:
			for i in elementos_organizados[:meio]:
				if elemento == i:
					return True
			return False
		elif elemento > elementos_organizados[meio]:
			for i in elementos_organizados[meio+1:]:
				if elemento == i:
					return True
			return False

	def indice(self, elemento):
		for index, element in enumerate(self.__elementos):
			if element == elemento:
				return index
		return f"O elemento '{elemento}' não pertence ao vetor"

	def remover_elemento(self, elemento):
		try:
			indice = self.indice(elemento)
			vetor_inicio = self.__elementos[:indice]
			vetor_final = self.__elementos[indice+1:]
			self.__elementos = vetor_inicio+vetor_final
		except:
			print(f'O elemento {elemento} não pertence ao vetor')

	def remover_posicao(self, posicao):
		vetor_inicio = self.__elementos[:posicao]
		vetor_final = self.__elementos[posicao+1:]
		self.__elementos = vetor_inicio+vetor_final


	def inserir_elemento_posicao(self, elemento, posicao):
		try:
			vetor_inicio = self.__elementos[:posicao] + [None]
			vetor_final = self.__elementos[posicao:]
			vetor_inicio[posicao] = elemento
			self.__elementos = vetor_inicio + vetor_final
			self.__posicao +=1
		except:
			print(f"Erro: Posição Invalida o elemento '{elemento}' foi inserido na posicao '{self.__posicao}'")
			self.inserir_elemento_final(elemento)

	def __str__(self):
		return ' '.join([str(i) for i in self.__elementos])

	def inserir_elemento_final(self, elemento):
		if (self.__posicao) < self.tamanho:
			self.__elementos[self.__posicao] = elemento
			self.__posicao += 1
		else:
			self.__elementos = self.__elementos + [elemento]
			self.__posicao += 1

		
	def listar_elemento(self, posicao):
		return self.__elementos[posicao]




