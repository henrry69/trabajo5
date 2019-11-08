#Input
numero1=int(input("Ingresar numero1:"))
numero2=int(input("Ingresar numero2:"))

#Processing
modulo=numero1%numero2

#Verificador
multiplo=(modulo==0)
#Ouput
print("###########################################################")
print("# Algoritmo para hallar el modulo de dos números enteros  #")
print("###########################################################")
print("# numero1 :",numero1,"                                           #")
print("# numero2 :",numero2,"                                           #")
print("# modulo  :",modulo,"                                            #")
print("###########################################################")
print("# El numero",numero1,"es multipo de",numero2,":",multiplo,"                      #")
