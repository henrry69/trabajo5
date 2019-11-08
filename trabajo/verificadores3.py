#INPUT
base_mayor=float(input("ingrese base mayor:"))
base_menor=float(input("ingrese base menor:"))
altura=float(input("ingrese altura:"))

#processing
area=altura*(base_menor+base_mayor)/2

#VERIFICADORES
area_pequeña=(area>100)

#OUTPUT
print("##########################################")
print("####   calcular area del trapecio    ####")
print("##########################################")
print("#### base_mayor:",base_mayor,"              #######")
print("#### base_mayor:",base_menor,"              #######")
print("#### altura:",altura,"                    #####")
print("#### area:",area  ,"                      #####")
print("##########################################")
print("area muy pequeña:",area_pequeña)
