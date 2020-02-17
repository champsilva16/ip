pv=[]
ps=[]
v=0
p=0
soma=0
soma2=0
max=-999
f=0
n=int(input())
for i in range(n):                                 #a
    x,y=map(int,input().split())
    pv.append(x)
    ps.append(y)
for i in range (n):
    if(pv[i]>ps[i]):
        v=v+1
        print("VENCEU {0}x{1}". format(v,p))     #(,sep="")        
    elif(pv[i]<ps[i]):
        p=p+1
        print("PERDEU {0}x{1}". format(v,p))                        #b
    else:
        print("EMPATE {0}x{1}". format(v,p))
              
if(v>p):
    print("VITORIA POR",v,"x",p)
for i in range(n):
    soma=soma+pv[i]
    soma2=soma2+ps[i]
media=soma/n
media2=soma2/n
print("MEDIA DOS PONTOS MARCADOS: {0:.2f}  SOFRIDOS: {1:.2f}". format(media,media2)) #c
for i in range(n):
    v=pv[i]-ps[i]
    if(v>max):
        max=v
        print("MAIOR DIFERENÇA DE PONTOS:",v)
    if(ps[i]<20):
        f=f+1
print("MENOS DE 20 PONTOS:",f,"SETS")
    
