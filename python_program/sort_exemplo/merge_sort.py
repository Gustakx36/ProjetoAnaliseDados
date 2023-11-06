class MergeSort:
    def __init__(self):
        pass

    def function(self, lista):
        if len(lista)>1:
            meio = len(lista)//2
            meioEsquerdo = lista[:meio]
            meioDireito = lista[meio:]

            self.function(meioEsquerdo)
            self.function(meioDireito)

            i=0
            j=0
            k=0
            while i < len(meioEsquerdo) and j < len(meioDireito):
                if meioEsquerdo[i] < meioDireito[j]:
                    lista[k]=meioEsquerdo[i]
                    i=i+1
                else:
                    lista[k]=meioDireito[j]
                    j=j+1
                k=k+1

            while i < len(meioEsquerdo):
                lista[k]=meioEsquerdo[i]
                i=i+1
                k=k+1

            while j < len(meioDireito):
                lista[k]=meioDireito[j]
                j=j+1
                k=k+1 

    def functionName(self, inicio = 0, fim = 0):
        if inicio - fim == 0:
            return {'tempo/s' : 'Erro', 'nomeFuncao' : 'Merge Sort'}
        return {'tempo/s' : '%f' % (fim - inicio), 'nomeFuncao' : 'Merge Sort'}