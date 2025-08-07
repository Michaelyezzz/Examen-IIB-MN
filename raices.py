import numpy as np
from scipy import optimize

def f(x):
    return x**5 + 5.5*x**4 + 4.5*x**3 - 9.5*x**2 - 15.5*x - 6

xs = np.linspace(-20, 20, 4001)
signs = np.sign(f(xs))
brackets = []
for i in range(len(xs)-1):
    if signs[i] == 0:
        brackets.append((xs[i], xs[i]))
    elif signs[i]*signs[i+1] < 0:
        brackets.append((xs[i], xs[i+1]))
brackets = sorted(set(brackets), key=lambda b: (b[0], b[1]))

roots = []
for a, b in brackets:
    if a == b:
        roots.append(a)
    else:
        sol = optimize.root_scalar(f, bracket=[a, b], method='bisect', xtol=1e-8)
        roots.append(sol.root)
        
unique_roots = np.unique(np.round(roots, 8))
print("Raíces reales (bisección):", unique_roots)


