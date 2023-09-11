class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direito = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor, self.raiz)

    def _inserir_recursivo(self, valor, no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no.esquerda)
        else:
            if no.direito is None:
                no.direito = No(valor)
            else:
                self._inserir_recursivo(valor, no.direito)

    def arvore_binaria_de_busca(self):
        return self._is_bst_recursivo(self.raiz, float('-inf'), float('inf'))

    def _arvore_binaria_de_busca_recursivo(self, no, minimo, maximo):
        if no is None:
            return True
        
        if not minimo < no.valor < maximo:
            return False

        return (self._arvore_binaria_de_busca_recursivo(no.esquerda, minimo, no.valor) and
                self._arvore_binaria_de_busca_recursivo(no.direito, no.valor, maximo))

