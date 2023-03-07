# Parcours de graphes
[Slides](https://github.com/INSAlgo/INSAlgo-2022-2023/blob/f3b9b7cdc2f97a130284eb63f406bba33cd8904f/11%20-%20Parcours%20de%20graphes/Cours%2011%20-%20BFS_DFS.pdf)</br>
Breadth First Search et Depth First Search
## Exercices
### Level 1
- [Maximum depth of binary tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [BattleDev Nov 2020 - 3](https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=70#)
### Level 2
- [Path Sum](https://leetcode.com/problems/path-sum/)
- [Path Sum II](https://leetcode.com/problems/path-sum-ii/)
### Level 3
- [Path Sum III](https://leetcode.com/problems/path-sum-iii/)
- [AOC21 day 12](https://adventofcode.com/2021/day/12)
### Commentaires
Les exos AOC (Advent Of Code) Nécessitent de lire un fichier texte au lieu de l'input, voici une fonction qui prend le nom du fichier texte et renvoi une liste de strings correspondant aux lignes d'input :
```python
def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    print(lines)
    return lines
```