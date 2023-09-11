class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direito = None
        
class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if not self.raiz:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._inserir_recursivo(no_atual.esquerda, valor)
        else:
            if no_atual.direito is None:
                no_atual.direito = No(valor)
            else:
                self._inserir_recursivo(no_atual.direito, valor)

    def obter_filhos(no):
        filhos = []
        if no.esquerda:
            filhos.append(no.esquerda)
        if no.direito:
            filhos.append(no.direito)
        return filhos
