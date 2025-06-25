from collections import deque
from typing import List, Tuple
from puzzle import Puzzle

def busca_em_largura(inicial: Puzzle, objetivo: Tuple[int]) -> Tuple[List[str], int, int]:
    fronteira = deque([inicial])  # fila FIFO
    visitados = set()
    nos_expandidos = 0

    while fronteira:
        atual = fronteira.popleft()
        visitados.add(atual)
        nos_expandidos += 1

        if atual.estado == objetivo:
            return atual.caminho(), atual.profundidade, nos_expandidos

        for vizinho in atual.gerar_sucessores():
            if vizinho not in visitados and vizinho not in fronteira:
                fronteira.append(vizinho)

    return [], 0, nos_expandidos 