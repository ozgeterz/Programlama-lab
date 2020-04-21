



import sympy as sym #gerekli olan kütüphaneler
from sympy import Symbol,factorial
from sympy import pprint
import matplotlib.pyplot as plt

x,n,p=Symbol("x"),Symbol("n"),Symbol("p")
part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x)) #formülün ilk parçası
pprint(part_0)

part_1=p**x
pprint(part_1)

part_2=(1-p)**(n-x) 
pprint(part_2)

my_f=(part_0*part_1*part_2) #formülün partlarını birleştirip oluşturduk
pprint(my_f)

x_values=[] #değerleri oluşturduk
y_values=[]
for value in range (0,10): #döngü ile 0 ile 10
    y=my_f.subs({p:0.42,n:8,x:value},title="Binomial Distribution") #p ve n ye değer atandı
    y_values.append(y) 
    x_values.append(value)
    print(value,y)

plt.plot(x_values,y_values) 
plt.show() #grafik çizimi 
