##Simulación de la Máquina de Galton
##Se deben importar librerias desde consola simbolo de sistema

import random
import matplotlib.pyplot as plt
import seaborn as sns

def simular_maquina_galton(num_canicas, num_niveles):
    resultados = [0] * num_niveles

    for _ in range(num_canicas):
        posicion = num_niveles // 2  # Comenzamos en el nivel central
        for _ in range(num_niveles):
            # Decidir si la canica cae a la izquierda (0) o derecha (1)
            lado = random.randint(0, 1)
            if lado == 0:
                posicion -= 1
            else:
                posicion += 1

            # Asegurarnos de que la posición esté dentro de los niveles
            posicion = max(0, min(posicion, num_niveles - 1))

        # Contar la canica en la posición final
        resultados[posicion] += 1

    return resultados

##En este cuadro de codigo se define las caracteristicas que queremos se muestre en el grafico



def graficar_histograma(resultados):

    plt.figure(figsize=(9, 5)) ##Tamaño del grafico que se imprime en pantalla    
    
    sns.barplot(x=list(range(1, len(resultados) + 1)), y=resultados, color='red') ##color de las barras del grafico
    
    plt.title('Simulación de Máquina de Galton') ##Titulo del grafico
    
    plt.xlabel('Contenedor') ##Niveles(12)
    
    plt.ylabel('Cantidad de Canicas') ##Cantidad de canicas (3000)   
    
    plt.show() ##Muestra la grafica generada

# Simulación con 3000 canicas y 12 niveles

num_canicas = 3000
num_niveles = 12
resultados = simular_maquina_galton(num_canicas, num_niveles)
graficar_histograma(resultados)
