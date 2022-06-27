##comentarios son lineas que no se ejecutan y son de uso del programador

#aqui modifique algo
#print("hola")

'''#print("hola")
#print("hola")
#print("hola")
#print("hola")
#print("hola")'''

##Constantes: tienen informacion que no cambia
pi=3.1416

##Variables: tienen informacion que PUEDE cambiar
fecha=7
fecha=8


###ejemplo de comentar una linea que no quiero usar ahorita###
#while True:
  #fecha=fecha+1

#TIPOS DE DATOS

#INT o integrers o enteros
entero=456
#FLOAT o floting o flotantes
flotante=456.5
#string o cadenas
ejemplo1="hola que hace"
ejemplo2="heyy"
ejemplo3="12345678, letras y )(/&"
#bool o boolean o boleanos: Evaluan un falso y verdadero
aprobado=True
reprobaratodoelgrupo=False

#COMANDOS
#print(mensaje): Es mandar a la consola informacion del codigo

#print para imprimir datos ya guardados en variable/Constantes
print(ejemplo1)
print(ejemplo3)
print(fecha)



#print para imprimir algo directamente
print('helloooo strangerrr')
print('080907')

#print combinado
print('el mensaje enviado fue:',ejemplo1)
print(fecha,'de Enero')

#imput(): Agregar datos directamente en la compile
nombre=input()
print('hola',nombre)

apellido=input('ingree su apellido:')
print('su nombre es',nombre,apellido)

#solo ingresa cadenas(strings)
num=input('ingrese numero')
print('el numero 10 veces es:',(10*num))

#int(): sirve para convertir una STRING en INT
#float(): sirve para convertir una STRING en un FLOAT
num=int(input('ingrese numero:'))
print('el numero 10 veces es',(10*num))


#while(): Es una estructura que permite repetir un codigo practicamente de una forma infinita
#Evaluan falso o verdadero

while True:
  input()
  print('hola')

#comparadores

  # == identico
  # >< mayor o menor
  # != falso
  # >= o <= mayor o igual; menor o igual

zeta=int(input('numero:'))
while zeta>=5:
  print("Tu numero es mayor o igual a 5")

pasw=input('password: ')

while (passw!='hola'):
  print(" Volver a intentar ")