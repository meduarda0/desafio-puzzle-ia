from puzzle import Puzzle
from heuristicas.fora_do_lugar import heuristica_fora_do_lugar
from heuristicas.manhattan import heuristica_manhattan
from utils.timer import Temporizador
from utils.visualizer import mostrar_caminho

from algoritmos.largura import busca_em_largura
from algoritmos.profundidade import busca_em_profundidade
from algoritmos.aprofundamento import busca_aprofundamento_iterativo
from algoritmos.gulosa import busca_gulosa
from algoritmos.a_estrela import busca_a_estrela

def exibir_resultado(puzzle: Puzzle, timer: Temporizador):
    print("Ações:", puzzle.caminho())
    print("Número de passos: ", puzzle.profundidade)
    timer.imprimir_tempo()
    print("Caminho da solução: ")
    mostrar_caminho(puzzle)

# estado_inicial_3x3 = (1, 0, 3,
#                       5, 2, 6,
#                       4, 7, 8)
estado_inicial_3x3 = (1, 2, 3,
                      4, 5, 6,
                      0, 7, 8)
objetivo_3x3 = (1, 2, 3, 4, 5, 6, 7, 8, 0)
puzzle_3x3 = Puzzle(estado_inicial_3x3, 3)

estado_inicial_4x4 = (1, 2, 3, 4,
                      5, 6, 7, 8,
                      9, 10, 11, 12,
                      13, 0, 14, 15)
objetivo_4x4 = (1, 2, 3, 4,
                5, 6, 7, 8,
                9, 10, 11, 12,
                13, 14, 15, 0)
puzzle_4x4 = Puzzle(estado_inicial_4x4, 4)

# estado_inicial_5x5 = (1, 2, 3, 4, 5,
#                       6, 7, 8, 9, 10,
#                       11, 12, 13, 14, 15,
#                       16, 17, 18, 0, 19,
#                       20, 21, 22, 23, 24)
estado_inicial_5x5 = (1, 2, 3, 4, 5,
                      6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15,
                      16, 17, 18, 19, 20,
                      21, 22, 0, 23, 24)
objetivo_5x5 = (1, 2, 3, 4, 5,
                6, 7, 8, 9, 10,
                11, 12, 13, 14, 15,
                16, 17, 18, 19, 20,
                21, 22, 23, 24, 0)
puzzle_5x5 = Puzzle(estado_inicial_5x5, 5)

while True:
    print("\n--- MENU DE BUSCAS ---")
    print("1 - BFS (8 e 15 peças)")
    print("2 - DFS (8 e 15 peças)")
    print("3 - IDS (8 e 15 peças)")
    print("4 - Gulosa (8, 15 e 24 peças)")
    print("5 - A* (8, 15 e 24 peças)")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4)]:
            print(f"\n--- BFS - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            acoes, passos, nos_expandidos, solucao = busca_em_largura(puzzle, objetivo)
            timer.parar()

            if solucao:
                print("Nós expandidos: ", nos_expandidos)
                exibir_resultado(solucao, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "2":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4)]:
            print(f"\n--- DFS - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            resultado, nos_expandidos = busca_em_profundidade(puzzle, objetivo)
            timer.parar()

            if resultado:
                print("Nós expandidos: ", nos_expandidos)
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "3":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4)]:
            print(f"\n--- IDS - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            resultado, nos_expandidos = busca_aprofundamento_iterativo(puzzle, objetivo)
            timer.parar()

            if resultado:
                print("Nós expandidos: ", nos_expandidos)
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "4":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4), (puzzle_5x5, objetivo_5x5)]:
            print(f"\n--- Gulosa - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            resultado, nos_expandidos = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica_fora_do_lugar)
            timer.parar()

            if resultado:
                print("Nós expandidos: ", nos_expandidos)
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "5":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4), (puzzle_5x5, objetivo_5x5)]:
            print(f"\n--- A* - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            resultado, nos_expandidos = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica_manhattan)
            timer.parar()

            if resultado:
                print("Nós expandidos: ", nos_expandidos)
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")