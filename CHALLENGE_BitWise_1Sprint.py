import json

# Função que exibe o menu principal do programa.
def menu():
    print("\n1 - Exibir lista das pistas")
    print("2 - Estimar uso de bateria durante a corrida")
    print("3 - Estimar a eficiencia da bateria com base na temperatura")
    print("4 - Calcular a distancia TOTAL da corrida")
    print("0 - Encerrar o programa")

# Função que exibe as pistas disponíveis e seus respectivos tamanhos por volta.
def exibir_pistas():
    print("\nPISTA -> TAMANHO POR VOLTA\n")
    for chave,valor in pistas.items():
        print(f"{chave}: \t{valor} Km")

pistas = {
    "MEXICO CITY": 2.628,
    "DIRIYAH": 2.495,
    "SÃO PAULO": 2.933,
    "MISANO": 3.381,
    "MONACO": 3.337,
    "BERLIN": 2.343,
    "SHANGHAI": 3.051,
    "PORTLAND": 3.221,
    "LONDON": 2.09,
}

# Função para estimar o uso de bateria durante a corrida.
def uso_bateria():
    potencia = 0
    tempo = float(input("Digite o tempo em horas da corrida: "))
    for x in range(3):
        potencia += float(input(f"Digite a potencia em KiloWatt(kW) usada no momento {x+1} da corrida (350 max): "))
    frenagens = int(input("Digite a quantidade de frenagens por volta: "))
    recuperacao = 0
    for y in range(frenagens):
        recuperacao += float(input(f"Digite a energia recuperada na frenagem {y+1} em KiloWatt(kW) (600 max): "))

    potencia_media = (potencia/3)*1000
    recuperacao_media = (recuperacao/frenagens)*1000
    resultado = (((potencia_media - recuperacao_media) * tempo) / 1000)

    meta = 47  # Kwh
    if resultado > meta:
        resposta = f"O consumo atual durante a corrida está em {resultado:.2f} Kwh, ULTRAPASSANDO {abs((resultado-meta)):.2f}Kwh a capacidade de 47Kwh."
    else:
        resposta = f"O consumo atual durante a corrida está em {resultado:.2f} Kwh, ECONOMIZANDO {abs((resultado-meta)):.2f}Kwh a capacidade de 47Kwh."

    # Salvando os dados em arquivo JSON
    dados = {
        "bateria": {
            "usagem": f"{resultado:.2f} Kwh",
            "relacao": f"{abs((resultado-meta)):.2f} Kwh",
            "status": "ultrapassando" if resultado > meta else "economizando"
        }
    }
    with open('dados_bateria.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

    return resposta

# Função para estimar a eficiência da bateria com base na temperatura.
def eficiencia_bateria(temperatura):
    eficiencia = 100
    if temperatura > 25:
        nova_eficiencia = eficiencia - (temperatura - 25)
        resposta = f"Devido à temperatura de {temperatura}°C, a eficiência diminuiu {eficiencia-nova_eficiencia}% resultando em {nova_eficiencia}% de eficácia."
    elif 20 <= temperatura <= 25:
        nova_eficiencia = eficiencia
        resposta = f"A temperatura {temperatura}°C está na margem ideal, logo a eficiência se manteve em {nova_eficiencia}%."
    else:
        nova_eficiencia = eficiencia - (20 - temperatura)
        resposta = f"Devido à temperatura de {temperatura}°C, a eficiência diminuiu {eficiencia-nova_eficiencia}% resultando em {nova_eficiencia}% de eficácia."

    # Salvando os dados em arquivo JSON
    dados = {
        "eficiencia_bateria": {
            "temperatura": f"{temperatura}°C",
            "eficiencia_restante": f"{nova_eficiencia}%"
        }
    }
    with open('dados_eficiencia_bateria.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

    return resposta

# Função para calcular a distância total da corrida.
def distancia_corrida(pista, voltas):
    volta = pistas.get(pista)
    distancia = volta * voltas
    resposta = f"A distância total da corrida é de {distancia} Km, percorrendo {voltas} voltas."

    # Salvando os dados em arquivo JSON
    dados = {
        "distancia_corrida": {
            "pista": pista,
            "voltas": voltas,
            "distancia_total": f"{distancia} Km"
        }
    }
    with open('dados_distancia_corrida.json', 'w') as arquivo_json:
        json.dump(dados, arquivo_json, indent=4)

    return resposta

# Programa principal
while True:
    menu()
    op = int(input("\nDigite a opção desejada do menu: "))
    match op:
        case 1:
            exibir_pistas()
        case 2:
            info = uso_bateria()
            print(info)
        case 3:
            temperatura = float(input("Digite a temperatura atual da bateria: "))
            info = eficiencia_bateria(temperatura)
            print(info)
        case 4:
            lista = list(pistas.keys())
            print(lista)
            pista = input("Digite o nome da pista desejada: ").upper()
            voltas = int(input("Digite a quantidade de voltas totais da corrida: "))
            info = distancia_corrida(pista, voltas)
            print(info)
        case 0:
            print("Encerrando o programa...")
            break
        case _:
            print("Digite uma opção válida.")
