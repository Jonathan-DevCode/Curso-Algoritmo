import re


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    arquivo = open('Arrquivo.txt', 'r')
    wal = arquivo.readline().rstrip()
    ttr = arquivo.readline().rstrip()
    hlr = arquivo.readline().rstrip()
    sal = arquivo.readline().rstrip()
    sac = arquivo.readline().rstrip()
    pal = arquivo.readline().rstrip()

    return [wal, ttr, hlr, sal, sac, pal], arquivo


def le_textos(arquivo):
    textos = []
    textoss = arquivo.readline().rstrip()
    textos.append(textoss)
    textoss = arquivo.readline().rstrip()
    textos.append(textoss)
    textoss = arquivo.readline().rstrip()
    textos.append(textoss)
    print(textos)
    return textos


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    elif sentencas[0] == '':
        del sentencas[0]
    return sentencas


def n_palavras_unicas(lista_palavras):
    frequencia = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in frequencia:
            if frequencia[p] == 1:
                unicas -= 1
            frequencia[p] += 1
        else:
            frequencia[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    frequencia = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in frequencia:
            frequencia[p] += 1
        else:
            frequencia[p] = 1

    return len(frequencia)


def calcula_assinatura(texto):
    frases_len = 0
    lista = []
    texto_bruto = texto.split()
    txtbr_len = len(texto_bruto)

    for elemento in texto_bruto:
        frases_len += len(elemento)
    tamanho_med_palavra = frases_len / txtbr_len

    frases = " ".join(texto_bruto)
    frases = frases.lower()
    frases = re.split(r'[,:;]+', frases)
    frases = len(frases)
    frases_len = 0
    for elemento in texto_bruto:
        frases_len += len(elemento)
    tamanho_med_frase = frases_len / frases

    sentenca = " ".join(texto_bruto)
    sentenca = sentenca.lower()
    sentenca = separa_sentencas(sentenca)
    sentenca_len = len(sentenca)
    sentenca_llen = 0
    for elemento in sentenca:
        sentenca_llen += len(elemento)
    tamanho_med_sentenca = sentenca_llen / sentenca_len

    complex_senten = frases / sentenca_len
    r_typetoken = n_palavras_diferentes(texto_bruto) / txtbr_len
    hapax_lego = n_palavras_unicas(texto_bruto) / txtbr_len

    lista.append(tamanho_med_palavra)
    lista.append(r_typetoken)
    lista.append(hapax_lego)
    lista.append(tamanho_med_sentenca)
    lista.append(complex_senten)
    lista.append(tamanho_med_frase)
    return lista


def compara_assinatura():
    global assigncompare
    global lista_assign
    stop = len(lista_assign)
    incl = 0
    savelist = []
    soma = 0
    while incl != stop:
        tamanho_med_palavra = assigncompare[0] - lista_assign[incl][0]
        r_typetoken = assigncompare[1] - lista_assign[incl][1]
        hapax_lego = assigncompare[2] - lista_assign[incl][2]
        tamanho_med_sentenca = assigncompare[3] - lista_assign[incl][3]
        complex_senten = assigncompare[4] - lista_assign[incl][4]
        tamanho_med_frase = assigncompare[5] - lista_assign[incl][5]
        soma = tamanho_med_palavra + r_typetoken + hapax_lego + tamanho_med_sentenca + complex_senten
        soma = (soma + tamanho_med_frase) / 6
        savelist.append(soma)
        incl += 1

    return soma


assigncompare, arq = le_assinatura()
texto = le_textos(arq)
sentenca_n = 0
chave_l = ",:;"
lista_assign = []
lista_final = []
for cada in texto:
    lista_assign.append(calcula_assinatura(cada))
lista_assign = compara_assinatura()


print("O texto com mais chances de ter copiado é (por ordem de digitação)", lista_assign)

