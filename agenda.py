import os

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def salvar(): 
    exportar('database.csv')
def carregar():
    importar('database.csv')
def capturar_dados():
    tel = input('Digite o telefone: ')
    email = input('Digite o email: ')
    tag = input('Digite uma tag: ')
    return tel, email, tag

AGENDA = {}

def menu():
    limpar_console()
    while True:
        print(f'========================================\n'
              f'digite 1 para adicionar um contato \n'
              f'digite 2 para remover um contato \n'
              f'digite 3 para visualizar um contato \n'
              f'digite 4 para editar um contato\n'
              f'digite 5 para ver a agenda completa\n'
              f'digite 6 para exportar a agenda\n'
              f'digite 7 para importar uma agenda\n'
              f'digite 0 para encerrar o programa\n'
              f'========================================')
        try:
            opcao = int(input('escolha uma opcao: '))
        except ValueError:
            print(f'insira apenas numeros!')
            continue
        if opcao == 1:
            contato = input(f'digite o nome de um contato: ')
            adicionar(contato)
        elif opcao == 2:
            contato = input(f'digite o nome de um contato: ')
            remover(contato)
        elif opcao == 3:
            contato = input(f'digite o nome de um contato: ')
            visualizar(contato)
        elif opcao == 4:
            contato = input(f'digite o nome de um contato: ')
            editar(contato)
        elif opcao == 5:
            verTudo()
        elif opcao == 6:
            nome_do_arquivo = input('insira o nome do arquivo que deseja exportar: ')
            exportar(nome_do_arquivo)
        elif opcao == 7:
            nome_do_arquivo = input('insira o nome do arquivo: ')
            importar(nome_do_arquivo)
        elif opcao == 0:
            print('>>> encerrando o programa...')
            break
        else: 
            print('selecione um numero entre 0 e 5')
        input('pressione Enter para continuar ')
        limpar_console()
def verTudo():
    if not AGENDA:
        print(f'a agenda esta vazia!')
    else:
        for i, contato in enumerate(AGENDA, start=1):
            print (f'{i} -> {contato}')
def visualizar(contato):
    if contato in AGENDA:
        print(f'\nnome: {contato}\n'
              f'email:{AGENDA[contato]['email']}\n'
              f'telefone:{AGENDA[contato]['tel']}\n'
              f'tag:{AGENDA[contato]['tag']}\n')
    else:
        print(f'contato nao encontrado!')
def remover(contato):
    if contato in AGENDA:
        AGENDA.pop(contato)
        salvar()
        print(f'>>>>> o contato {contato} foi removido')
    else:
        print(f'Este contato não existe!')
def adicionar(contato):
    if contato in AGENDA:
        print(f'ja existe um contato com esse nome. Deseja editar?')
        try:
            opcao = int(input('digite 1 para aceitar ou 2 para cancelar: '))
        except ValueError:
            print('insira apenas numeros')
            return     
        if opcao == 1:
            editar(contato)
        elif opcao == 2:
            print('operação cancelada')
        else:
            print('Opção inválida. Operação cancelada.')
    else:
        tel, email, tag = capturar_dados()
        AGENDA[contato] = {'tel':tel, 'email':email, 'tag':tag}
        salvar()
        print(f'>>>>> o contato {contato} foi adicionado')
def editar(contato):
    if contato in AGENDA:
        print(f'\nEditando o contato {contato}:\n'
            f'1 - Nome atual: {contato}\n'
            f'2 - Telefone atual: {AGENDA[contato]["tel"]}\n'
            f'3 - Email atual: {AGENDA[contato]["email"]}\n'
            f'4 - tag atual: {AGENDA[contato]["tag"]}\n')
        try: 
            opcao = int(input('selecione o que voce quer alterar: '))
        except ValueError:
            print('selecione apenas numeros entre 1 a 4')
            return
        if opcao == 1:
            novo_nome = input('insira um novo nome: ')
            if novo_nome in AGENDA:
                print('já existe um contato com esse nome.')
            else:
                AGENDA[novo_nome] = AGENDA.pop(contato)
                salvar()
                print(f'Nome atualizado para {novo_nome}.')
        if opcao == 2:
            novo_tel = input('digite o novo telefone: ')
            AGENDA[contato]['tel'] = novo_tel
            salvar()
            print(f'Telefone atualizado para {novo_tel}.')

        elif opcao == 3:

            novo_email = input('insira o novo email: ')
            AGENDA[contato]['email'] = novo_email
            salvar()
            print(f'Email atualizado para {novo_email}.')
        elif opcao == 4:

            nova_tag = input('Digite uma nova tag: ')
            AGENDA[contato]['tag'] = nova_tag
            salvar()
            print(f'tag atualizada para {nova_tag}.')
    else:
        print(f'o contato não existe')
        pass
def exportar(nome_do_arquivo):
    try:
        with open(nome_do_arquivo,'w') as arquivo:
            for contato in AGENDA:
                tel = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                tag = AGENDA[contato]['tag']
                arquivo.write(f'{contato}, {tel}, {email}, {tag}\n')
        print(f'foram exportados {len(AGENDA)} contatos')
    except Exception as error:
        print(f'ocorreu um erro. {error}')
def importar(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(',')
                nome = dados[0]
                tel = dados[1]
                email = dados[2]
                tag = dados[3]
            
                AGENDA[nome] = {'tel':tel,'email':email,'tag':tag}
        print(f'foram importados {len(linhas)} contatos')
    except FileNotFoundError:
        print('arquivo nao encontrado')

    except Exception as error:
        print(f'ocorreu um erro {error}')

carregar()
menu()