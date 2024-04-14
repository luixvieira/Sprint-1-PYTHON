# Sistema de Pré e Auto-atendimento de problemas em carros

# Criando a função exibir menu, quando eu chama-lá pelo nome da função, ela rodará.

def exibir_menu():
    print("Bem-vindo ao Sistema de Pré-Atendimento para Carros!")
    print("Escolha uma opção:")
    print("1. Registrar problemas do carro")
    print("2. Realizar diagnóstico")
    print("3. Sair")

# Criando função para registrar problemas
def registrar_problemas():
    problemas = input("Digite os problemas do carro (separados por vírgula): ")
    return problemas.split(", ")
    # a função split serve para separar o que foi inserido no input, desta forma,
    # quando eu defini o parametro para a sepação como ",", os problemas serao salvos separadamente