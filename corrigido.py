# -*- coding: utf-8 -*-
import random

# Função para criar o disco
def create_disk(size):
    return [''] * size

# Função para imprimir o disco
def print_disk(disk):
    for i, block in enumerate(disk):
        print('%02d: %s' % (i, block))
    print()

# Função para adicionar arquivos ao disco
def add_files_to_disk(disk, files):
    failed_files = []
    for file_name, file_size in files:
        start_index = None
        for i in range(len(disk) - file_size + 1):
            if all(block == '' for block in disk[i:i + file_size]):
                start_index = i
                break
        if start_index is not None:
            for i in range(start_index, start_index + file_size):
                disk[i] = file_name
        else:
            failed_files.append((file_name, file_size))
    return failed_files

# Função para remover arquivos aleatórios do disco
def remove_files_from_disk(disk, num_files_to_remove):
    existing_files = list(set(block for block in disk if block != ''))
    files_to_remove = random.sample(existing_files, num_files_to_remove)
    removed_files_with_sizes = []
    for file in files_to_remove:
        file_size = 0
        for i in range(len(disk)):
            if disk[i] == file:
                disk[i] = ''
                file_size += 1
        removed_files_with_sizes.append((file, file_size))
    return removed_files_with_sizes

# Função para realocar arquivos não alocados
def reallocate_files(disk, files_to_allocate):
    new_failed_files = []
    for file_name, file_size in files_to_allocate:
        start_index = None
        for i in range(len(disk) - file_size + 1):
            if all(block == '' for block in disk[i:i + file_size]):
                start_index = i
                break
        if start_index is not None:
            for i in range(start_index, start_index + file_size):
                disk[i] = file_name
        else:
            new_failed_files.append((file_name, file_size))
    return new_failed_files

# Função para desfragmentar o disco
def defragment_disk(disk):
    new_disk = create_disk(len(disk))
    current_index = 0
    for block in disk:
        if block != '':
            new_disk[current_index] = block
            current_index += 1
    return new_disk

# Função principal para executar cada fase
def main():
    # Fase 1
    print("Fase 1: Alocação inicial de arquivos")
    disk = create_disk(100)
    files = [('File%d' % i, random.randint(2, 6)) for i in range(1, 31)]
    failed_files = add_files_to_disk(disk, files)
    print("Disco após a alocação inicial:")
    print_disk(disk)
    if failed_files:
        print("Arquivos que não puderam ser alocados na fase 1:")
        for file_name, file_size in failed_files:
            print('%s (%d blocos)' % (file_name, file_size))
    else:
        print("Todos os arquivos foram alocados com sucesso na fase 1.")
    print()

    raw_input("Pressione Enter para continuar para a Fase 2...")

    # Fase 2
    print("Fase 2: Remoção de arquivos")
    removed_files_with_sizes = remove_files_from_disk(disk, 10)
    print("Disco após a remoção de arquivos:")
    print_disk(disk)
    print("Arquivos removidos na fase 2:")
    for file, size in removed_files_with_sizes:
        print('%s (%d blocos)' % (file, size))
    print()

    raw_input("Pressione Enter para continuar para a Fase 3...")

    # Fase 3
    print("Fase 3: Realocação de arquivos não alocados e removidos")
    failed_files = reallocate_files(disk, failed_files)
    print("Disco após tentar realocar arquivos não alocados na fase 1:")
    print_disk(disk)
    if failed_files:
        print("Arquivos que não puderam ser alocados na fase 3:")
        for file_name, file_size in failed_files:
            print('%s (%d blocos)' % (file_name, file_size))
    else:
        print("Todos os arquivos não alocados na fase 1 foram alocados com sucesso na fase 3.")
    print()

    # Tentar realocar arquivos removidos na fase 2
    failed_removed_files = reallocate_files(disk, removed_files_with_sizes)
    print("Disco após tentar realocar arquivos removidos na fase 2:")
    print_disk(disk)
    if failed_removed_files:
        print("Arquivos removidos que não puderam ser realocados na fase 3:")
        for file_name, file_size in failed_removed_files:
            print('%s (%d blocos)' % (file_name, file_size))
    else:
        print("Todos os arquivos removidos na fase 2 foram realocados com sucesso na fase 3.")
    print()

    raw_input("Pressione Enter para continuar para a Fase 4...")

    # Fase 4
    print("Fase 4: Desfragmentação do disco")
    disk = defragment_disk(disk)
    print("Disco após desfragmentação:")
    print_disk(disk)
    failed_files = reallocate_files(disk, failed_files)
    failed_removed_files = reallocate_files(disk, failed_removed_files)
    print("Disco após tentar realocar arquivos não alocados na fase 3 e arquivos removidos:")
    print_disk(disk)
    if failed_files or failed_removed_files:
        print("Arquivos que não puderam ser alocados após a desfragmentação:")
        for file_name, file_size in failed_files:
            print('%s (%d blocos)' % (file_name, file_size))
        for file_name, file_size in failed_removed_files:
            print('%s (%d blocos)' % (file_name, file_size))
    else:
        print("Todos os arquivos foram alocados com sucesso após a desfragmentação.")
    print()

if __name__ == '__main__':
    main()
