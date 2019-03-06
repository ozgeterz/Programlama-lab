## 2 ye 2 lik determinant hesaplayan kod


matris_1=[[5,6],[7,9]]
matris_2=[[1,2,3],[4,5,6],[7,8,9]]
print(matris_1,matris_2)

def det_2_2_hesap(m_1):
    s_1=m_1[0][0]*m_1[1][1]
    s_2=m_1[0][1]*m_1[1][0]
    s_3=s_1-s_2
    return s_3
print(det_2_2_hesap(matris_1))

def satırsil(m1,m,n):
    sonuc=[]
    size_1=(len(m1))
    size_2=(len(m1[0]))
    for i in range(size_1):
        if(i==m):
            continue
        row_1=[]
        for j in range(size_2):
            if(j==n):
                continue
            row_1.append(m1[i][j])
        sonuc.append(row_1)
    return sonuc
matris_1=[[5,6],[7,9]]
print(matris_2,satırsil(matris_2,0,0))

def det_3_3_hesap(m_1):
    a1=m_1[0][0]
    a2=satırsil(m_1,0,0)
    a3=det_2_2_hesap(a2)
    a4=a1*a3

    b1=m_1[0][1]
    b2=satırsil(m_1,0,1)
    b3=det_2_2_hesap(b2)
    b4=b1*b3

    c1=m_1[0][2]
    c2=satırsil(m_1,0,2)
    c3=det_2_2_hesap(c2)
    c4=c1*c3

    return a4-b4+c4
print(det_3_3_hesap(matris_2))

matris_4=[[4,6,3,7],[6,2,8,4],[2,9,5,1],[3,0,2,4]]
def det_4_4_hesap(m_1):
    a1 = m_1[0][0]
    a2 = satırsil(m_1, 0, 0)
    a3 = det_3_3_hesap(a2)
    a4 = a1 * a3

    b1 = m_1[0][1]
    b2 = satırsil(m_1, 0, 1)
    b3 = det_3_3_hesap(b2)
    b4 = b1 * b3

    c1 = m_1[0][2]
    c2 = satırsil(m_1, 0, 2)
    c3 = det_3_3_hesap(c2)
    c4 = c1 * c3

    d1=m_1[0][3]
    d2=satırsil(m_1,0,3)
    d3=det_3_3_hesap(d2)
    d4=d1*d3

    return a4-b4+c4-d4
print(det_4_4_hesap(matris_4))

