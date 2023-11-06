class ShellSort:
    def __init__(self):
        pass

    def function(self, lista):
        intervalo = len(lista) // 2
        while intervalo > 0:
            for i in range(intervalo, len(lista)):
                temp = lista[i]
                j = i
                while j >= intervalo and lista[j - intervalo] > temp:
                    lista[j] = lista[j - intervalo]
                    j -= intervalo

                lista[j] = temp
            intervalo //= 2

    def functionName(self, inicio = 0, fim = 0):
        if inicio - fim == 0:
            return {'tempo/s' : 'Erro', 'nomeFuncao' : 'Shell Sort'}
        return {'tempo/s' : '%f' % (fim - inicio), 'nomeFuncao' : 'Shell Sort'}    