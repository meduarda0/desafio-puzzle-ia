#IDS
from typing import Tuple, Optional
from puzzle import Puzzle

def busca_aprofundamento_iterativo(inicial: Puzzle, objetivo: Tuple[int], limite_max: int = 40) -> Tuple[Optional[Puzzle], int]:
    total_nos_expandidos = 0

    for limite in range(limite_max + 1):
        fronteira = [inicial]

        while fronteira:
            atual = fronteira.pop()
            total_nos_expandidos += 1

            if atual.estado == objetivo:
                return atual, total_nos_expandidos

            if atual.profundidade < limite:
                for vizinho in reversed(atual.gerar_sucessores()):
                    fronteira.append(vizinho)

    return None, total_nos_expandidos