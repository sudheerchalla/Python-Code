def l():
       lcw=[]
       u="secret"
       v="bisect"
       #lcw=[[0]*(len(v)+1) for i in range(len(u)+1)]
       for r in range(len(u)+1):     
                      l=[]           
                      for c in range(len(v)+1):
                             l.append(0)
                      lcw.append(l)
       maxlength=0
       for c in range(len(v)-1,-1,-1):
              for r in range(len(u)-1,-1,-1): 
                     if u[r]==v[c]:
                            lcw[r][c]=lcw[r+1][c+1]+1
                     if lcw[r][c]>maxlength :
                            maxlength=lcw[r][c]
       return (maxlength)

print (l())
