#IMPUT
cateto_uno=float(input("ingrese cateto uno:"))
cateto_dos=float(input("ingrese cateto dos:"))

#PROCESSING
hipotenusa=(cateto_uno**2+cateto_dos**2)**(1/2)

#VERIFICADOR
triangulo_grande=(hipotenusa>100)

#OUTPUT
print("##########################################")
print("####    calcular la hipotenusa        ####")
print("##########################################")
print("#### cateto uno:",cateto_uno,"               ######")
print("#### cateto dos:",cateto_dos,"                #####")
print("#### hipotenusa:",hipotenusa ,"   #####")
print("##########################################")
print("triamgulo grande:",triangulo_grande)
