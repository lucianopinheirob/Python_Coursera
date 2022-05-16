import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def módulo(n):
    if n>=0:
        return n
    if n<0:
        return -n

def soma_elementos(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma


def compara_assinatura(as_a, as_b):
#Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.
    similaridade = []
    for i in range(len(as_a)):
        simi = as_a[i] - as_b[i]
        similaridade.append(simi)
    for i in range(len(similaridade)):
        similaridade[i] = módulo(similaridade[i])
    soma = soma_elementos(similaridade)
    grau_similaridade = soma/6
    return grau_similaridade

def tamanho_medio_palavras(lis_palavra):
    tamanho = 0
    for palavra in lis_palavra:
        tamanho = tamanho + len(palavra)
    tamanho_medio = tamanho/len(lis_palavra)
    return tamanho_medio

def tamanho_medio_sentencas(lis_sentenca):
    tamanho = 0
    for sentenca in lis_sentenca:
        tamanho = tamanho + len(sentenca)
    tamanho_medio = tamanho/len(lis_sentenca)
    return tamanho_medio

def tamanho_medio_sentencas(lis_frase):
    tamanho = 0
    for frase in lis_frase:
        tamanho = tamanho + len(frase)
    tamanho_medio = tamanho/len(lis_frase)
    return tamanho_medio

def calcula_assinatura(texto):
#Essa funcao recebe um texto e deve devolver a assinatura do texto.
    i = 0
    j = 0
    frases = []
    palavras = []
    sentencas = separa_sentencas(texto)
    while i < len(sentencas):
        frases = frases + separa_frases(sentencas[i])
        i = i+1
    while j < len(frases):
        palavras = palavras + separa_palavras(frases[j])
        j = j+1
#Calcular temanho médio de palavras
    wal = tamanho_medio_palavras(palavras)
#Calcular relação type token
    ttr = n_palavras_diferentes(palavras)/len(palavras)
#Calcular Razão Hapax Legomana
    hlr = n_palavras_unicas(palavras)/len(palavras)
#Calcular tamanho médio da sentença
    sal = tamanho_medio_sentencas(sentencas)
#Calcular complexidade de sentença
    sac = len(frases)/len(sentencas)
#Calcular tamanho médio de frase
    pal = tamanho_medio_sentencas(frases)
#Retorna a assinatura do texto
    return ([wal, ttr, hlr, sal, sac, pal])
    

def avalia_textos(textos, ass_cp):
#Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
#Criar lista de assinaturas
    assinaturas = []
    for i in range(len(textos)):
        assinatura = calcula_assinatura(textos[i])
        assinaturas.append(assinatura)
#Calcular e criar vetor grau de similaridade para a assinatura de cada texto.
    lista_grau = []
    for i in range(len(assinaturas)):
        grau = compara_assinatura(ass_cp, assinaturas[i])
        lista_grau.append(grau)
#Calcular a posição do menor grau de similaridade
    min = lista_grau[0]
    for i in range(len(lista_grau)):
        if lista_grau[i] <= min:
            min = lista_grau[i]
            pos_min = i
#Retornar o texto mais similar, com base em sua posição no vetor grau de similaridade
    return pos_min+1

ass_cp = le_assinatura()
textos = le_textos()
avalia_textos(textos, ass_cp)
print("\n O autor do texto", avalia_textos(textos, ass_cp), "está infectado com COH-PIAH")
    


