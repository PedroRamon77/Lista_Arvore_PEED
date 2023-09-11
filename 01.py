class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def __repr__(self):
        return '%s <-- %s --> %s' %(self.esquerda and self.esquerda.valor, self.valor , self.direita and self.direita.valor)
    
