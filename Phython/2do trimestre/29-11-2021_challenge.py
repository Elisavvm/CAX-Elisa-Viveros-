print("Morita's store")
print("insert your name:")
name=input()
print("Welcome",name)
producto1=input('1st product: ')
producto2=input('2nd product: ')
producto3=input('3rd product: ')
producto4=input('4th product: ')
producto5=input('5th product: ')

producto1=int(input('1st product cost: '))
producto2=int(input('2nd product cost: '))
producto3=int(input('3rd product cost: '))
producto4=int(input('4th product cost: '))
producto5=int(input('5th product cost: '))
IVA=producto1+producto2+producto3+producto4+producto5*0.16
subtotal=producto1+producto2+producto3+producto4+producto5
total=producto1+producto2+producto3+producto4+producto5+IVA
print("______________")


print("subtotal:",subtotal)
print("total", total)