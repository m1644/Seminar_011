'''Задача:
Дана функция f(x) = 5x^2 + 10x - 30
1. Определить корни
2. Найти интервалы, на которых функция возрастает (ответ: от -35 до +oo)
3. Найти интервалы, на которых функция убывает (ответ: от -oo до -35)
4. Построить график
5. Вычислить вершину
6. Определить промежутки, на котором f > 0 
7. Определить промежутки, на котором f < 0 
'''

from sympy import *
from sympy.solvers import solve
from sympy.plotting import plot
from sympy.calculus.util import minimum, maximum

x = Symbol('x')
f = 5 * x**2 + 10*x - 30

plot(f, (x, -5, 5))
solution = solve(f, x)
print(solution)
interv_min = Interval(float(solution[1]), float(solution[0]))
print(interv_min)
res_min = minimum(f, x, interv_min)
print(res_min)
interv_max = Interval(float(solution[1]), float(solution[0]))
print(interv_max)
res_max = maximum(f, x, interv_max)
print(res_max)
