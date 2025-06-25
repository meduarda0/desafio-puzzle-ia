from puzzle import Puzzle
from heuristicas.fora_do_lugar import heuristica_fora_do_lugar
from heuristicas.manhattan import heuristica_manhattan
from utils.embaralhador import gerar_estado_aleatorio_resolvido
from utils.timer import Temporizador
from utils.visualizer import mostrar_caminho

from algoritmos.largura import busca_em_largura
from algoritmos.profundidade import busca_em_profundidade
from algoritmos.aprofundamento import busca_aprofundamento_iterativo
from algoritmos.gulosa import busca_gulosa
from algoritmos.a_estrela import busca_a_estrela


def exibir_resultado(puzzle: Puzzle, timer: Temporizador):
    print("Ações:", puzzle.caminho())
    print("Número de passos:", puzzle.profundidade)
    timer.imprimir_tempo()
    print("Caminho da solução:")
    mostrar_caminho(puzzle)

# Estados iniciais e objetivos
estado_3x3 = gerar_estado_aleatorio_resolvido(3)
puzzle_3x3 = Puzzle(estado_3x3, 3)
objetivo_3x3 = (1, 2, 3, 4, 5, 6, 7, 8, 0)

estado_4x4 = gerar_estado_aleatorio_resolvido(4)
puzzle_4x4 = Puzzle(estado_4x4, 4)
objetivo_4x4 = (1, 2, 3, 4,
                5, 6, 7, 8,
                9, 10, 11, 12,
                13, 14, 15, 0)

estado_5x5 = gerar_estado_aleatorio_resolvido(5)
puzzle_5x5 = Puzzle(estado_5x5, 5)
objetivo_5x5 = (1, 2, 3, 4, 5,
                6, 7, 8, 9, 10,
                11, 12, 13, 14, 15,
                16, 17, 18, 19, 20,
                21, 22, 23, 24, 0)


