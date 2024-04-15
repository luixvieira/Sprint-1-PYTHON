# Sistema de Pré-Atendimento para Diagnóstico de Problemas em Carros

def exibir_menu():
    print("Bem-vindo ao Sistema de Pré-Atendimento para Carros!")
    print("Escolha uma opção:")
    print("1. Registrar problemas do carro")
    print("2. Realizar diagnóstico")
    print("3. Sair")

def registrar_problemas():
    problemas = input("Digite os problemas do carro (separados por vírgula): ")
    return problemas.split(", ")
# O split serve para separar os problemas, dessa forma, a cada vigurla, vira um problema novo

def realizar_diagnostico(problemas):
    # Lógica para determinar o possível problema com base nos problemas registrados
    # Aqui a gnt pode implementar regras especificas para a detecção dos problemas

    # Exemplo simples: se "motor" estiver nos problemas digitados, sugerir o diagnostico "problema no motor"
    if "motor" in problemas:
        print("Possível problema: motor com defeito")
    elif "pneu" in problemas:
        print("Possivel problema no pneu, entre em nosso site para poder realizar a troca.")
    else:
        print("Não foi possível determinar o problema com base nos dados fornecidos.")

def main():
    while True:
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            problemas_registrados = registrar_problemas()
            print("Problemas registrados:", problemas_registrados)
        elif opcao == "2":
            possivel_problema = realizar_diagnostico(problemas_registrados)
            print("Diagnóstico:", possivel_problema)
        elif opcao == "3":
            print("Encerrando o programa. Obrigado!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
