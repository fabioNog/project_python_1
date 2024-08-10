def adicionar_tarefa(tarefas, nome_tarefa):
    if not nome_tarefa.strip():
        raise ValueError("O nome da tarefa não pode estar vazio.")
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
    if not novo_nome_tarefa.strip():
        raise ValueError("O novo nome da tarefa não pode estar vazio.")
    if 0 < indice_tarefa <= len(tarefas):
        tarefas[indice_tarefa - 1]["nome"] = novo_nome_tarefa
        print("Tarefa atualizada com sucesso!")
    else:
        raise ValueError("Índice inválido. Por favor, insira um número dentro do intervalo de tarefas disponíveis.")

def completar_tarefa(tarefas, indice_tarefa):
    if 0 < indice_tarefa <= len(tarefas):
        tarefas[indice_tarefa - 1]["completada"] = True
        print("Tarefa marcada como completada!")
    else:
        raise ValueError("Índice inválido. Por favor, insira um número dentro do intervalo de tarefas disponíveis.")

def deletar_tarefa(tarefas, indice_tarefa):
    if 0 < indice_tarefa <= len(tarefas):
        tarefa_removida = tarefas.pop(indice_tarefa - 1)
        print(f"Tarefa '{tarefa_removida['nome']}' foi deletada com sucesso!")
    else:
        raise ValueError("Índice inválido. Por favor, insira um número dentro do intervalo de tarefas disponíveis.")

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
            except ValueError as ve:
                print(f"Erro: {ve}")
        elif escolha == "4":
            try:
                indice = int(input("Digite o número da tarefa que deseja marcar como completada: "))
                completar_tarefa(tarefas, indice)
            except ValueError as ve:
                print(f"Erro: {ve}")
        elif escolha == "5":
            try:
                indice = int(input("Digite o número da tarefa que deseja deletar: "))
                deletar_tarefa(tarefas, indice)
            except ValueError as ve:
                print(f"Erro: {ve}")
        elif escolha == "6":
            break
        else:
            print("Escolha inválida. Tente novamente.")

    except ValueError as ve:
        print(f"Ocorreu um erro: {ve}")

print("Programa Finalizado")
