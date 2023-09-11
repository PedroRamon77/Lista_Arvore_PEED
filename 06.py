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
                
    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia!') 
        else:
            self.mostrar_pre_ordem_recursiva(self.raiz)
        
    def mostrar_pre_ordem_recursiva(self,no):
        print(no.valor, end=' ')
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursiva(no.esquerda)
        if no.direita  is not None:
            self.mostrar_pre_ordem_recursiva(no.direita)
    