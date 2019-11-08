#INPUT
trabajador=input("ingrese nombre de trabajador:")
pago_por_horas_extras=float(input("ingrese el pago por horas extras:"))
horas_extras_trabajadas=float(input("ingrese horas extras trabajadas:"))

#PROCESSING
pago_total_de_horas_extras_trabajadas=pago_por_horas_extras*horas_extras_trabajadas

#VERIFICADORES
pago_total_por_horas_extras_alta=(pago_total_de_horas_extras_trabajadas>120)

#OUTPUT

print("###################################################")
print("####   calcular el pago tota por horas extras   ###")
print("###################################################")
print("####trbajador:",trabajador,"                               ###" )
print("#### pago por horas extras:",pago_por_horas_extras,"           #######")
print("#### horas extras trabajadas:",horas_extras_trabajadas,"             #####")
print("#### pago total de horas extras trabajadas:",pago_total_de_horas_extras_trabajadas ,"###")
print("##########################################")
print("pago total  por horas extras  alta:",pago_total_por_horas_extras_alta)
