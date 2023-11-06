class HeapSort:
    def __init__(self):
        pass

    def heap_sort(self, lista, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
    
        if l < n and lista[i] < lista[l]:
            largest = l
    
        if r < n and lista[largest] < lista[r]:
            largest = r
    
        if largest != i:
            (lista[i], lista[largest]) = (lista[largest], lista[i])  # swap
    
            self.heap_sort(lista, n, largest)
    
    def function(self, lista):
        n = len(lista)
    
        for i in range(n // 2 - 1, -1, -1):
            self.heap_sort(lista, n, i)
    
        for i in range(n - 1, 0, -1):
            (lista[i], lista[0]) = (lista[0], lista[i])
            self.heap_sort(lista, i, 0)

    def functionName(self, inicio = 0, fim = 0):
        if inicio - fim == 0:
            return {'tempo/s' : 'Erro', 'nomeFuncao' : 'Heap Sort'}
        return {'tempo/s' : '%f' % (fim - inicio), 'nomeFuncao' : 'Heap Sort'}