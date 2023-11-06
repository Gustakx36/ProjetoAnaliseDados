class QuickSort:
    def __init__(self):
        pass

    def function(self, lista):
        tamanho_da_lista = len(lista)
        if tamanho_da_lista > 0:
            self.quick_sort(lista, 0, tamanho_da_lista - 1)
    
    def quick_sort(self, lista, inicio, fim):
        if len(lista) < 0:
            return
        if inicio > fim:
            return
        anterior = inicio
        posterior = fim
        pivo = lista[inicio]

        while anterior < posterior:
            while anterior < posterior and lista[posterior] > pivo:
                posterior = posterior - 1

            if anterior < posterior:
                lista[anterior] = lista[posterior]
                anterior = anterior + 1

            while anterior < posterior and lista[anterior] <= pivo:
                anterior = anterior + 1

            if anterior < posterior:
                lista[posterior] = lista[anterior]
                posterior = posterior - 1

            lista[anterior] = pivo

        self.quick_sort(lista, inicio, anterior - 1)
        self.quick_sort(lista, anterior + 1, fim)

    def functionName(self, inicio = 0, fim = 0):
        if inicio - fim == 0:
            return {'tempo/s' : 'Erro', 'nomeFuncao' : 'Quick Sort'}
        return {'tempo/s' : '%f' % (fim - inicio), 'nomeFuncao' : 'Quick Sort'}