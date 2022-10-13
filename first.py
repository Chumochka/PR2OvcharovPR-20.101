while(True):
    a=input()
    if(a=='end'):
        break
    if(len(a)>=3):
        n=0
        for i in a:
            try:
                k=float(i)
            except Exception:
                n+=1
        if(n==len(a)):
            with open('./text/'+a,'w') as con:
                pass
        else:
            print('Введите слово')
    else:
        print('Введите слово от 3 символов длиной')