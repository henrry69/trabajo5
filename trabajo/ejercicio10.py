#Input
lado1=float(input("Ingrese lado1:"))
lado2=float(input("Ingrese lado2:"))

#Processing
area=lado2*lado1

#Verificador
area_muy_pequeña=(area<=10)

#Ouput
print("##################################################")
print("# Algoritmo para hallar el area de un rectangulo #")
print("##################################################")
print("# lado1 :",lado1,"                                     #")
print("# lado2 :",lado2,"                                     #")
print("# area  :",area,"                                  #")
print("##################################################")
print("# area muy pequeña:",area_muy_pequeña,"                         #")
