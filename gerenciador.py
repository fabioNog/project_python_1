def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"nome": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' foi adicionada com sucesso!")

def ver_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa disponível.")
    else:
        print("\nLista de Tarefas:")
        for indice, tarefa in enumerate(tarefas, start=1):
            status = "✓" if tarefa["completada"] else " "
            nome_tarefa = tarefa["nome"]
            print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):
    try:
        if 0 < indice_tarefa <= len(tarefas):
            tarefas[indice_tarefa - 1]["nome"] = novo_nome_tarefa
            print("Tarefa atualizada com sucesso!")
        else:
            print("Índice inválido.")
    except Exception as e:
        print(f"Erro ao atualizar tarefa: {e}")

def completar_tarefa(tarefas, indice_tarefa):
    try:
        if 0 < indice_tarefa <= len(tarefas):
            tarefas[indice_tarefa - 1]["completada"] = True
            print("Tarefa marcada como completada!")
        else:
            print("Índice inválido.")
    except Exception as e:
        print(f"Erro ao completar tarefa: {e}")

def deletar_tarefa(tarefas, indice_tarefa):
    try:
        if 0 < indice_tarefa <= len(tarefas):
            tarefa_removida = tarefas.pop(indice_tarefa - 1)
            print(f"Tarefa '{tarefa_removida['nome']}' foi deletada com sucesso!")
        else:
            print("Índice inválido.")
    except Exception as e:
        print(f"Erro ao deletar tarefa: {e}")

tarefas = []

while True:
    try:
        print("\nMenu do Gerenciador:")
        print("1. Adicionar Tarefa")
        print("2. Ver Tarefas")
        print("3. Atualizar Tarefa")
        print("4. Completar Tarefa")
        print("5. Deletar Tarefa")
        print("6. Sair")

        escolha = input("Digite a sua escolha: ")

        if escolha == "1":
            nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
            adicionar_tarefa(tarefas, nome_tarefa)
        elif escolha == "2":
            ver_tarefas(tarefas)
        elif escolha == "3":
            try:
                indice = int(input("Digite o número da tarefa que deseja atualizar: "))
                novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
                atualizar_tarefa(tarefas, indice, novo_nome_tarefa)
            except ValueError:
                print("Por favor, insira um número válido para o índice.")
        elif escolha == "4":
            try:
                indice = int(input("Digite o número da tarefa que deseja marcar como completada: "))
                completar_tarefa(tarefas, indice)
            except ValueError:
                print("Por favor, insira um número válido para o índice.")
        elif escolha == "5":
            try:
                indice = int(input("Digite o número da tarefa que deseja deletar: "))
                deletar_tarefa(tarefas, indice)
            except ValueError:
                print("Por favor, insira um número válido para o índice.")
        elif escolha == "6":
            break
        else:
            print("Escolha inválida. Tente novamente.")

    except Exception as e:
        print(f"Ocorreu um erro: {e}")

print("Programa Finalizado")
