#INPUT
base=float(input("ingrese base:"))
altura=float(input("ingrese altura:"))

#PROCESSING
area=base*altura

#VERIFICADOR
a=(area<100)

#OUTPUT
print("##########################################")
print("####   calcular area del rectangulo   ####")
print("##########################################")
print("#### base:",base,"                      #####")
print("#### altura:",altura,"                    #####")
print("#### area:",area  ,"                      #####")
print("##########################################")
print("area muy pequeña:",a)
