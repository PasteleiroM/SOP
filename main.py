# -*- coding: utf-8 -*-
import random

class Style():
    RED = "\033[31m"
    GREEN = "\033[32m"
    BLUE = "\033[34m"
    RESET = "\033[0m"


def criar_disco(tamanho):
    return [''] * tamanho

def print_disco(disco):
    for i, bloco in enumerate(disco):
        print('%02d: %s' % (i, bloco))
    print(" ")

def adicionar_arquivos_ao_disco(disco, arquivos):
    arquivos_erro = []
    for nome_arquivo, tamanho_arquivo in arquivos:
        indice_inicial = None
        for i in range(len(disco) - tamanho_arquivo + 1):
            if all(bloco == '' for bloco in disco[i:i + tamanho_arquivo]):
                indice_inicial = i
                break
        if indice_inicial is not None:
            for i in range(indice_inicial, indice_inicial + tamanho_arquivo):
                disco[i] = nome_arquivo
        else:
            arquivos_erro.append((nome_arquivo, tamanho_arquivo))
    return arquivos_erro

def remover_arquivos_do_disco(disco, num_arquivos_para_remover):
    arquivos_existentes = list(set(bloco for bloco in disco if bloco != ''))
    arquivos_para_remover = random.sample(arquivos_existentes, num_arquivos_para_remover)
    arquivos_removidos_com_tamanhos = []
    for arquivo in arquivos_para_remover:
        tamanho_arquivo = 0
        for i in range(len(disco)):
            if disco[i] == arquivo:
                disco[i] = ''
                tamanho_arquivo += 1
        arquivos_removidos_com_tamanhos.append((arquivo, tamanho_arquivo))
    return arquivos_removidos_com_tamanhos

# Funcao para realocar arquivos nao alocados
def realocar_arquivos(disco, arquivos_para_alocar):
    novos_arquivos_erro = []
    for nome_arquivo, tamanho_arquivo in arquivos_para_alocar:
        indice_inicial = None
        for i in range(len(disco) - tamanho_arquivo + 1):
            if all(bloco == '' for bloco in disco[i:i + tamanho_arquivo]):
                indice_inicial = i
                break
        if indice_inicial is not None:
            for i in range(indice_inicial, indice_inicial + tamanho_arquivo):
                disco[i] = nome_arquivo
        else:
            novos_arquivos_erro.append((nome_arquivo, tamanho_arquivo))
    return novos_arquivos_erro

# Funcao para desfragmentar o disco
def desfragmentar_disco(disco):
    novo_disco = criar_disco(len(disco))
    indice_atual = 0
    for bloco in disco:
        if bloco != '':
            novo_disco[indice_atual] = bloco
            indice_atual += 1
    return novo_disco

