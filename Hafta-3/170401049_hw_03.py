
#Binomal Distribution
#Olasılık kuramı ve istatistik bilim kollarında, binom dağılımı n sayıda iki kategori sonucu veren denemelere uygulanır.
#Bu türlü her bir deneyde, bağımsız olarak, başarı olasılığının p olduğu bilinir.
#170401049 

#Çiftlikten seçilen hayvanın köpek olma olasılığı-> p=0.42=42/100
#Çiflikteki seçilen hayvanın köpek olma durumu 1, olmama durumu 0 olsun
# 8 hayvan seçilmesi durumunda oluşacak binom grafiği 
#n=8

import sympy as sym 
from sympy import Symbol #gerekli olan kütüphaneler
from sympy import pprint
import matplotlib.pyplot as plt

p,n,x=Symbol('p'),Symbol('n'),Symbol('x') #değişkenler symbol sekline cevrildi

my_func_1=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x)) #formüldeki kombinasyon adımı
my_func_1
pprint(my_func_1)

my_func_2=p**x
my_func_2
pprint(my_func_2)#fonksiyonun p üzeri x kısmı

my_func_3=(1-p)**(n-x)
my_func_3
pprint(my_func_3)

my_func=my_func_1*my_func_2*my_func_3 #adımları birleştirip gerçek fonksiyonu elde ettik
my_func #binom dağılımı fonksiyonu
pprint(my_func)

sym.plot(my_func.subs({p:0.42,n:8}),(x,0,8),title='binomial distribution')

