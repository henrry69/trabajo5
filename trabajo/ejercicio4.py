#Input
numero1=float(input("Imgrese numero1:"))
numero2=float(input("Imgrese numero2:"))

#Processing
división=numero1/numero2

#Verificador
division_exacta=(división==int(división))
#Ouput
print("########################################################")
print("# Algoritmo para hallar la division entre dos números  #")
print("########################################################")
print("# numero1  :",numero1,"                                #")
print("# numero2  :",numero2,"                                #")
print("# division :",división,"                               #")
print("########################################################")
print("# La division es exacta:",division_exacta,"                  #")
