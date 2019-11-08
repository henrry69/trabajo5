#Input
numero1=float(input("Ingrese numero1:"))
numero2=float(input("Ingrese numero2:"))
numero3=float(input("Ingrese numero3:"))

#Processing
resta=numero1-numero2-numero3

#Verificador
resta_positiva=(resta>=0)

#Ouput
print("################################################")
print("# Algoritmo para hallar la resta de 3 numeros  #")
print("################################################")
print("# numero1 :",numero1,"                              #")
print("# numero2 :",numero2,"                              #")
print("# numero3 :",numero3,"                              #")
print("# resta   :",resta,"                             #")
print("################################################")
print("# La resta es positiva:",resta_positiva,"                 #")
