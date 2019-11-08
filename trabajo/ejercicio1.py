#Input
nota1=float(input("Inresar nota1:"))
nota2=float(input("Inresar nota2:"))
nota3=float(input("Inresar nota3:"))
nota4=float(input("Inresar nota4:"))

#Processing
promedio=(nota1+nota2+nota3+nota4)/4

#Verificador
alumno_aprobado=(promedio>=11)

#Ouput
print("############################################")
print("# Algoritmo para saber la suma de 4 notas  #")
print("############################################")
print("# nota1    :",nota1,"                            #")
print("# nota2    :",nota2,"                            #")
print("# nota3    :",nota3,"                            #")
print("# nota4    :",nota4,"                            #")
print("# promedio :",promedio,"                            #")
print("############################################")
print("# alumno aprobado:",alumno_aprobado,"                    #")
