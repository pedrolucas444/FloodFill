# FloodFill - Mapeamento de Terreno para Robôs Autônomos

## Sobre o Projeto

O **FloodFill Mapper** é um projeto educativo desenvolvido
para demonstrar a aplicação prática do **Algoritmo Flood Fill**
(Preenchimento por Inundação) na resolução de problemas de mapeamento de
terrenos.

O sistema simula um robô autônomo que precisa identificar
e classificar regiões conectadas em um grid, diferenciando áreas
navegáveis de obstáculos e reconhecendo zonas isoladas
(desconectadas).

Este projeto atende aos requisitos do "Trabalho em Grupo 2" da
disciplina de **Fundamentos de Projeto e Análise de Algoritmos**.

------------------------------------------------------------------------

## Contexto

Sua equipe foi contratada por uma empresa de automação
para desenvolver um sistema de mapeamento inteligente. O
terreno é representado como um grid bidimensional desconhecido pelo
robô. Nele, existem:

-   **Espaços livres:** Onde o robô pode transitar.
-   **Obstáculos:** Paredes ou barreiras que impedem a passagem.
-   **Regiões desconectadas:** Diferentes áreas livres
    separadas por barreiras.

O sistema deve "colorir" automaticamente todas as áreas
livres, facilitando o planejamento de rotas do robô.

------------------------------------------------------------------------

## Objetivo

Implementar o **Algoritmo Flood Fill** para identificar
automaticamente todas as regiões conectadas em um grid 2D,
considerando:

-   **Identificação:** Distinguir terreno navegável (`0`)
    de obstáculos (`1`).
-   **Segmentação:** Atribuir uma cor (número inteiro)
    diferente para cada nova região encontrada (ex: 2, 3, 4...)\[cite:
    29\].
-   **Automação:** O algoritmo deve varrer o grid em busca
    de células não visitadas para garantir que nenhuma região fique sem
    mapeamento.

------------------------------------------------------------------------

## Regras do Grid

O terreno é representado por uma **matriz n × m**, onde os
valores seguem a legenda:

-   `0`: **Terreno navegável** (Branco)
-   `1`: **Obstáculo** (Preto)
-   `2, 3, 4...`: **Regiões Mapeadas** pelo algoritmo.

### Movimentação

A região conectada utiliza apenas vizinhos ortogonais (cima, baixo,
esquerda, direita).\
Diagonais não são consideradas conexões diretas neste
projeto.

------------------------------------------------------------------------

## O Algoritmo Implementado

O projeto utiliza uma abordagem **Iterativa (BFS - Breadth-First
Search)** com `deque`.

### Por que BFS Iterativo?

Evita estouro de pilha em grids grandes e é mais eficiente
que a recursão tradicional.

### Lógica:

1.  Recebe coordenada inicial.
2.  Adiciona à fila e pinta se for `0`.
3.  Expande verificando 4 direções.
4.  Após completar uma região, busca novos `0` restantes, incrementando
    a cor.

------------------------------------------------------------------------

## Estrutura do Código

### `main.py`

-   **`flood_fill(grid, x, y, color)`**\
    Preenche uma região navegável.

-   **`fill_all_regions(grid, initial_x, initial_y)`**\
    Controla o processo global de mapeamento.

-   **`print_grid(grid)`**\
    Exibe a matriz no terminal.

-   **`teste()`**\
    Fornece um cenário pronto para demonstração.

------------------------------------------------------------------------

## Execução

### 1. Pré-requisitos

-   Python 3.6 ou superior.

### 2. Executar

``` bash
python main.py
```

------------------------------------------------------------------------

# Exemplo de Uso

Considerando o grid de teste configurado no arquivo **main.py**:

### Entrada:

Grid inicial com obstáculos e múltiplas regiões desconexas.\
Ponto de partida: **(0, 0)**.

    === GRID ORIGINAL ===
    0 0 1 0 0
    1 0 1 0 1
    0 0 0 1 0
    1 1 0 0 0

### Saída:

O algoritmo identifica **três regiões distintas**:

-   A região conectada ao início recebe a **cor 2**.
-   A região isolada no canto superior direito recebe **cor 3**.
-   A região isolada no canto inferior direito recebe **cor 4**.

```{=html}
<!-- -->
```
    === GRID PREENCHIDO ===
    2 2 1 3 3
    1 2 1 3 1
    2 2 2 1 4
    1 1 4 4 4

------------------------------------------------------------------------

# Critérios de Avaliação Atendidos

### ✔ Corretude

Respeita obstáculos e conexões válidas.

### ✔ Eficiência

Evita recursão profunda, usa BFS robusto.

### ✔ Visualização

Exibe claramente o grid antes e depois.

### ✔ Documentação

Explicação detalhada e exemplo funcional.

------------------------------------------------------------------------

# Autores

-   **Pedro Lucas Sousa e Silva**
-   **Gustavo Ceolin Silva Veloso**
-   **Henrique Pinto Santos**
-   **Pedro Araújo Franco**
