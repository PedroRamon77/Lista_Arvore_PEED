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

    def encontrar_caminho(self, valor):
        return self._encontrar_caminho_recursivo(self.raiz, valor, [])

    def _encontrar_caminho_recursivo(self, no_atual, valor, caminho_atual):
        if no_atual is None:
            return None

        caminho_atual.append(no_atual)

        if no_atual.valor == valor:
            return caminho_atual

        if valor < no_atual.valor:
            caminho_esquerda = self._encontrar_caminho_recursivo(no_atual.esquerda, valor, caminho_atual.copy())
            if caminho_esquerda:
                return caminho_esquerda

        caminho_direita = self._encontrar_caminho_recursivo(no_atual.direito, valor, caminho_atual.copy())
        if caminho_direita:
            return caminho_direita

        return None