# Funcao principal para executar cada fase
def main():
    # Fase 1
    print(Style.GREEN + "Fase 1: Alocacao inicial de arquivos" + Style.RESET)
    disco = criar_disco(100)
    arquivos = [('Arquivo%d' % i, random.randint(2, 6)) for i in range(1, 31)]
    arquivos_erro = adicionar_arquivos_ao_disco(disco, arquivos)
    print("Disco apos a alocacao inicial:")
    print_disco(disco)
    if arquivos_erro:
        print("Arquivos que nao puderam ser alocados na fase 1:")
        for nome_arquivo, tamanho_arquivo in arquivos_erro:
            arquivos_erro_cor = '%s (%d blocos)' % (nome_arquivo, tamanho_arquivo)
            print(Style.RED + arquivos_erro_cor + Style.RESET)
    else:
        print("Todos os arquivos foram alocados com sucesso na fase 1.")
    print(" ")

    raw_input("Pressione Enter para continuar para a Fase 2...")

    # Fase 2
    print(Style.GREEN + "Fase 2: Remocao de arquivos" + Style.RESET)
    arquivos_removidos_com_tamanhos = remover_arquivos_do_disco(disco, 10)
    print("Disco apos a remocao de arquivos:")
    print_disco(disco)
    print("Arquivos removidos na fase 2:")
    for arquivo, tamanho in arquivos_removidos_com_tamanhos:
        arquivos_removidos_com_tamanhos_cor = '%s (%d blocos)' % (arquivo, tamanho)
        print(Style.BLUE + arquivos_removidos_com_tamanhos_cor + Style.RESET)
    print("")

    raw_input("Pressione Enter para continuar para a Fase 3...")

    # Fase 3.1
    print(Style.GREEN + "Fase 3.1: Realocacao de arquivos nao alocados e removidos" + Style.RESET)
    arquivos_erro = realocar_arquivos(disco, arquivos_erro)
    print("Disco apos tentar realocar arquivos nao alocados na fase 1:")
    print_disco(disco)
    if arquivos_erro:
        print("Arquivos que nao puderam ser alocados na fase 3:")
        for nome_arquivo, tamanho_arquivo in arquivos_erro:
            arquivos_erro_cor = '%s (%d blocos)' % (nome_arquivo, tamanho_arquivo)
            print(Style.RED + arquivos_erro_cor + Style.RESET)
    else:
        print("Todos os arquivos nao alocados na fase 1 foram alocados com sucesso na fase 3.1")
    print("")
    raw_input("Pressione Enter para continuar para a Fase 3.2:")
    
    
    
    # Fase 3.2 - Tentar realocar arquivos removidos na fase 2
    print(Style.GREEN + "Fase 3.2: Realocar arquivos removidos na Fase 2"  + Style.RESET)
    arquivos_removidos_erro = realocar_arquivos(disco, arquivos_removidos_com_tamanhos)
    print("Disco apos tentar realocar arquivos removidos na fase 2:")
    print_disco(disco)
    if arquivos_removidos_erro:
        print("Arquivos removidos que nao puderam ser realocados na fase 3.2:")
        for nome_arquivo, tamanho_arquivo in arquivos_removidos_erro:
            arquivos_removidos_erro_cor = '%s (%d blocos)' % (nome_arquivo, tamanho_arquivo)
            print(Style.RED + arquivos_removidos_erro_cor + Style.RESET)
    else:
        print("Todos os arquivos removidos na fase 2 foram realocados com sucesso na fase 3.2")
    print("")

    raw_input("Pressione Enter para continuar para a Fase 4...")

    # Fase 4.1
    print(Style.GREEN + "Fase 4.1: Desfragmentacao do disco" + Style.RESET)
    disco = desfragmentar_disco(disco)
    print("Disco apos desfragmentacao:")
    print_disco(disco)
    raw_input("Pressione Enter para continuar para a Fase 4.2")

    # Fase 4.2
    print(Style.GREEN + "Fase 4.2: Realocacao de arquivos removidos e restantes da Fase 3." + Style.RESET)
    arquivos_erro = realocar_arquivos(disco, arquivos_erro)
    arquivos_removidos_erro = realocar_arquivos(disco, arquivos_removidos_erro)
    print("Disco apos tentar realocar arquivos restantes da fase 3 e arquivos removidos:")
    print_disco(disco)
    if arquivos_erro or arquivos_removidos_erro:
        print("Arquivos que nao puderam ser alocados apos a desfragmentacao:")
        for nome_arquivo, tamanho_arquivo in arquivos_erro:
            arquivos_erro_cor = '%s (%d blocos)' % (nome_arquivo, tamanho_arquivo)
            print(Style.RED + arquivos_erro_cor + Style.RESET)
        for nome_arquivo, tamanho_arquivo in arquivos_removidos_erro:
            arquivos_removidos_erro_cor = '%s (%d blocos)' % (nome_arquivo, tamanho_arquivo)
            print(Style.RED + arquivos_removidos_erro_cor + Style.RESET)
    else:
        print("Todos os arquivos foram alocados com sucesso apos a desfragmentacao.")
    print("")

if __name__ == '__main__':
    main()
