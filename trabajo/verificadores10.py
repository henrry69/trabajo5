#INPUT
masa=float(input("ingrese masa:"))
longitud=float(input("ingrese longitud:"))
tiempo=float(input("ingrese tiempo:"))

#PROCESSING
energia=(masa*longitud**2)/tiempo**2

#VERIFICADOR
mucha_energia_utilizada=(energia>10)

#OUTPUT
print("mucha energia utilizadas",mucha_energia_utilizada)
print("##########################################")
print("####   calcular area del rectangulo   ####")
print("##########################################")
print("#### base_mayor:",masa,"              #######")
print("####tiempo:", tiempo,"                    ######")
print("#### altura:",longitud,"                    #####")
print("#### area:",energia ,"       #####")
print("##########################################")
print("area muy pequeña:",mucha_energia_utilizada)
