#INPUT
radio=float(input("ingrese radio:"))
pi=float(input("ingrese el valor de pi:"))

#PROCESSING
area=pi*(radio**2)

#VERIFICADOR
radio_pequeno=(area<20)

#OUTPUT
print("##########################################")
print("####   calcular area del circulo      ####")
print("##########################################")
print("#### radio:",radio,"                   #######")
print("#### pi:",pi,"                       #####")
print("#### area:",area  ,"                     #####")
print("##########################################")
print("radio pequeno:",radio_pequeno)
