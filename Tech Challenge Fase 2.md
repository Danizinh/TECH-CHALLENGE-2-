![][image1]

**Tech Challenge II**

**IA para Devs**

**Daniela Cruz de Malta \- RM353365**

**Gabriela Maciel Godoi \- RM355125**

**Lucas Sutelo \- RM353721**

**Sumário**

[**Caso de Estudo	3**](\#caso-de-estudo)

[**Descrição do Problema	3**](\#descrição-do-problema)

[**Metodologia	3**](\#metodologia)

[1\. Inicialização dos Dados	3](\#1.-inicialização-dos-dados)

[2\. Funções Auxiliares	3](\#2.-funções-auxiliares)

[3\. Algoritmo Genético	3](\#3.-algoritmo-genético)

[4\. Visualização da Rota	4](\#4.-visualização-da-rota)

[**Discussão de Resultados	4**](\#discussão-de-resultados)

[**Conclusão	4**](\#conclusão)

# 

# 

# **Caso de Estudo** {#caso-de-estudo}

Encontrar a rota de menor distância que permita a um técnico visitar todos os condomínios uma vez e retornar ao ponto de partida, utilizando um algoritmo genético para otimização da rota.

# **Descrição do Problema** {#descrição-do-problema}

O grupo decidiu utilizar um problema de rotas de uma empresa de elevadores, onde o técnico é responsável por visitar uma quantidade de 15 condomínios. O objetivo é encontrar o melhor resultado, ou seja, a rota com menor distância total que permita ao técnico retornar ao seu ponto inicial após visitar todos os locais.

# **Metodologia** {#metodologia}

## 1\. Inicialização dos Dados {#1.-inicialização-dos-dados}

* Definimos um conjunto de coordenadas de latitude e longitude para os edifícios (condomínios).  
* Caso o número de edifícios fornecidos fosse menor que o necessário, coordenadas aleatórias adicionais seriam geradas.

## 2\. Funções Auxiliares {#2.-funções-auxiliares}

* haversine: Calcula a distância entre dois pontos geográficos usando a fórmula Haversine.  
* calcular\_aptidao: Calcula a aptidão de uma rota, que é a distância total percorrida.


## 3\. Algoritmo Genético {#3.-algoritmo-genético}

* **Geração da População Inicial:** Utilizando `gerar_populacao` para criar uma população inicial de rotas aleatórias.  
* **Avaliação da Aptidão:** Avaliando a aptidão de cada indivíduo na população.  
* **Seleção:** Ordenando a população com base na aptidão.  
* **Elitismo:** Mantendo a melhor solução de cada geração.  
* **Crossover e Mutação:** Aplicando crossover e mutação para criar novos indivíduos.  
* **Prevenção de Divisão por Zero:** Adicionando uma pequena constante para evitar divisão por zero nas probabilidades de seleção.  
* **Normalização das Probabilidades:** Normalizando as probabilidades de seleção para garantir uma distribuição correta.


## 4\. Visualização da Rota {#4.-visualização-da-rota}

* Criando um mapa interativo usando Folium para visualizar a melhor rota encontrada.  
* Salvando o mapa em um arquivo HTML.

# **Discussão de Resultados** {#discussão-de-resultados}

GABI vai completar

# **Conclusão** {#conclusão}

Com este Tech Challenge o grupo conseguiu desenvolver um algoritmo genético e aplicar a solução em um caso real de otimização de rotas.

GABI vai completar

[image1]: <data:image/png;base64,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>