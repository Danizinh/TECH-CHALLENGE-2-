import random
import itertools
import numpy as np
from genetic_algorithm import mutate as mutacao, order_crossover as cruzamento, generate_random_population as gerar_populacao, calculate_fitness as calcular_aptidao, sort_population as ordenar_populacao
from geopy.distance import geodesic

# Valores constantes
N_TESTES = 5
MENOR_DIST = 47
N_EDIFICIOS = 10
N_GERACOES = 300
TAM_POPULACAO = 100
PROBABILIDADE_MUTACAO = 0.3

# Lista de coordenadas dos edifícios (latitude, longitude)
locais_edificios = [
    (-30.079948, -51.2093066),
    (-30.0220521, -51.2023915),
    (-29.948837, -51.099896),
    (-30.0303042, -51.2251123), 
    (-29.9194706, -51.1821899),
    (-29.922883, -51.1822102),
    (-30.0272048, -51.2034566),
    (-30.0109574, -51.1899711),
    (-30.0183578, -51.200375),
    (-29.9862553, -51.191835),
    #Podem ser adicionados mais locais
]

# Se houver menos edifícios fornecidos do que o necessário, gera aleatórios (para fins de exemplo)
while len(locais_edificios) < N_EDIFICIOS:
    locais_edificios.append((
        random.uniform(-29.9, -30.1), # Latitude
        random.uniform(-51, -51.3) # Longitude
    ))

# Calcula a distância entre dois pontos, em km
def haversine(coord1, coord2):
    return geodesic(coord1, coord2).kilometers

# Substitui o cálculo de aptidão para usar a distância Haversine
def calcular_aptidao(individuo):
    distancia_total = 0
    for i in range(len(individuo) - 1):
        distancia_total += haversine(locais_edificios[individuo[i]], locais_edificios[individuo[i + 1]])
    distancia_total += haversine(locais_edificios[individuo[-1]], locais_edificios[individuo[0]]) # Retorno ao início
    return distancia_total


# Loop principal

n_test = 0
media_geracao = 0

while n_test < N_TESTES:

    # Inicializa o problema
    populacao = gerar_populacao(list(range(len(locais_edificios))), TAM_POPULACAO)
    valores_melhor_aptidao = []
    melhores_solucoes = []

    contador_geracoes = itertools.count(start=1)
    geracao = 1
    melhor_aptidao = 99999999

    while melhor_aptidao > MENOR_DIST or geracao > N_GERACOES:
        
        aptidao_populacao = [calcular_aptidao(individuo) for individuo in populacao]
        populacao, aptidao_populacao = ordenar_populacao(populacao, aptidao_populacao)

        melhor_aptidao = calcular_aptidao(populacao[0])
        melhor_solucao = populacao[0]

        valores_melhor_aptidao.append(melhor_aptidao)
        melhores_solucoes.append(melhor_solucao)

        nova_populacao = [populacao[0]]  # Elitismo


        # Prevenção de divisão por zero
        probabilidade = 1 / (np.array(aptidao_populacao) + 1e-6)  # Adiciona pequena constante para evitar divisão por zero
        probabilidade /= probabilidade.sum()  # Normaliza as probabilidades
        
        
        while len(nova_populacao) < TAM_POPULACAO:
            pai1, pai2 = random.choices(populacao, weights=probabilidade, k=2)
            filho1 = cruzamento(pai1, pai2)
            #filho1, filho2 = cruzamento_2(pai1, pai2)
            filho1 = mutacao(filho1, PROBABILIDADE_MUTACAO)
            #filho2 = mutacao(filho2, PROBABILIDADE_MUTACAO)
            nova_populacao.append(filho1)
            #nova_populacao.append(filho2)

        
        melhor_geracao = geracao

        populacao = nova_populacao
        geracao += 1

    print(f"Geração {melhor_geracao}: Melhor distância = {round(melhor_aptidao, 2)} km - {melhor_solucao}")

    media_geracao = media_geracao + melhor_geracao

    n_test += 1

media_geracao = media_geracao / 3

print(f"Média de Gerações = {round(media_geracao, 2)}")