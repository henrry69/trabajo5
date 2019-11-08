#INPUT
trabajador=input("ingrese nombre de trabajador:")
pago_por_horas=float(input("ingrese pago por horas:"))
horas_trabajadas=float(input("ingrese horas trabajadas:"))

#PROCESSING
pago_de_trabajador=pago_por_horas*horas_trabajadas

#VERIFICADOR
a=(pago_de_trabajador>100)

#OUPUT
print("##########################################")
print("####   calcular pago de trabajador    ####")
print("##########################################")
print("####trabajador:",trabajador,"                  ###" )
print("#### pago de trabajdor:",pago_de_trabajador,"         #####")
print("#### pago por horas :",pago_por_horas,"           #####")
print("#### horas trabajadas:",horas_trabajadas,"          #####")
print("##########################################")
print("trabjador con buen sueldo:",a)
