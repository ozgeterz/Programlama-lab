my_list=[1,3,4,5,1,3,4,5,9]
print(my_list)

def frekans_tablosu(liste):
    frekans={}
    for i in liste:
        if(i in frekans):#eger i frekansta mevcutsa if'e gir
            frekans[i]=frekans[i]+1
        else:
            frekans[i]=1
        #print(i,frekans)
    return frekans

#print(frekans_tablosu(my_list))
frekans_tablosu(my_list)

def frekans_tablosu_2(liste_2):
    frekans_liste=[]
    for i in range(len(liste_2)):
        s=False
        for j in range(len(frekans_liste)):
            if(liste_2[i]==frekans_liste[j][0]):#sayi frekans_listesine yollanmis mi?
                frekans_liste[j][1]=frekans_liste[j][1]+1
                s=True
        if(s==False):
                frekans_liste.append([liste_2[i],1])#ekleme
    return frekans_liste
        
print(frekans_tablosu_2(my_list))
