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
    read = arquivo.readline().rstrip()
    textos.append(read)
    read = arquivo.readline().rstrip()
    textos.append(read)
    read = arquivo.readline().rstrip()
    textos.append(read)
    
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
        p_lower = palavra.lower()
        if p_lower in frequencia:
            if frequencia[p_lower] == 1:
                unicas -= 1
            frequencia[p_lower] += 1
        else:
            frequencia[p_lower] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    frequencia = dict()
    for palavra in lista_palavras:
        p_lower = p_lower.lower()
        if p_lower in frequencia:
            frequencia[p_lower] += 1
        else:
            frequencia[p_lower] = 1

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
    elemento_len = 0
    for elemento in sentenca:
        elemento_len += len(elemento)
    tamanho_med_sentenca = elemento_len / sentenca_len

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
    # Apenas expondo o uso de variáveis globais
    global compara_assinatura
    global assinaturas
    parada = len(assinaturas)
    incremento_lista = 0
    salvar_lista = []
    soma = 0
    while incremento_lista != parada:
        tamanho_med_palavra = compara_assinatura[0] - assinaturas[incremento_lista][0]
        r_typetoken = compara_assinatura[1] - assinaturas[incremento_lista][1]
        hapax_lego = compara_assinatura[2] - assinaturas[incremento_lista][2]
        tamanho_med_sentenca = compara_assinatura[3] - assinaturas[incremento_lista][3]
        complex_senten = compara_assinatura[4] - assinaturas[incremento_lista][4]
        tamanho_med_frase = compara_assinatura[5] - assinaturas[incremento_lista][5]
        soma = tamanho_med_palavra + r_typetoken + hapax_lego + tamanho_med_sentenca + complex_senten
        soma = (soma + tamanho_med_frase) / 6
        salvar_lista.append(soma)
        incremento_lista += 1

    return soma


compara_assinatura, arquivo = le_assinatura()
texto = le_textos(arquivo)
assinaturas = []
for cada in texto:
    assinaturas.append(calcula_assinatura(cada))
resultado = compara_assinatura()


print("O texto com mais chances de ter copiado é (por ordem de digitação)", resultado)

