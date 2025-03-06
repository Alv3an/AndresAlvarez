import numpy as np
import matplotlib.pyplot as plt

# Se Define la función real ln(x)
def ln_x(x):
    return np.log(x)

# Se Define la aproximación de la serie de Taylor de ln(x) en x=1 hasta el término cúbico
def taylor_ln_x(x):
    return (x - 1) - (x - 1)**2 / 2 + (x - 1)**3 / 3

# Rango de valores de x
x = np.linspace(0.1, 2, 400)  # Evitamos x=0 por la singularidad de ln(x)
y_ln = ln_x(x)
y_taylor = taylor_ln_x(x)

# Se Grafica
plt.figure(figsize=(8, 5))
plt.plot(x, y_ln, label=r'$\ln(x)$', color='blue', linewidth=2)
plt.plot(x, y_taylor, label=r'Aprox. Taylor ($3^\text{er}$ orden)', color='red', linestyle='dashed', linewidth=2)
plt.axvline(x=1, color='gray', linestyle='dotted', linewidth=1)  # Línea en x=1 (punto de expansión)
plt.axhline(y=0, color='black', linewidth=1)  # Eje x
plt.axvline(x=0, color='black', linewidth=1)  # Eje y

# Etiquetas y leyenda
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Aproximación de Taylor de ln(x) en x=1')
plt.legend()
plt.grid(True)
plt.show()