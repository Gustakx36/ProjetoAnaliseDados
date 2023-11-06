from tqdm import tqdm
import time

def gerarValores(listaMisturada, func, testes=10):
    listaTempos = []
    Objeto = func()
    nomeFuncao = '\033[34m' + Objeto.functionName()["nomeFuncao"] + '\033[0;0m'
    try:
        print("\n")
        for i in tqdm(range(testes)):
            listaAtual = listaMisturada.copy()
            inicio = time.time()
            Objeto.function(listaAtual)
            fim = time.time()
            listaTempos.append(Objeto.functionName(inicio, fim)["tempo/s"])
    except RecursionError:
        return {
            'msg' : f"""
    '
    '- - -> {nomeFuncao} : \033[31mErro -> Numero máximo de funções recursivas atingido!\033[0;0m""",
            'tempo' : 0,
            'nome' : nomeFuncao
        }
    except Exception as e:
        return {
            'msg' : f"""
    '
    '- - -> {nomeFuncao} : \033[31mErro -> {e}!\033[0;0m""",
            'tempo' : 0,
            'nome' : nomeFuncao
        }
    return {
        'msg' : f"""
    '
    '- - -> {nomeFuncao} : \033[32mSucesso\033[0;0m -> Tempo Médio : \033[33m{calculaMedia(listaTempos)}s\033[0;0m na reorganização de {len(listaMisturada)} itens - \033[36mForam feitos {testes} testes!\033[0;0m""",
        'tempo' : calculaMedia(listaTempos),
        'nome' : nomeFuncao
    }

def calculaMedia(listaTempos):
    soma = 0
    for item in listaTempos:
        soma += float(item)
    return '%f' % (soma / len(listaTempos))