class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direito = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no_atual, valor):
        if not no_atual:
            return no_atual
        
        if valor < no_atual.valor:
            no_atual.esquerda = self._remover_recursivo(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            no_atual.direito = self._remover_recursivo(no_atual.direito, valor)
        else:
            if not no_atual.esquerda:
                return no_atual.direito
            elif not no_atual.direito:
                return no_atual.esquerda
            
            no_atual.valor = self._min_valor_no(no_atual.direito).valor
            no_atual.direito = self._remover_recursivo(no_atual.direito, no_atual.valor)

        return no_atual

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda:
            atual = atual.esquerda
        return atual
