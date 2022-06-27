num1=float(input("calificacion 1:"))
num2=float(input("calificacion 2:"))
num3=float(input("calificacion 3:"))

promedio=(num1+num2+num3)/3
print("promedio:",promedio)

if promedio<6:
  print("Reprobaste el año")
if promedio>=6:
  print("Pasaste el año")
if promedio>=9:
  print("¡Felicidades!")