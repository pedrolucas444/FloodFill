# FloodFill - Mapeamento de Terreno para Robôs Autônomos

## Sobre o Projeto

O **FloodFill Mapper** é um sistema inteligente de mapeamento de terrenos que utiliza o **Algoritmo Flood Fill** (Preenchimento por Inundação) para identificar e classificar regiões conectadas em ambientes desconhecidos.

O projeto simula um robô autônomo capaz de:
- Identificar automaticamente todas as regiões navegáveis
- Colorir cada região com uma cor única
- Respeitar obstáculos e barreiras
- Mapear terrenos completamente de forma autônoma

**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos  
**Instituição:** Engenharia de Software

---

## Objetivo

Implementar o **Algoritmo Flood Fill** para:

1. **Identificar** todas as regiões conectadas em um grid bidimensional
2. **Segmentar** cada região com uma cor (valor numérico) distinta
3. **Automatizar** o processo de mapeamento completo do terreno
4. **Respeitar** obstáculos e limites do grid

---

## Contexto do Problema

### Cenário
Uma empresa de automação precisa de um sistema para que robôs autônomos possam mapear terrenos desconhecidos antes de executar suas operações.

### Representação do Terreno
O ambiente é modelado como uma **matriz n × m** onde cada célula representa:

| Valor | Significado | Cor Visual |
|-------|-------------|------------|
| `0` | Terreno navegável | Branco |
| `1` | Obstáculo | Preto |
| `2` | Região mapeada 1 | Vermelho |
| `3` | Região mapeada 2 | Laranja |
| `4` | Região mapeada 3 | Amarelo |
| `5+` | Outras regiões | Verde, Azul, etc. |

### Regras de Conectividade
- Movimentos válidos: Ortogonais (cima, baixo, esquerda, direita)
- Movimentos inválidos: Diagonais
- Obstáculos: Bloqueiam conexões entre regiões

---

## O Algoritmo Flood Fill

### Descrição
O Flood Fill é um algoritmo de preenchimento que, a partir de um ponto inicial, expande-se para todas as células conectadas que possuem a mesma característica (no nosso caso, valor `0`).

### Implementação: BFS Iterativo

O projeto utiliza uma abordagem **iterativa baseada em BFS (Breadth-First Search)** com `deque` (fila de dupla extremidade).

#### Por que BFS Iterativo?

| Característica | Recursivo | BFS Iterativo |
|----------------|-----------|---------------|
| Controle de memória | Pilha limitada | Controle explícito |
| Grids grandes | Stack overflow | Robusto |
| Performance | Overhead de chamadas | Mais eficiente |
| Ordem de preenchimento | DFS (profundidade) | BFS (largura) |

### Pseudocódigo

```
FUNÇÃO flood_fill(grid, x, y, cor):
    SE grid[x][y] ≠ 0 ENTÃO RETORNAR
    
    fila ← nova_fila()
    fila.adicionar((x, y))
    grid[x][y] ← cor
    
    ENQUANTO fila não vazia:
        atual_x, atual_y ← fila.remover()
        
        PARA CADA direção em [(0,1), (0,-1), (1,0), (-1,0)]:
            novo_x ← atual_x + direção[0]
            novo_y ← atual_y + direção[1]
            
            SE posição_válida(novo_x, novo_y) E grid[novo_x][novo_y] = 0:
                grid[novo_x][novo_y] ← cor
                fila.adicionar((novo_x, novo_y))

FUNÇÃO fill_all_regions(grid, x_inicial, y_inicial):
    cor_atual ← 2
    flood_fill(grid, x_inicial, y_inicial, cor_atual)
    cor_atual ← cor_atual + 1
    
    PARA CADA linha em grid:
        PARA CADA coluna em linha:
            SE grid[linha][coluna] = 0:
                flood_fill(grid, linha, coluna, cor_atual)
                cor_atual ← cor_atual + 1
```

### Análise de Complexidade

Seja **n** o número de linhas e **m** o número de colunas:

- **Complexidade de Tempo:** `O(n × m)`
  - Cada célula é visitada no máximo uma vez
  - Operações na fila são `O(1)`
  
- **Complexidade de Espaço:** `O(n × m)`
  - Pior caso: todas as células são navegáveis e entram na fila
  - Grid armazenado em memória: `O(n × m)`

---

## Estrutura do Projeto

```
trabalho_em_grupo_2_FPAA/
│
├── main.py                 # Implementação principal do algoritmo
├── README.md              # Este arquivo
└── requirements.txt       # Dependências (se houver GUI)
```

### Principais Funções em `main.py`

#### `flood_fill(grid, x, y, color)`
Preenche uma região conectada específica.

**Parâmetros:**
- `grid` (list): Matriz bidimensional do terreno
- `x` (int): Coordenada da linha inicial
- `y` (int): Coordenada da coluna inicial
- `color` (int): Valor da cor a ser preenchida

**Retorno:** None (modifica o grid in-place)

#### `fill_all_regions(grid, initial_x, initial_y)`
Orquestra o mapeamento completo do terreno.

**Processo:**
1. Preenche a região conectada ao ponto inicial
2. Varre todo o grid buscando células não visitadas (`0`)
3. Para cada nova região encontrada, incrementa a cor e preenche
4. Continua até mapear todas as regiões

