import random
import itertools
import numpy as np
from genetic_algorithm import mutate as mutacao, order_crossover as cruzamento, generate_random_population as gerar_populacao, calculate_fitness as calcular_aptidao, sort_population as ordenar_populacao
import folium
from geopy.distance import geodesic

# Valores constantes
N_EDIFICIOS = 15
TAM_POPULACAO = 100
N_GERACOES = 300
PROBABILIDADE_MUTACAO = 0.6

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

# Inicializa o problema
populacao = gerar_populacao(list(range(len(locais_edificios))), TAM_POPULACAO)
valores_melhor_aptidao = []
melhores_solucoes = []

# Loop principal
contador_geracoes = itertools.count(start=1)
geracao = 1
while geracao <= N_GERACOES:
       
    aptidao_populacao = [calcular_aptidao(individuo) for individuo in populacao]
    populacao, aptidao_populacao = ordenar_populacao(populacao, aptidao_populacao)

    melhor_aptidao = calcular_aptidao(populacao[0])
    melhor_solucao = populacao[0]

    valores_melhor_aptidao.append(melhor_aptidao)
    melhores_solucoes.append(melhor_solucao)

    print(f"Geração {geracao}: Melhor aptidão = {round(melhor_aptidao, 2)} km - {melhor_solucao}")

    nova_populacao = [populacao[0]]  # Elitismo


# Prevenção de divisão por zero
    probabilidade = 1 / (np.array(aptidao_populacao) + 1e-6)  # Adiciona pequena constante para evitar divisão por zero
    probabilidade /= probabilidade.sum()  # Normaliza as probabilidades
    
     
    while len(nova_populacao) < TAM_POPULACAO:
        pai1, pai2 = random.choices(populacao, weights=probabilidade, k=2)
        filho1 = cruzamento(pai1, pai2)
        filho1 = mutacao(filho1, PROBABILIDADE_MUTACAO)
        nova_populacao.append(filho1)

    populacao = nova_populacao
    geracao += 1

# Exibe o melhor percurso em um mapa
melhor_percurso = melhores_solucoes[-1]
mapa_percurso = folium.Map(location=[-30,-51], zoom_start=11)
for i in range(len(melhor_percurso)):
    inicio = locais_edificios[melhor_percurso[i]]
    fim = locais_edificios[melhor_percurso[(i + 1) % len(melhor_percurso)]]
    folium.Marker(inicio, tooltip=f"Edifício {i + 1}").add_to(mapa_percurso)
    folium.Marker(fim, tooltip=f"Edifício {i + 2}").add_to(mapa_percurso)
    folium.PolyLine([inicio, fim], color="blue").add_to(mapa_percurso)

# Salva o mapa em um arquivo HTML
mapa_percurso.save("rota_otimizada.html")
print("Mapa salvo em rota_otimizada.html")
