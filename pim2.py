from datetime import datetime
import time
import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Senha definida
senha_correta = "1234"
tentativas = 3

# Tela de boas-vindas
limpar_tela()
print("="*60)
print("🔐  SISTEMA PROTEGIDO: PORTAL DE GESTÃO SEGURA DE DADOS  🔐")
print("="*60)
print("Atenção: este sistema é restrito. Apenas usuários autorizados podem acessá-lo.")
print("Digite sua senha para continuar.")
print("-"*60)

# Tentativas de senha
while tentativas > 0:
    tentativa = input("🔑 Senha de acesso: ")
    print("Verificando credenciais...")
    time.sleep(1.5)

    if tentativa == senha_correta:
        print("\n✅ Acesso concedido. Bem-vindo ao sistema de dados pessoais!")
        time.sleep(1)
        limpar_tela()
        # Aqui começa o menu principal...

        usuarios = []

        while True:
            print("""
        [ 1 ] Cadastrar Usuário
        [ 2 ] Editar Usuário
        [ 3 ] Visualizar Usuário
        [ 4 ] Excluir Usuário
        [ 5 ] Sair
        """)

            opcao = int(input('Digite a opção desejada: '))

            if opcao == 1:
                nome = input('Digite o nome: ')
                cpf = input('Digite o CPF: ')
                nascimento = input('Digite a data de nascimento (DD/MM/AAAA): ')
                email = input('Digite o email: ')

                try:
                    data_formatada = datetime.strptime(nascimento, "%d/%m/%Y")
                    usuario = {
                        'nome': nome,
                        'cpf': cpf,
                        'nascimento': nascimento,
                        'email': email
                    }
                    usuarios.append(usuario)
                    print('Cadastro adicionado com sucesso!')
                except ValueError:
                    print("Data inválida! Use o formato DD/MM/AAAA.")

            elif opcao == 2:
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                else:
                    print("\n--- Usuários Cadastrados ---")
                    for i, u in enumerate(usuarios):
                        print(f"[{i}] {u['nome']} - CPF: {u['cpf']}")

                    try:
                        indice = int(input("Digite o número do usuário que deseja editar: "))
                        if 0 <= indice < len(usuarios):
                            usuario = usuarios[indice]
                            print(f"Editando {usuario['nome']}")

                            novo_nome = input(f"Nome ({usuario['nome']}): ") or usuario['nome']
                            novo_cpf = input(f"CPF ({usuario['cpf']}): ") or usuario['cpf']
                            novo_nascimento = input(f"Nascimento ({usuario['nascimento']}): ") or usuario['nascimento']
                            novo_email = input(f"Email ({usuario['email']}): ") or usuario['email']

                            try:
                                datetime.strptime(novo_nascimento, "%d/%m/%Y")  # valida a nova data
                                usuario.update({
                                    'nome': novo_nome,
                                    'cpf': novo_cpf,
                                    'nascimento': novo_nascimento,
                                    'email': novo_email
                                })
                                print("Usuário atualizado com sucesso!")
                            except ValueError:
                                print("Data de nascimento inválida! Alterações canceladas.")
                        else:
                            print("Índice inválido.")
                    except ValueError:
                        print("Entrada inválida.")

            elif opcao == 3:
                if not usuarios:
                    print("Nenhum usuário cadastrado.")
                else:
                    print("\n--- Lista de Usuários ---")
                    for i, u in enumerate(usuarios):
                        print(f"Usuário {i + 1}:")
                        print(f"  Nome: {u['nome']}")
                        print(f"  CPF: {u['cpf']}")
                        print(f"  Nascimento: {u['nascimento']}")
                        print(f"  Email: {u['email']}\n")

            elif opcao == 4:

                if not usuarios:
                    print("Nenhum usuário cadastrado.")

                else:
                    print("\n--- Usuários Cadastrados ---")

                    for i, u in enumerate(usuarios):
                        print(f"[{i}] {u['nome']} - CPF: {u['cpf']}")

                    try:
                        indice = int(input("Digite o número do usuário que deseja excluir: "))

                        if 0 <= indice < len(usuarios):
                            confirmacao = input(
                                f"Tem certeza que deseja excluir {usuarios[indice]['nome']}? (s/n): ").lower()

                            if confirmacao == 's':
                                usuarios.pop(indice)
                                print("Usuário excluído com sucesso!")

                            else:
                                print("Exclusão cancelada.")

                        else:
                            print("Índice inválido.")

                    except ValueError:
                        print("Entrada inválida.")

            elif opcao == 5:
                print("Saindo do programa...")
                break

            else:
                print("Opção inválida. Tente novamente.")
        break
    else:
        tentativas -= 1
        print(f"❌ Senha incorreta. Tentativas restantes: {tentativas}\n")
        time.sleep(1)

# Se todas as tentativas forem usadas
if tentativas == 0:
    print("🚫 Acesso bloqueado. Número de tentativas excedido.")
    print("Por motivos de segurança, o sistema será encerrado.")
    time.sleep(2)
    exit()
