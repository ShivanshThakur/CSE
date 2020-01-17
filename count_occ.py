def count_occ(sub, st):
    ind_ne=-1
    ind_ol=-1
    c=0
    s=set()
    for i in range(len(st)):
        if(sub[0]==st[i]):
            ind_ol=ind_ne
            ind_ne=i
            c+=1
            j=0
            while j+1<len(sub):
                if sub[j+1]!=st[i+j+1]:
                    c-=1
                    ind_ne=ind_ol
                    break
                j+=1
            s.add(ind_ne)
    return(s, ind_ne, c)

st=input('Enter string :')
sub=input('Enter substring :')
s, i, c=count_occ(sub, st)
s=list(s)
print('Found ', sub,'"', c, '"time(s)\nLast occurance at :', i, '\nAll occurances :',
      s)
