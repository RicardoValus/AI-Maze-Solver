from collections import deque

class Labirinto:
    def __init__(self, labirinto):
        self.labirinto = labirinto
        self.linhas = len(labirinto)
        self.colunas = len(labirinto[0])

    def is_valido(self, linha, coluna):
        return 0 <= linha < self.linhas and 0 <= coluna < self.colunas and self.labirinto[linha][coluna] != '#'

    def busca_largura(self, inicio, fim):
        fila = deque([(inicio, [inicio])])
        visitado = set([inicio])

        while fila:
            (linha, coluna), caminho = fila.popleft()

            if (linha, coluna) == fim:
                return caminho

            for dl, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nova_linha, nova_coluna = linha + dl, coluna + dc

                if self.is_valido(nova_linha, nova_coluna) and (nova_linha, nova_coluna) not in visitado:
                    fila.append(((nova_linha, nova_coluna), caminho + [(nova_linha, nova_coluna)]))
                    visitado.add((nova_linha, nova_coluna))

        return None

labirinto = [
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.'],
    ['#', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '.']
]

lab = Labirinto(labirinto)
inicio = (0, 0)
fim = (4, 4)
caminho = lab.busca_largura(inicio, fim)

if caminho:
    print("Caminho encontrado:")
    for linha, coluna in caminho:
        print(f'({linha}, {coluna})', end=" -> ")
else:
    print("Não há caminho para sair do labirinto!")
