class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        return '%s <-- %s --> %s' %(self.esquerda and self.esquerda.valor, self.valor , self.direita and self.direita.valor)
    
class arvoreBinaria:
    def __init__(self):
        self.raiz = None
    
    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_recursivo(valor,self.raiz)
    
    def _inserir_recursivo(self,valor,no):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_recursivo(valor, no.esquerda)
        else:
            if no.direita is None:
                no.direita = No(valor)        
            else:
                self._inserir_recursivo(valor, no.direita)
                
    def valor_maximo(self):
        return self._valor_maximo_recursivo(self.raiz)

    def _valor_maximo_recursivo(self, no):
        if no is None:
            return float('-inf')

        valor_max_esquerdo = self._valor_maximo_recursivo(no.esquerda)
        valor_max_direito = self._valor_maximo_recursivo(no.direito)
        
        return max(no.valor, valor_max_esquerdo, valor_max_direito)