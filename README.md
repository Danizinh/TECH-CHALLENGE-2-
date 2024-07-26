# Otimização de Rota para Manutenção Predial 🏢

Este projeto utiliza um algoritmo genético para otimizar a rota de um técnico de manutenção que precisa visitar diversos edifícios. O objetivo é minimizar a distância total percorrida, considerando as coordenadas geográficas de cada edifício.

## ⚙️ Como funciona

1. **Geração da População Inicial**: Um conjunto de rotas pré-definidas e aleatórias é criado, representando possíveis sequências de visitas aos edifícios.

2. **Avaliação (Aptidão)**: Cada rota é avaliada com base na sua distância total, utilizando a fórmula Haversine para calcular distâncias geográficas precisas entre os edifícios.

3. **Seleção**: As melhores rotas (aquelas com menor distância) têm maior probabilidade de serem selecionadas para a próxima geração.

4. **Cruzamento**: Novas rotas são geradas combinando partes de rotas existentes.

5. **Mutação**: Pequenas alterações aleatórias são introduzidas nas novas rotas para explorar novas possibilidades e evitar soluções locais.

6. **Repetição**: Os passos 2 a 5 são repetidos por várias gerações, até que uma solução satisfatória seja encontrada ou um número máximo de gerações seja atingido.

## 🗺️ Visualização

A rota otimizada final é exibida em um mapa interativo utilizando a biblioteca Folium. Os edifícios são marcados, e a rota ideal é traçada entre eles.

## 🚀 Como usar

### Pré-requisitos

- Python 3.x
- Bibliotecas: `random`, `itertools`, `sys`, `numpy`, `genetic_algorithm` (fornecido pelo Prof. SérgioPolimante), `folium`, `geopy`

### Instalação

Instale as bibliotecas necessárias:

```bash
pip install folium geopy
```

### Execução

```bash
python otimizador.py
```

Um mapa HTML (rota_otimizada.html) será gerado, exibindo a rota otimizada para a visita aos edifícios.
