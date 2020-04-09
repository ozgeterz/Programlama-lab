import sys

def histogramOlustur(dosya):
    histogram = []
    for i in dosya:
        kontrol = False
        for k in range(len(histogram)):
            if int(i.split(";")[3].split("-")[1]) == histogram[k][0]:
                histogram[k][1] += 1
                kontrol = True
        if kontrol == False:
            histogram.append([int(i.split(";")[3].split("-")[1]), 1])
    return histogram
    
def ort(dizi):
    toplam=0
    for i in dizi:
        toplam+=i
    return toplam/len(dizi)

def bubbleSort(dizi):
    for i in range(len(dizi)-1,-1,-1):
        for j in range(0,i):
            if not dizi[j]<dizi[j+1]:
                temp=dizi[j]
                dizi[j],dizi[j+1]=dizi[j+1],temp
    return dizi

def median(dizi):
    dizi=bubbleSort(dizi)
    if len(dizi)%2==1:
        orta = int(len(dizi)/2)+1
        return dizi[orta-1]
    else:
        orta1,orta2=dizi[int(len(dizi)/2)],dizi[int(len(dizi)/2)-1]
        return (orta1+orta2)/2
             
        
def dosyaYaz(adres):
    yazilacak_dosya= open(adres+"170401049_hw_2_output.txt","w+",encoding="UTF-8")
    yazilacak_dosya.write(f"Median : {median(aylar)}")
    yazilacak_dosya.write(f"Ortalama : {ort(aylar)}")
    yazilacak_dosya.close()
    
with open(sys.argv[1]+"input_hw_2.csv") as dosya:
    histogram = histogramOlustur(dosya)
    aylar = histogram[1]
    histogram = histogram[0]
    dosyaYaz(sys.argv[2])
    print("Histogram : ",histogram)
