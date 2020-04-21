

from sympy as sp
import sympy.plotting as syp
import matplotlib.pyplot as plt

#Binomal Distribution
#170401049
#Olasılık kuramı ve istatistik bilim kollarında, binom dağılımı n sayıda iki kategori sonucu veren denemelere uygulanı
# Bu türlü her bir deneyde, bağımsız olarak, başarı olasılığının p olduğu bilinir.
#İstenen olayın gerçekleşme ihtimali -> a=0.42
#Tüm seçme sayısı -> b=66
#Seçilen hayvanın köpek çıkması gereken sayı -> c=6 


x,b,a,c = Symbol('x'),Symbol('b'),Symbol('a'),Symbol('c')
my_f= binomial(b,c) * a ** c * (1-a)**(b-c)

plot(my_f.subs({a:0.42,c:6}),(b,1,66),title="Binomial Distribution Grap")
xDegerleri,yDegerleri=[],[]
for i in range(1,66):
    y = my_f.subs({a:0.42,c:6,b:i})
    xDegerleri.append(i)
    yDegerleri.append(y)
plt.plot(xDegerleri,yDegerleri)
plt.show()
