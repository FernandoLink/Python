import array as arr
import numpy as np

# É executado para armazenar de maneira eficiente e não é possível colocar tipos diferentes
# por isso é necessário passar o tipo
arr.array('d', [1, 3.5])

# Se você precisa de trabalho numérico é costume usar o numpy
numeros = np.array([1., 3.5])
print(numeros)
numeros = numeros + 3
print(numeros)