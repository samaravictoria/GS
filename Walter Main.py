# Import necessary libraries
import sys
from unidecode import unidecode

# Definindo os pontos de coleta por tipo de resíduo
pontos_de_coleta = {
    'Metal': 'Ponto de Coleta de Metal: Rua Oscar Freire, 500',
    'Papel': 'Ponto de Coleta de Papel: Avenida Paulista, 1578',
    'Plástico': 'Ponto de Coleta de Plástico: Rua da Consolação, 2302',
    'Vidro': 'Ponto de Coleta de Vidro: Rua Augusta, 1508',
    'Orgânico': 'Ponto de Coleta de Orgânico: Rua Vergueiro, 1000',
    'Eletrônico': 'Ponto de Coleta de Eletrônico: Rua Santa Ifigênia, 556'
}

# Mapeamento para tratar variações de entrada
tipo_residuo_mapeamento = {
    'metal': 'Metal',
    'papel': 'Papel',
    'plastico': 'Plástico',
    'vidro': 'Vidro',
    'organico': 'Orgânico',
    'eletronico': 'Eletrônico'
}

# Lista de resíduos do usuário
residuos_usuario = []

# Dados do usuário
usuario = {}

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Opções:")
    print("1. Adicionar resíduo")
    print("2. Ver resíduos adicionados")
    print("3. Ver pontos de coleta")
    print("4. Ver informações do usuário")
    print("5. Sair")

# Função para normalizar a entrada do usuário
def normalizar_tipo_residuo(tipo):
    tipo_normalizado = unidecode(tipo.strip().lower())
    return tipo_residuo_mapeamento.get(tipo_normalizado, None)

# Função para adicionar resíduo à lista
def adicionar_residuo():
    while True:
        print("\nTipos de resíduos disponíveis:")
        for tipo in pontos_de_coleta.keys():
            print(f"- {tipo}")

        tipo_residuo = input("Digite o tipo de resíduo que deseja adicionar: ").strip()
        tipo_residuo_normalizado = normalizar_tipo_residuo(tipo_residuo)

        if tipo_residuo_normalizado:
            residuos_usuario.append(tipo_residuo_normalizado)
            print(f"{tipo_residuo_normalizado} adicionado à lista de resíduos.")
            break
        else:
            print("Tipo de resíduo inválido. Por favor, tente novamente.")

# Função para exibir resíduos adicionados
def ver_residuos():
    if residuos_usuario:
        print("\nResíduos adicionados:")
        for i, residuo in enumerate(residuos_usuario, start=1):
            print(f"{i}. {residuo}")
    else:
        print("\nNenhum resíduo adicionado.")

# Função para exibir pontos de coleta
def ver_pontos_de_coleta():
    if residuos_usuario:
        print("\nPontos de coleta recomendados:")
        pontos_unicos = set(residuos_usuario)
        for ponto in pontos_unicos:
            print(pontos_de_coleta[ponto])
    else:
        print("\nNenhum resíduo adicionado para sugerir pontos de coleta.")

# Função para exibir informações do usuário
def ver_info_usuario():
    if usuario:
        print("\nInformações do Usuário:")
        for chave, valor in usuario.items():
            print(f"{chave.capitalize()}: {valor}")
    else:
        print("\nNenhuma informação de usuário cadastrada.")

# Função para cadastrar usuário
def cadastrar_usuario():
    print("\nCadastro de Usuário")
    usuario['nome'] = input("Digite seu nome: ").strip()
    usuario['email'] = input("Digite seu email: ").strip()
    usuario['telefone'] = input("Digite seu telefone: ").strip()
    print(f"Usuário {usuario['nome']} cadastrado com sucesso!")

# Função principal
def main():
    cadastrar_usuario()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            adicionar_residuo()
        elif opcao == '2':
            ver_residuos()
        elif opcao == '3':
            ver_pontos_de_coleta()
        elif opcao == '4':
            ver_info_usuario()
        elif opcao == '5':
            print("Saindo do sistema. Obrigado!")
            sys.exit()
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
