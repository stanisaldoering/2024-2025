
def szyfruj(n,klucz,w,m,k):
    if n+k-1<m:
        for i in range(k):
            s=s+w[n+klucz[i]-1]
        szyfruj(n+k,w, klucz,m,k)
    else:
        while n<=m:
            if n<m:
                s=s+w[n+1]+w[n]
                n=n+2
            else:
                s=s+w[n]
                n=n+1

s = ""
w='KOLORADO'
m=len(w)-1
klucz=[2,3,1]
k=len(klucz)-1
print(szyfruj(0,klucz,w,m,k))
