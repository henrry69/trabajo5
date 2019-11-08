#Input
numero1=float(input("Ingresar el numero1:"))
numero2=float(input("Ingresar el numero2:"))

#Processing
raiz=(numero1*numero2)**(1/2)

#verificador
raiz_exacta=(raiz==int(raiz))

#Ouput
print("###########################################################")
print("# Algoritmo para hallar la raiz cuadrada de un producto   #")
print("###########################################################")
print("# numero1 :",numero1,"                                        #")
print("# numero2 :",numero2,"                                        #")
print("# raiz  :",raiz,"                                 #")
print("###########################################################")
print("# raiz exacta:",raiz_exacta,"                                     #")
