import json

# Função que exibe o menu principal do programa.
def menu() -> None:
    """
    Exibe o menu principal com as opções disponíveis no programa.
    """
    print("\n1 - Exibir lista das pistas")
    print("2 - Estimar uso de bateria durante a corrida")
    print("3 - Estimar a eficiencia da bateria com base na temperatura")
    print("4 - Calcular a distancia TOTAL da corrida")
    print("0 - Encerrar o programa")

# Função que exibe as pistas disponíveis e seus respectivos tamanhos por volta.
def exibir_pistas() -> None:
    """
    Exibe a lista de pistas disponíveis com seus respectivos tamanhos em quilômetros.
    """
    print("\nPISTA -> TAMANHO POR VOLTA\n")
    for chave,valor in pistas.items():
        print(f"{chave}: \t{valor} Km")

#nome da pista: tamanho do circuito (Km)
# Dicionário contendo as pistas e seus tamanhos em quilômetros.
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

#Definições e cálculos relacionados à bateria dos carros de Fórmula-E.

#os carros da fórmula-E tem capacidade total de 47 kWh
#Capacidade maxima de andar 400 Km
#Desempenho máximo (Modo de Qualificação e atack mode): 350 kW. Corridas: 300Kw (OU SEJA 300 Mil Watts)
#Consumo de energia -> Watt (W) * horas (h) / 1.000 = 466 Kwh -> Uso da potencia maxima em 45 minutos (insuficiente para a corrida) devido a disponibilidade total de 47 Kwh.
#Consumo ideal médio (sem recarga nas frenagens) = 62kw que geram 46kWh TOTAIS
#400km / 47 Kwh = 8,5 km por Kw
#recuperação da bateria nas frenagens = até 600kW
#Conta consumo ideal medio final seria: watt(usados) - watt(recuperados(até 600 por frenagem)) * hora total do circuito / 1.000 --> TEM QUE DAR ATE 47 Kwh

#Função para estimar o uso de bateria durante a corrida com base na potência usada e energia recuperada nas frenagens.
def uso_bateria() -> str:
    """
    Calcula o consumo de bateria durante a corrida com base na potência usada e energia recuperada nas frenagens.
    Retorna uma mensagem informando se o consumo foi maior ou menor que o limite de 47 kWh.
    """

    potencia = 0
    tempo = float(input("Digite o tempo em horas da corrida: "))
    for x in range(3):
        potencia += float(input(f"Digite a potencia em KiloWatt(kW) usada no momento {x+1} da corrida (350 max): "))
    frenagens = int(input("Digite a quantidade de frenagens por volta: "))
    recuperacao = 0
    for y in range(frenagens):
        recuperacao += float(input(f"Digite a energia recuperada na frenagem {y+1} em KiloWatt(kW) (600 max): "))

    #cálculos 
    potencia_media = (potencia/3)*1000 #transformando Kw -> W
    recuperacao_media = (recuperacao/frenagens)*1000
    resultado = (((potencia_media - recuperacao_media) * tempo) / 1000)
    meta = 47 #Kwh
    if resultado > meta:
        resposta = f"O consumo atual durante a corrida está em {resultado:.2f} Kwh, ou seja, ULTRAPASSANDO em {abs((resultado-meta)):.2f}Kwh a capacidade de 47Kwh Máximos durante a corrida."
    else:
        resposta = f"O consumo atual durante a corrida está em {resultado:.2f} Kwh, ou seja, ECONOMIZANDO em {abs((resultado-meta)):.2f}Kwh a capacidade de 47Kwh Máximos durante a corrida."
    
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


#temperatura ideal da bateria = 20 a 25 graus (C)
#A margem que se distancia desse range a eficiencia diminui

#Função para estimar a eficiência da bateria com base na temperatura atual.
def eficiencia_bateria(temperatura: float) -> str:
    """
    Calcula a eficiência da bateria com base na temperatura fornecida.
    Retorna a eficiência percentual da bateria.
    """
    eficiencia = 100
    if temperatura > 25:
        nova_eficiencia = eficiencia - (temperatura - 25)
        resposta = f"Devido a temperatura de {temperatura} graus celcius, a eficiencia diminuiu {eficiencia-nova_eficiencia}% resultando em {nova_eficiencia}% de eficácia"

    elif temperatura >= 20 and temperatura <=25:
        nova_eficiencia = eficiencia
        resposta = f"A temperatura {temperatura} graus celcius está na margem ideal, logo a eficiencia se manteve em {nova_eficiencia}% (disponibilidade TOTAL da potencia do carro)"

    else:
        nova_eficiencia = eficiencia - (20 - temperatura)
        resposta = f"Devido a temperatura de {temperatura} graus celcius, a eficiencia diminuiu {eficiencia-nova_eficiencia}% resultando em {nova_eficiencia}% de eficácia"
    
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


#Função para calcular a distância total da corrida com base na pista escolhida e no número de voltas.
def distancia_corrida(pista: str,voltas: int) -> str:
    """
    Calcula a distância total da corrida com base na pista escolhida e no número de voltas.
    Retorna a distância total em quilômetros.
    """
    volta = pistas.get(pista)
    distancia = volta * voltas
    resposta = f"A distancia total da corrida (Race Lenght) é de {distancia}, percorrendo {voltas} voltas."
    
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
    


#programa
#Loop principal do programa que permite ao usuário interagir com o menu e acessar as funcionalidades.
while True:
    menu()
    op = int(input("\nDigite a opção desejada do menu: "))
    match op:
        case 1:
            #Executando a função que exibe as pistas
            exibir_pistas()
        case 2:
            #Guardando em "info" o retorno da função e exibindo
            info = uso_bateria()
            print(info)
        case 3:
            #Recebimento de parametros (temperatura) para executar a função
            temperatura = float(input("Digite a temperatura atual da bateria: "))

            #Guardando em "info" o retorno da função e exibindo
            info = eficiencia_bateria(temperatura)
            print(info)
        case 4:
            #Exibindo a lista de pistas (desempacotada do dicionario)
            lista = []
            for x in pistas.keys():
                lista += [x]
            print(lista)
            
            #Recebimento de parametros (pistas e voltas) para executar a função
            pista = input("Digite o nome da pista desejada: ").upper()
            voltas = int(input("Digite a quantidade de voltas totais da corrida: "))

            #Guardando em "info" o retorno da função e exibindo
            info = distancia_corrida(pista,voltas)
            print(info)
        case 0:
            #Encerrando o loop while do programa principal
            print("Encerrando o programa...")
            break
        case _:
            print("Digite uma opção válida.")