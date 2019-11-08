#INPUT
estudiante=input("ingrese nombre de estudiate:")
horas_estudiadas_por_dia=float(input("ingrese horas estudiadas por dias:"))
dias_de_estudio=float(input("ingrese dias de estudio:"))

#PROCESSING
horas_estudiadas_en_la_semana=horas_estudiadas_por_dia*dias_de_estudio

#VERIFICADOR
varias_hora_estudiadas=(horas_estudiadas_en_la_semana>150)

#OUTPUT

print("##############################################")
print("##calcular horas estudiadas a la semana ######")
print("##############################################")
print("####estudiante:",estudiante,"                  ###" )
print("#### horas de estudiadas por dia:",horas_estudiadas_por_dia,"    ####")
print("#### dias de estudio:",dias_de_estudio,"                 ###")
print("#### horas estudiadas a la semana:",horas_estudiadas_en_la_semana  ,"  ####")
print("#############################################")
print("varia  horas estudiadas:",varias_hora_estudiadas)
