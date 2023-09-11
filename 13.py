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

    def nos_no_nivel(self, nivel):
        if self.raiz is None:
            return []
        resultado = []
        fila = [(self.raiz, 0)]
        
        while fila:
            no_atual, nivel_atual = fila.pop(0)
            
            if nivel_atual == nivel:
                resultado.append(no_atual)
            if nivel_atual > nivel:
                break
            if no_atual.esquerda:
                fila.append((no_atual.esquerda, nivel_atual + 1))
            if no_atual.direito:
                fila.append((no_atual.direito, nivel_atual + 1))
        return resultado