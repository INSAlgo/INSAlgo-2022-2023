# Cours Libraries
[slides](Cours 8 - Python Libraries.pdf)

## Exercices

### Level 1

- [Learn to use counter](https://www.hackerrank.com/challenges/collections-counter/problem) : [Solution](counter.py)
- [Letter case permutation](https://leetcode.com/problems/letter-case-permutation/) (à faire avec itertools) : [Solution](letter_case_permutation.py)
- [Battledev nov 2020 Ex 1](https://www.isograd-testingservices.com/FR/solutions-challenges-de-code?cts_id=70) (à faire avec re) : [Solution](bd-11-2020-Ex1.py)
- [Alternating Characters](https://www.hackerrank.com/challenges/alternating-characters/problem) (à faire avec re) : [Solution](alternating_characters.py)

### Level 2

- [Most Frequent Subtree Sum](https://leetcode.com/problems/most-frequent-subtree-sum/) : [Solution](most_frequent_subtree_sum.py)
- [AOC 21 Day 03](https://adventofcode.com/2021/day/3) : [Solution](AOC21_03.py)

### Level 3

- [AOC 21 Day 14](https://adventofcode.com/2021/day/14) : [Solution](AOC21_14.py)

</br>

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
