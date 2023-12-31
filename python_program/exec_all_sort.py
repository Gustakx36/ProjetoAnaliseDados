from sort_exemplo.merge_sort import MergeSort as mg
from sort_exemplo.shell_sort import ShellSort as ss
from sort_exemplo.heap_sort import HeapSort as hs
from gerar_media import gerarValores as media
from arquivo_read import leituraObj as read
from tqdm import tqdm
import time
import sys
import re

# Arquivos que foram feitos testes na máquina local

# 'Teste1' -> Pouco menos de 50 itens
# ['Total_emissions']

# 'Teste2' -> Pouco menos de 1.000 itens
# ['ValueNumeric']

# 'Teste3' -> Mais de 400.000 itens
# ['so2','no2']

# 'Teste4' -> Mais de 1.000.000 de itens
# ['relativehumidity_2m']

# 'Teste5' -> Mais de 3.500.000 de itens
# ['Average value']



# ---------------------------------------------------------------------
# 'arquivo_exemplo' -> Exemplo de 4 itens
# ['coluna_2']

#Variaveis Globais:
arquivo = 'Teste5' # nome do arquivo
coluna = 'Average value' # Coluna que vai ser retirada a lista para o sort
vezes = 2 #quantidade de vezes
# ---------------------------------------------------------------------



def msgDesempenho(objeto):
    keyObj = objeto.keys()
    sortedObj = {}
    for item in keyObj:
        if float(objeto[item]) > 0:
            sortedObj[objeto[item]] = f"{item}(\033[33m{objeto[item]}\033[0;0m)"
    listResult = list(sortedObj.keys())
    merge = mg()
    merge.function(listResult)
    return f"{sortedObj[listResult[0]]} < {sortedObj[listResult[1]]} < {sortedObj[listResult[2]]}"

if __name__ == '__main__':
    print('\n')
    listaTotal = []
    try:
        for item in read('./base_dados/'+arquivo+'.csv'):
            if re.match('[0-9]+', item[coluna]):
                listaTotal.append(item[coluna])
        print("""
    '
    '- - -> \033[32mArquivo lido com sucesso!\033[0;0m""")
    except KeyError:
        print("""
    '
    '- - -> \033[31mA coluna indicada não existe!\033[0;0m""")
        sys.exit()
    
    print("\n")

    # [mg, hs, ss]
    listaFuncoes = [hs, mg, ss]
    listaMisturada = listaTotal.copy()
    objetoTempoMedio = {}
    inicio = time.time()
    for func in listaFuncoes:
        resp = media(listaMisturada, func, vezes)
        print(resp['msg'])
        objetoTempoMedio[resp['nome']] = resp['tempo']
    print("\n")
    fim = time.time()
    print(f"\033[0;0m -> ({msgDesempenho(objetoTempoMedio)})\n\n")