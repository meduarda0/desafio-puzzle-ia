#DFS
from time import time
from puzzle import Puzzle
from typing import Tuple, Optional


def busca_em_profundidade(
    inicial: Puzzle,
    objetivo: Tuple[int],
    tempo_maximo: int = 10,
    limite: int = 10
) -> Tuple[Optional[Puzzle], int]:
    
    inicio = time()
    fronteira = [inicial]
    visitados = set()
    nos_expandidos = 0

    while fronteira:
        if time() - inicio > tempo_maximo:
            raise TimeoutError("Tempo limite atingido.")

        atual = fronteira.pop()

        if atual in visitados:
            continue

        visitados.add(atual)
        nos_expandidos += 1

        if atual.estado == objetivo:
            return atual, nos_expandidos

        if atual.profundidade < limite:
            for vizinho in reversed(atual.gerar_sucessores()):
                if vizinho not in visitados:
                    fronteira.append(vizinho)

    return None, nos_expandidos


""" Busca em profundidade (DFS) com limite de tempo e profundidade.
    
    Parâmetros:
    - inicial: estado inicial do puzzle
    - objetivo: estado final desejado
    - tempo_maximo: tempo limite de execução (em segundos)
    - limite: profundidade máxima permitida
    
    Retorna:
    - caminho: lista de ações até o objetivo
    - passos: número de movimentos
    - nos_expandidos: quantos nós foram visitados """