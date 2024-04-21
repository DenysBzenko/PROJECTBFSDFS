# DMPROJECT

## Опис
Це репозиторій містить проект для реалізації алгоритмів пошуку в ширину (BFS) і пошуку в глибину (DFS) для графів, вони представлені списками суміжності та матрицями. Проект має 3 головних файлів: algorithm.py, main-5.py, randomMatrix.py. Вони демонструються побудову матриць і спички суміжності, та аналіз алгоритмів на цих даних. 

## Вміст файлів
- algorithmbfsdfs.py - Містить функції для BFS і DFS, що працюють як з матрицями суміжності, так і зі списками суміжності.
- main.py - Виконавчий файл, який імпортує алгоритми з algorithmbfsdfs.py та тестує їх на графах, згенерованих generateMatrix.py. Вимірює час виконання алгоритмів і виводить результати.
- generateMatrix.py - Генерує випадкові взважені графи з заданою кількістю вершин та щільністю.

### Типи даних:
- Для представлення графів використовуються матриці (numpy arrays) та списки суміжності.

### Функціональність:
- Розрахунок часу виконання з допомогою модуля time для оцінки ефективності алгоритмів.
- Використання deque для оптимізації роботи BFS.
