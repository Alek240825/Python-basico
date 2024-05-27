listaA = []
for _ in range(10):
    numero = float(input("Ingresa un número para la lista A: "))
    listaA.append(numero)
listaB = []
for _ in range(10):
    numero = float(input("Ingresa un número para la lista B: "))
    listaB.append(numero)

listaC = []

for i in range(len(listaA)):
    resultado = listaA[i] * listaB[-(i + 1)]
    listaC.append(resultado)
    
print("Resultado de la multiplicación:")
print(listaC)

matrix = [['0'] * 5 for _ in range(5)]

for i in range(5):
    matrix[0][i] = 'x'
    matrix[4][i] = 'x'

matrix[1][1] = 'x'
matrix[2][2] = 'x'
matrix[3][3] = 'x'

for fila in matrix:
    print(fila)
