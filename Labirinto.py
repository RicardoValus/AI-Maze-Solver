from collections import deque

class Labirinto:
    def __init__(self, labirinto):
        # Inicializa o labirinto e calcula o número de linhas e colunas.
        self.labirinto = labirinto
        self.linhas = len(labirinto)
        self.colunas = len(labirinto[0])

    def is_valido(self, linha, coluna):
        # Verifica se uma posição é válida (não é uma parede e está dentro dos limites).
        return 0 <= linha < self.linhas and 0 <= coluna < self.colunas and self.labirinto[linha][coluna] != '#'

    def busca_largura(self, inicio, fim):
        # Executa a busca em largura para encontrar um caminho do início ao fim.
        fila = deque([(inicio, [inicio])])  # Inicializa a fila com a posição inicial.
        visitado = set([inicio])  # Mantém o controle das posições visitadas.

        while fila:
            # Itera sobre a fila de posições para explorar.
            (linha, coluna), caminho = fila.popleft()

            if (linha, coluna) == fim:
                # Se a posição atual é o destino, retorna o caminho encontrado.
                return caminho

            for dl, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                # Explora as posições vizinhas válidas.
                nova_linha, nova_coluna = linha + dl, coluna + dc

                if self.is_valido(nova_linha, nova_coluna) and (nova_linha, nova_coluna) not in visitado:
                    # Se a posição vizinha é válida e não foi visitada, adiciona à fila para explorar.
                    fila.append(((nova_linha, nova_coluna), caminho + [(nova_linha, nova_coluna)]))
                    visitado.add((nova_linha, nova_coluna))

        # Retorna None se não houver caminho válido.
        return None

# Definição do labirinto e busca de caminho.
labirinto = [
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.'],
    ['#', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '.']
]

lab = Labirinto(labirinto)
inicio = (3, 1)
fim = (1, 2)
caminho = lab.busca_largura(inicio, fim)

if caminho:
    # Se um caminho foi encontrado, imprime as posições do caminho.
    print("Caminho encontrado:")
    for linha, coluna in caminho:
        print(f'({linha}, {coluna})', end=" -> ")
else:
    # Caso contrário, imprime que não há caminho.
    print("Não há caminho para sair do labirinto!")