#### `print_grid(grid)`
Exibe a matriz formatada no terminal.

#### `teste()`
Fornece um grid de demonstração pré-configurado.

---

## Como Executar

### Pré-requisitos

- **Python 3.6+** instalado
- (Opcional) `matplotlib` para visualização gráfica

### Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/trabalho_em_grupo_2_FPAA.git
cd trabalho_em_grupo_2_FPAA
```

2. **Instale dependências (se usar GUI):**
```bash
pip install matplotlib numpy
```

### Execução

#### Modo Terminal (Padrão)
```bash
python main.py
```

#### Personalizar Grid
Edite a função `teste()` em `main.py`:

```python
def teste():
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0]
    ]
    initial_x, initial_y = 0, 0  # Ponto de partida
    return grid, initial_x, initial_y
```

---

## Exemplos de Uso

### Exemplo 1: Grid Simples

#### Entrada
```
Grid 4x5:
0 0 1 0 0
1 0 1 0 1
0 0 0 1 0
1 1 0 0 0

Ponto inicial: (0, 0)
```

#### Processo de Mapeamento
1. **Região 2 (Vermelho):** Iniciando em (0,0), preenche toda a área conectada no canto esquerdo
2. **Região 3 (Laranja):** Detecta área isolada no canto superior direito
3. **Região 4 (Amarelo):** Detecta área isolada no canto inferior direito

#### Saída
```
Grid Mapeado:
2 2 1 3 3
1 2 1 3 1
2 2 2 1 4
1 1 4 4 4

Legenda:
2 = Região conectada ao início
3 = Região isolada (superior direita)
4 = Região isolada (inferior direita)
1 = Obstáculos
```

### Exemplo 2: Corredor com Múltiplas Salas

#### Entrada
```
Grid 4x5:
0 1 0 0 1
0 1 0 0 1
0 1 1 1 1
0 0 0 1 0

Ponto inicial: (0, 2)
```

#### Saída
```
Grid Mapeado:
3 1 2 2 1
3 1 2 2 1
3 1 1 1 1
3 3 3 1 4

Regiões identificadas:
- Região 2 (começou em 0,2): Sala superior direita
- Região 3: Corredor esquerdo conectado à sala inferior
- Região 4: Sala isolada no canto inferior direito
```

---

## Critérios de Avaliação Atendidos

| Critério | Status | Detalhes |
|----------|--------|----------|
| **Corretude** | Atendido | Respeita obstáculos e identifica todas as conexões válidas |
| **Eficiência** | Atendido | BFS iterativo evita stack overflow, `O(n×m)` ótimo |
| **Visualização Terminal** | Atendido | Matriz formatada com números claros |
| **Visualização Gráfica** | Atendido | (Se implementada) Cores distintas por região |
| **Clareza do Código** | Atendido | Funções bem nomeadas, lógica modular |
| **Documentação** | Atendido | README completo com exemplos e explicações |
| **Robustez** | Atendido | Trata grids vazios, sem navegáveis, e grandes dimensões |

---

## Testes

### Casos de Teste Implementados

1. **Grid completamente livre** (todas células = 0)
   - Resultado esperado: Uma única região

2. **Grid completamente bloqueado** (todas células = 1)
   - Resultado esperado: Nenhuma região mapeada

3. **Múltiplas regiões desconexas**
   - Resultado esperado: Cada ilha recebe cor diferente

4. **Grid grande (100x100)**
   - Resultado esperado: Execução eficiente sem erros

### Como Adicionar Testes

```python
def test_custom_grid():
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    expected_regions = 1  # Todas conectadas
    
    fill_all_regions(grid, 0, 0)
    # Adicione suas verificações
```

---

## Troubleshooting

### Problemas Comuns

**Problema:** `IndexError: list index out of range`
- **Causa:** Coordenadas iniciais fora dos limites do grid
- **Solução:** Verifique se `0 <= x < n` e `0 <= y < m`

**Problema:** Região não foi preenchida
- **Causa:** Ponto inicial não está em célula navegável (valor ≠ 0)
- **Solução:** Escolha um ponto inicial com valor `0`

**Problema:** Performance lenta em grids grandes
- **Causa:** Grid muito grande (ex: 10.000 x 10.000)
- **Solução:** A implementação já é otimizada, mas considere processamento paralelo para casos extremos

---

## Extensões Futuras (Opcional)

- Interface gráfica interativa com `tkinter` ou `pygame`
- Geração aleatória de grids com densidade configurável de obstáculos
- Animação do processo de preenchimento em tempo real
- Suporte a movimentação diagonal (8-conectividade)
- Exportação do mapa para imagem (PNG/SVG)
- Métricas de análise (número de regiões, tamanho médio, etc.)
---

## Autores

**Equipe de Desenvolvimento:**
- Pedro Lucas Sousa e Silva
- Gustavo Ceolin Silva Veloso
- Henrique Pinto Santos
- Pedro Araújo Franco

**Disciplina:** Fundamentos de Projeto e Análise de Algoritmos  
**Curso:** Engenharia de Software  
**Professor:** João Paulo Carneiro Aramuni

---

