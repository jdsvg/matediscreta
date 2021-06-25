import math
#Algoritmo
def es_primo(n,e):
        for d in range(2,(math.floor(math.sqrt(n)+1) ) ):
                if(n%d == 0):
                        #return d
                        #Factorizacion prima:
                        c = int(n/d)        
                        print(n,"=",d,"*",c)
                        return es_primo(c,e)
        return 0

#n>1, 1<d<n
n= 2867
c = 0
salida = 0
e = n
entrada = n
#Resultados
print(es_primo(n,e))
#
print("----------------------------------------------------------------------")
p = 1300
z = 2701
n = 17
c=pow(p,n) % z
print(c)
print("----------------------------------------------------------------------")
c = 1315
s = 251
z = 2867
p=pow(c,s) % z
print(p)