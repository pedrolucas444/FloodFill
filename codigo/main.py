from collections import deque

def flood_fill(grid, start_x, start_y, color):
    """Executa o flood fill BFS a partir de (start_x, start_y) preenchendo com 'color'."""
    n = len(grid)
    m = len(grid[0])

    # Só preenche se a célula inicial for navegável
    if grid[start_x][start_y] != 0:
        return False  # Nada foi preenchido

    queue = deque()
    queue.append((start_x, start_y))
    grid[start_x][start_y] = color

    # Movimentos ortogonais
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            # Verifica limites
            if 0 <= nx < n and 0 <= ny < m:
                # Só preenche células navegáveis (0)
                if grid[nx][ny] == 0:
                    grid[nx][ny] = color
                    queue.append((nx, ny))

    return True  # Região foi preenchida

def fill_all_regions(grid, initial_x, initial_y):
    n = len(grid)
    m = len(grid[0])

    color = 2  # Primeira cor disponível

    # Primeiro: preencher a região inicial
    if flood_fill(grid, initial_x, initial_y, color):
        color += 1

    # Agora: preencher automaticamente TODAS as outras regiões com 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:  # Achou outra região livre
                if flood_fill(grid, i, j, color):
                    color += 1

    return grid


# Testes e visualização

def print_grid(grid):
    for linha in grid:
        print(" ".join(str(x) for x in linha))
    print()  # linha em branco


def teste():
    # Grid de exemplo para testar
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0]
    ]

    start_x, start_y = 0, 0  # ponto inicial do preenchimento

    print("=== GRID ORIGINAL ===")
    print_grid(grid)

    resultado = fill_all_regions(grid, start_x, start_y)

    print("=== GRID PREENCHIDO ===")
    print_grid(resultado)


# Executa o teste automaticamente quando rodar o arquivo
teste()