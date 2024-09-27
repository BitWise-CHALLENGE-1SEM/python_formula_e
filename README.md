# BitWise: Projeto CHALLENGE Fórmula E - 1 semestre (sprint 1) 

## Alunos: 
	1. Bruno Biletsky Gonçalves dos Santos - RM: 554739 
	2. Enrico Ricarte Rodrigues - RM: 558571
	3. Victor Freire Martins Siqueira - RM: 556191
	4. Matheus Gushi Morioka - RM: 556935
	5. Pedro Gaspar Fernandes Ferrari - RM: 554887
	
# Formula-E Race Assistant

Este programa é uma ferramenta de assistência para corridas de Formula-E, permitindo aos usuários calcular e estimar diversos aspectos importantes da corrida, a eficiência da bateria com base na temperatura e dados estimados sobre o uso ideal da potencia da bateria (indicar se está fora da margem necessária para a distância total da corrida).

## Instruções de Uso

Para utilizar o programa, siga os passos abaixo:

1. Execute o arquivo do programa no seu terminal ou IDE de preferência.
2. Um menu será exibido com as seguintes opções:
   - `1` - Exibir lista das pistas
   - `2` - Estimar uso de bateria durante a corrida
   - `3` - Estimar a eficiencia da bateria com base na temperatura
   - `4` - Calcular a distancia TOTAL da corrida
   - `0` - Encerrar o programa
3. Digite o número correspondente à opção desejada e pressione Enter.
4. Siga as instruções adicionais que aparecerão no terminal para fornecer os dados necessários para cada cálculo.

## Requisitos

- Python 3.x

## Dependências

Não há dependências externas necessárias para executar este programa.

## Informações Adicionais

- O dicionário `pistas` contém as pistas disponíveis e seus respectivos tamanhos em quilômetros por volta.
- A função `uso_bateria` estima o uso de bateria durante a corrida com base na potência usada e energia recuperada nas frenagens. Alertando se estiver fora da margem necessária pra completar a corrida.
- A função `eficiencia_bateria` estima a eficiência da bateria com base na temperatura atual.
- A função `distancia_corrida` calcula a distância total da corrida com base na pista escolhida e no número de voltas.
