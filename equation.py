print("Programa Javier Jiménez")
print(''' Ecuacion de 2º Grado ''')
print(''' ax2+bx+c ''')

a=int(input("Valor de a: "))
b=int(input("Valor de b: "))
c=int(input("Valor de c: "))

disc=(b*b)-4*a*c    

if disc<0:
  disc=abs(disc)
  x1=complex(((-b)/2*a),(((disc)**1/2)/2*a))
  x2=complex(((-b)/2*a),(((disc)**1/2)/2*a))
  if x1==x2:
    print("x1 = ", x1)
  else:
    print("x1 = ", x1)
    print("x2 = ", x2)

else:
  x1=(-b+(disc)**1/2)/2*a
  x2=(-b-(disc)**1/2)/2*a
  if x1==x2:
    print("x1 = ", x1)
  else:
    print("x1 = ", x1)
    print("x2 = ", x2)
