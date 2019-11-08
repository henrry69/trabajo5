#INPUT
trabajador=input("ingrese nombre de trabajador:")
numero_de_articulos_vendidos=float(input("ingrese numero de articulos vendidos:"))
monto_promedio_de_ventas=float(input("ingrese monto promedio dde ventas:"))

#PROCESSING
bonificacion=numero_de_articulos_vendidos*monto_promedio_de_ventas

#VERIFICADOR
bonificacion_alta=(bonificacion<50)

#OUTPUT

print("##########################################")
print("####   calcular la bonificacion       ####")
print("##########################################")
print("####trbajador:",trabajador,"                  ###" )
print("#### numero de articulos vendidos:",numero_de_articulos_vendidos,"###")
print("#### monto promedio de ventas:",monto_promedio_de_ventas,"   ####")
print("#### bonificacion:",bonificacion  ,"               ####")
print("##########################################")
print("bonificacion alta:",bonificacion_alta)