# Menu principal
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
            acoes, passos, nos, solucao = busca_em_largura(puzzle, objetivo)
            timer.parar()

            if solucao:
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
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")


    elif opcao == "4":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4), (puzzle_5x5, objetivo_5x5)]:
            print(f"\n--- Gulosa - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica_fora_do_lugar)
            timer.parar()

            if resultado:
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "5":
        for puzzle, objetivo in [(puzzle_3x3, objetivo_3x3), (puzzle_4x4, objetivo_4x4), (puzzle_5x5, objetivo_5x5)]:
            print(f"\n--- A* - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
            timer = Temporizador()
            timer.iniciar()
            resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica_manhattan)
            timer.parar()

            if resultado:
                exibir_resultado(resultado, timer)
            else:
                print("Nenhuma solução encontrada.")

    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")


# from puzzle import Puzzle
# from heuristicas.fora_do_lugar import heuristica_fora_do_lugar
# from heuristicas.manhattan import heuristica_manhattan
# from utils.embaralhador import gerar_estado_aleatorio_resolvido
# from utils.timer import Temporizador
# from utils.visualizer import mostrar_caminho

# from algoritmos.largura import busca_em_largura
# from algoritmos.profundidade import busca_em_profundidade
# from algoritmos.aprofundamento import busca_aprofundamento_iterativo
# from algoritmos.gulosa import busca_gulosa
# from algoritmos.a_estrela import busca_a_estrela

# def executar_busca(algoritmo, puzzles, objetivos, heuristica=None):
#     for puzzle, objetivo in zip(puzzles, objetivos):
#         print(f"\n--- {algoritmo.upper()} - {puzzle.tamanho * puzzle.tamanho - 1} peças ---")
#         timer = Temporizador()
#         timer.iniciar()

#         if algoritmo == "bfs":
#             acoes, passos, nos = busca_em_largura(puzzle, objetivo)
#             timer.parar()
#             print("Ações:", acoes)
#             print("Passos:", passos)
#             print("Nós expandidos:", nos)

#         elif algoritmo == "dfs":
#             acoes, passos, nos = busca_em_profundidade(puzzle, objetivo)
#             timer.parar()
#             print("Ações:", acoes)
#             print("Passos:", passos)
#             print("Nós expandidos:", nos)

#         elif algoritmo == "ids":
#             caminho, profundidade, nos, solucao = busca_aprofundamento_iterativo(puzzle, objetivo)
#             timer.parar()
#             if solucao:
#                 print("Movimentos:", caminho)
#                 print("Profundidade:", profundidade)
#                 print("Nós expandidos:", nos)
#                 mostrar_caminho(solucao)
#             else:
#                 print("Nenhuma solução encontrada.")

#         elif algoritmo == "gulosa":
#             resultado = busca_gulosa(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
#             timer.parar()
#             if resultado:
#                 print("Movimentos:", resultado.caminho())
#                 print("Profundidade:", resultado.profundidade)
#                 mostrar_caminho(resultado)
#             else:
#                 print("Nenhuma solução encontrada com busca gulosa.")

#         elif algoritmo == "astar":
#             resultado = busca_a_estrela(puzzle.estado, puzzle.tamanho, objetivo, heuristica)
#             timer.parar()
#             if resultado:
#                 print("Movimentos:", resultado.caminho())
#                 print("Profundidade:", resultado.profundidade)
#                 mostrar_caminho(resultado)
#             else:
#                 print("Nenhuma solução encontrada com A*.")

#         else:
#             print("Opção inválida.")

#         timer.imprimir_tempo()


# # Estados iniciais e objetivos
# estado_3x3 = gerar_estado_aleatorio_resolvido(3)
# puzzle_3x3 = Puzzle(estado_3x3, 3)
# objetivo_3x3 = (1, 2, 3, 
#                 4, 5, 6, 
#                 7, 8, 0)

# estado_4x4 = gerar_estado_aleatorio_resolvido(4)
# puzzle_4x4 = Puzzle(estado_4x4, 4)
# objetivo_4x4 = (1, 2, 3, 4,
#                 5, 6, 7, 8,
#                 9, 10, 11, 12,
#                 13, 14, 15, 0)

# estado_5x5 = gerar_estado_aleatorio_resolvido(5)
# puzzle_5x5 = Puzzle(estado_5x5, 5)
# objetivo_5x5 = (1, 2, 3, 4, 5,
#                 6, 7, 8, 9, 10,
#                 11, 12, 13, 14, 15,
#                 16, 17, 18, 19, 20,
#                 21, 22, 23, 24, 0)


# # Menu principal
# while True:
#     print("\n--- MENU DE BUSCAS ---")
#     print("1 - BFS/LARGURA  (8 e 15 peças)")
#     print("2 - DFS/PROFUNDIDADE (8 e 15 peças)")
#     print("3 - IDS/PROFUNDIDADE ITERATIVA (8 e 15 peças)")
#     print("4 - Gulosa (8, 15 e 24 peças)")
#     print("5 - A* (8, 15 e 24 peças)")
#     print("0 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         executar_busca("bfs", [puzzle_3x3, puzzle_4x4], [objetivo_3x3, objetivo_4x4])
#     elif opcao == "2":
#         executar_busca("dfs", [puzzle_3x3, puzzle_4x4], [objetivo_3x3, objetivo_4x4])
#     elif opcao == "3":
#         executar_busca("ids", [puzzle_3x3, puzzle_4x4], [objetivo_3x3, objetivo_4x4])
#     elif opcao == "4":
#         executar_busca("gulosa", [puzzle_3x3, puzzle_4x4, puzzle_5x5], [objetivo_3x3, objetivo_4x4, objetivo_5x5], heuristica_fora_do_lugar)
#     elif opcao == "5":
#         executar_busca("astar", [puzzle_3x3, puzzle_4x4, puzzle_5x5], [objetivo_3x3, objetivo_4x4, objetivo_5x5], heuristica_manhattan)
#     elif opcao == "0":
#         print("Encerrando...")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")