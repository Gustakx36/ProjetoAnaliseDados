from tqdm import tqdm
import re

def leituraObj(arquivo):
    with open(arquivo, 'r', errors='replace') as ficheiro:
        read = ficheiro.readlines()
        if len(read) > 0:
            colunas = read.pop(0).split(',')
            linhas = []
            with tqdm(total=len(read)) as progress:
                for linha in read:
                    linhas.append(linha)
                    progress.update(0.5)
                dataObj = []
                for linha in linhas:
                    progress.update(0.5)
                    obj = {}
                    indice = 0
                    linha = separaString(linha)
                    for data in linha.split(','):
                        obj[colunas[indice].replace('\n', '')] = data.replace('-virgula-', ', ').replace('\n', '')
                        indice += 1
                    dataObj.append(obj)
                return dataObj
            
def separaString(string):
    padrao = re.findall('\"(.*?)\"', string)
    for  item in padrao:
        novoItem = item.replace(',', '-virgula-')
        string = string.replace(item, novoItem)
    return string


