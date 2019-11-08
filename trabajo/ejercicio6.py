#Input
lado1=float(input("Ingrese lado1:"))
lado2=float(input("Ingrese lado2:"))
lado3=float(input("Ingrese lado3:"))

#Processing
promedio=(lado1+lado2+lado3)/3

#Verificadores
promedio_correcto=(promedio>=0)

#Ouput
print("##################################################################")
print("# Algoritmo para hallar el promedio de los lados de un triangulo #")
print("##################################################################")
print("# lado1     :",lado1,"                                           #")
print("# lado2     :",lado2,"                                           #")
print("# lado3     :",lado3,"                                           #")
print("# promedio  :",promedio,"                                        #")
print("##################################################################")
print("# promedio correcto:",promedio_correcto,"                             #")
