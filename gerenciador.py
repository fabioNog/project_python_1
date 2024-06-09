def adicionar_tarefa(tarefas,nome_tarefa):
    tarefa = {"nome": nome_tarefa,"completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return 

tarefas = []

while True:

    print("\n Menu do Gerenciador")

    print("1. Adiconar Tarefas")
    print("2. Ver Tarefas")
    print("3. Atualizar Tarefas")
    print("4. Completar Tarefas")
    print("5. Deletar Tarefas Completadas")
    print("6. Sair")

    escolha = input("Digite a sua escolha: ")
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")        
        adicionar_tarefa(tarefas,nome_tarefa)
    elif escolha == "6":        
        break
    
print("Programa Finalizado")