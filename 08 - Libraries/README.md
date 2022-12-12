# Cours Libraries
[Slides](https://github.com/INSAlgo/INSAlgo-2022-2023/blob/main/08%20-%20Libraries/Cours%208%20-%20Python%20Libraries.pdf)</br>
Découverte et explication sur les librairies python utiles.
## Exercices
### Level 1
- [Learn to use counter](https://www.hackerrank.com/challenges/collections-counter/problem)
- [Letter case permutation](https://leetcode.com/problems/letter-case-permutation/) (à faire avec itertools)
- [Battledev nov 2020 Ex 1](https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=70) (à faire avec re)
- [Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters/problem) (à faire avec re)
### Level 2
- [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/)
- [AOC 21 Day 03](https://adventofcode.com/2021/day/3)
### Level 3
- [AOC 21 Day 14](https://adventofcode.com/2021/day/14)
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