#IDS
from typing import List, Tuple, Optional
from puzzle import Puzzle

def busca_aprofundamento_iterativo(inicial: Puzzle, objetivo: Tuple[int], limite_max: int = 10) -> Tuple[List[str], int, int, Optional[Puzzle]]:
    total_nos_expandidos = 0
    for limite in range(limite_max + 1):
        fronteira = [inicial]

        while fronteira:
            atual = fronteira.pop()
            total_nos_expandidos += 1

            if atual.estado == objetivo:
                return atual.caminho(), atual.profundidade, total_nos_expandidos, atual

            if atual.profundidade < limite:
                for vizinho in reversed(atual.gerar_sucessores()):
                    fronteira.append(vizinho)

    return [], 0, total_nos_expandidos, None