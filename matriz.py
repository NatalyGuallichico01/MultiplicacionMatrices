#MULTIPLICACION DE MATRICES
print ("/tMultiplicacion de matrices")
matriz1=[[0,0,0],[0,0,0],[0,0,0]]
matriz2=[[0,0,0],[0,0,0],[0,0,0]]
matrizResult=[[0,0,0],[0,0,0],[0,0,0]]
matrizInversa=[[0,0,0],[0,0,0],[0,0,0]]

matriz1 [0][0]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [0][1]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [0][2]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [1][0]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [1][1]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [1][2]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [2][0]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [2][1]=int (input("Ingrese elemento de la primera matriz: "))
matriz1 [2][2]=int (input("Ingrese elemento de la primera matriz: "))
print()
print("Su primera matriz es ")
print ()
for i in range (3):
	print(matriz1[i])
print ()

#SEGUNDA MATRIZ
matriz2 [0][0]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [0][1]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [0][2]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [1][0]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [1][1]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [1][2]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [2][0]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [2][1]=int (input("Ingrese elemento de la segunda matriz: "))
matriz2 [2][2]=int (input("Ingrese elemento de la segunda matriz: "))
print ()
print("Su segunda matriz es ")
print ()
for i in range (3):
	print(matriz2[i])

#MATRIZ RESULTANTE
matrizResult[0][0]=((matriz1[0][0]*matriz2[0][0])+(matriz1[0][1]*matriz2[1][0])+(matriz1[0][2]*matriz2[2][0]))
matrizResult[0][1]=((matriz1[0][0]*matriz2[0][1])+(matriz1[0][1]*matriz2[1][1])+(matriz1[0][2]*matriz2[2][1]))
matrizResult[0][2]=((matriz1[0][0]*matriz2[0][2])+(matriz1[0][1]*matriz2[1][2])+(matriz1[0][2]*matriz2[2][2]))
matrizResult[1][0]=((matriz1[1][0]*matriz2[0][0])+(matriz1[1][1]*matriz2[1][0])+(matriz1[1][2]*matriz2[2][0]))
matrizResult[1][1]=((matriz1[1][0]*matriz2[0][1])+(matriz1[1][1]*matriz2[1][1])+(matriz1[1][2]*matriz2[2][1]))
matrizResult[1][2]=((matriz1[1][0]*matriz2[0][2])+(matriz1[1][1]*matriz2[1][2])+(matriz1[1][2]*matriz2[2][2]))
matrizResult[2][0]=((matriz1[2][0]*matriz2[0][0])+(matriz1[2][1]*matriz2[1][0])+(matriz1[2][2]*matriz2[2][0]))
matrizResult[2][1]=((matriz1[2][0]*matriz2[0][1])+(matriz1[2][1]*matriz2[1][1])+(matriz1[2][2]*matriz2[2][1]))
matrizResult[2][2]=((matriz1[2][0]*matriz2[0][2])+(matriz1[2][1]*matriz2[1][2])+(matriz1[2][2]*matriz2[2][2]))
print ()
print("El resultado de las 2 matrices multiplicadas es: ")
print ()
for i in range (3):
	print(matrizResult[i])

#MATRIZ INVERSA
print()
print("Matriz inversa")
print ()
matrizInversa[0][0]=(1/matrizResult[0][0])
matrizInversa[0][1]=(1/matrizResult[0][1])
matrizInversa[0][2]=(1/matrizResult[0][2])
matrizInversa[1][0]=(1/matrizResult[1][0])
matrizInversa[1][1]=(1/matrizResult[1][1])
matrizInversa[1][2]=(1/matrizResult[1][2])
matrizInversa[2][0]=(1/matrizResult[2][0])
matrizInversa[2][1]=(1/matrizResult[2][1])
matrizInversa[2][2]=(1/matrizResult[2][2])

for i in range (3):
	print (matrizInversa[i])
