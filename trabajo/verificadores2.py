#INPUT
dioganal_mayor=float(input("ingrese diagonal_mayor:"))
dioganal_menor=float(input("ingrese diagonal_menor:"))

#PROCESSING
area=(dioganal_menor*dioganal_mayor)/2
#VERIFICADOR

rombo_pequeño=(area<20)

#OUTPUT
print("##########################################")
print("####     calcular area del rombo      ####")
print("##########################################")
print("#### diagonal_mayor:",dioganal_mayor,"          #######")
print("#### diagonal_menor:",dioganal_menor,"           ######")
print("#### area:",area  ,"                      #####")
print("##########################################")
print("rombo pequeno:",rombo_pequeño)
