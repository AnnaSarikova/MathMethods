from scipy.optimize import linprog
from sympy import plot_implicit, symbols, And, Eq

# Минимализация

#F(x1, x2) = 1/4x1 + x2 → min
# A: x1 + 3x2>= 6,
# B: 4x1 + x2>= 8,
# C: 3x1+2x2>=11,
# x1>=0, x2>=0.
# Задание системы координат

obj = [1/4, 2]
#      ─┬  ─┬
#       │   └┤ Коэффициент для x2
#       └────┤ Коэффициент для x1

lhs_ineq = [[ -1,  -3],  # левая сторона красного неравенства
            [ -4,  -2],  # левая сторона синего неравенства
            [ -3,  -2]]  # левая сторона желтого неравенства

rhs_ineq = [-6,  # правая сторона красного неравенства
            -8,  # правая сторона синего неравенства
            -11]  # правая сторона желтого неравенства

# Если чтото будет =, то код ниже:
#lhs_eq = [[-1, 5]]  # левая сторона зеленого равенства
#rhs_eq = [15]       # правая сторона зеленого равенства

bnd = [(0, float("inf")),  # Границы x1
       (0, float("inf"))]  # Границы x2

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
              method="revised simplex")

#print(opt)
print(f'Ответ. M∗({opt.x[1]}; {opt.x[0]}); Fmin = F(M∗) = {opt.fun}.')

# Рисуем графики

x1, x2 = symbols('x1 x2')
p1 = plot_implicit(And(x1 + 3*x2>= 6,
                       4*x1 + x2>= 8,
                       3*x1 + 2*x2>=11,
                       x1>=0,
                       x2>=0),
                   x_var=(x1, -20, 20), y_var=(x2, -10, 10), line_color='yellow',
                   markers=[{'args': [opt.x[0], opt.x[1]], 'color': "blue", 'marker': "o", 'ms': 5}],
                   annotations=[{'xy': [opt.x[0], opt.x[1]], 'text': f'  M*{opt.x[0], opt.x[1]}', 'ha': 'left', 'va': 'top', 'color': 'blue'}],
                   show=False

              )

#Строим линии
p2 = plot_implicit(Eq(x1 + 3*x2, 6), (x1, -20, 20), (x2, -10, 10), show=False)
p3 = plot_implicit(Eq(4*x1 + x2, 8), (x1, -20, 20), (x2, -10, 10), show=False)
p4 = plot_implicit(Eq(3*x1 - 2*x2, 11), (x1, -20, 20), (x2, -10, 10), show=False)
p5 = plot_implicit(Eq(x1, 0), (x1, -20, 20), (x2, -10, 10), show=False)
p6 = plot_implicit(Eq(x2, 0), (x1, -20, 20), (x2, -10, 10), show=False)

#Добавляем графики все в одного
p1.append(p2[0])
p1.append(p3[0])
p1.append(p4[0])
p1.append(p5[0])
p1.append(p6[0])
p1.show()