#Input
precio1=float(input("Ingresar el precio1:"))
precio2=float(input("Ingresar el precio2:"))
precio3=float(input("Ingresar el precio3:"))
precio4=float(input("Ingresar el precio4:"))
precio5=float(input("Ingresar el precio5:"))
precio6=float(input("Ingresar el precio6:"))
precio7=float(input("Ingresar el precio7:"))

#Processing
suma=precio1+precio2+precio3+precio4+precio5+precio6+precio7

#Verificador
comprador_compulsivo=(suma>=300)
#Ouput
print("################################################################")
print("# Algoritmo para hallar la suma de precios de útiles escolares #")
print("################################################################")
print("# precio1 :",precio1,"                                                    #")
print("# precio2 :",precio2,"                                                    #")
print("# precio3 :",precio3,"                                                    #")
print("# precio4 :",precio4,"                                                    #")
print("# precio5 :",precio5,"                                                    #")
print("# precio6 :",precio6,"                                                    #")
print("# precio7 :",precio7,"                                                    #")
print("# suma    :",suma,"                                             #")
print("################################################################")
print("# el comprador escoje los productos mas caros:",comprador_compulsivo,"            #")
