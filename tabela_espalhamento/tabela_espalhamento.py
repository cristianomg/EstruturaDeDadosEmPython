from listas import lista_ligada


class Tabela_espelhamento:

	def __init__(self, categorias=2):
		self.__elementos = lista_ligada.ListaLigada()
		self.__numero_categorias = categorias
		self.__tamanho = 0
		for i in range(self.__numero_categorias):
			self.__elementos.inserir(lista_ligada.ListaLigada())

	@property
	def tamanho(self):
		return self.__tamanho

	def __gerar_num_espalhamento(self, elemento):
		return hash(elemento) % self.__numero_categorias

	def contem(self, elemento):
		numero_espalhamento = self.__gerar_num_espalhamento(elemento)
		categoria = self.__elementos.recuperar_elemento_no(numero_espalhamento)
		return categoria.contem(elemento)
	

	def inserir(self, elemento):
		if not self.contem(elemento):
			num_espalhamento = self.__gerar_num_espalhamento(elemento)
			categoria = self.__elementos.recuperar_elemento_no(num_espalhamento)
			categoria.inserir(elemento)
			self.__tamanho += 1
			return True
		else:
			return False

	def remover(self, elemento):
			num_espalhamento = self.__gerar_num_espalhamento(elemento)
			categoria = self.__elementos.recuperar_elemento_no(num_espalhamento)
			categoria.remover_elemento(elemento)
			self.__tamanho -= 1

	def __str__(self):
		return self.__elementos.__str__()