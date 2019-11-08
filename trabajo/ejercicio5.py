#Input
numero1=float(input("Imgrese numero1:"))
numero2=float(input("Imgrese numero2:"))

#Processing
potencia=(numero1*numero2)**5

#Verificador
potencia_excedida=(potencia>=1000)

#Ouput
print("##################################################")
print("# Algoritmo para elevar un producto a la quinta  #")
print("#################################################")
print("# numero1  :",numero1,"                            #")
print("# numero2  :",numero2,"                            #")
print("# potencia :",potencia,"                            #")
print("##################################################")
print("# potencia excedida:",potencia_excedida,"               #")
