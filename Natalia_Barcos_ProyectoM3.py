import numpy as np
import matplotlib.pyplot as plt

def simular_maquina_galton(num_canicas, num_niveles):
    # Inicializamos los contenedores con 0 canicas
    contenedores = [0] * (num_niveles + 1)

    for _ in range(num_canicas):
        posicion = num_niveles // 2  # Comenzamos en el nivel medio
        for _ in range(num_niveles):
            # Elegimos aleatoriamente si la canica va a la izquierda o derecha
            if np.random.rand() < 0.5:
                posicion -= 1
            else:
                posicion += 1
        # Aseguramos que la posición esté dentro de los límites
        posicion = max(0, min(posicion, num_niveles))
        contenedores[posicion] += 1

    return contenedores

def graficar_histograma(contenedores):
    X = np.arange(-((len(contenedores) // 2) - 0.5), (len(contenedores) // 2) + 0.5)
    plt.xlabel('Contenedor')
    plt.ylabel('Cantidad de canicas')
    plt.title('Simulación de Máquina de Galton')
    plt.bar(X, contenedores, width=0.90, color="green")
    plt.show()

if __name__ == "__main__":
    num_canicas = 3000
    num_niveles = 12

    resultados = simular_maquina_galton(num_canicas, num_niveles)
    graficar_histograma(resultados)
