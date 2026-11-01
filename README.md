# Desafio Puzzle IA

Projeto desenvolvido para implementar e comparar diferentes algoritmos de busca aplicados à resolução do problema do Sliding Puzzle. A aplicação permite resolver configurações de 8, 15 e 24 peças utilizando algoritmos de busca sem informação e busca informada.

## Algoritmos implementados

### Buscas sem informação

- Busca em Largura (BFS)
- Busca em Profundidade (DFS)
- Busca de Aprofundamento Iterativo (IDS)

### Buscas informadas

- Busca Gulosa
- Busca A*

## Heurísticas

O projeto utiliza diferentes heurísticas para orientar as buscas informadas:
- Peças fora do lugar
- Distância de Manhattan

## Funcionamento

O problema é representado por uma classe responsável por armazenar o estado do puzzle e gerar os possíveis sucessores a partir do movimento do espaço vazio. A aplicação disponibiliza um menu para selecionar o algoritmo de busca. Para cada execução, são apresentadas informações como:
- Sequência de ações para a solução
- Número de passos
- Número de nós expandidos
- Tempo de execução
- Caminho da solução

As buscas em largura, profundidade e aprofundamento iterativo são executadas para os puzzles de 8 e 15 peças. As buscas Gulosa e A* também incluem o puzzle de 24 peças.

## Estrutura do projeto

```text
desafio-puzzle-ia/
│
├── algoritmos/
│   ├── largura.py
│   ├── profundidade.py
│   ├── aprofundamento.py
│   ├── gulosa.py
│   └── a_estrela.py
│
├── heuristicas/
│   ├── fora_do_lugar.py
│   └── manhattan.py
│
├── utils/
│   ├── tempo.py
│   └── visualizar.py
│
├── puzzle.py
└── main.py
```

## Tecnologias utilizadas

- Python

## Como executar

Clone o repositório:

```bash
git clone https://github.com/meduarda0/desafio-puzzle-ia.git
```

Acesse a pasta do projeto:

```bash
cd desafio-puzzle-ia
```

Execute o arquivo principal:

```bash
python main.py
```

Em seguida, selecione no menu o algoritmo que deseja executar.

## Objetivo

Projeto desenvolvido com finalidade acadêmica para estudar algoritmos de busca e estratégias heurísticas aplicadas à resolução de problemas em Inteligência Artificial.
