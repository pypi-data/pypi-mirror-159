import dropb
def addprofile(base,name,znac,autopush=True):
    open(f'{base}.txt', 'a+')
    fin = open(f"{base}.txt", "at")

    fin.write(f'{name} {str(znac)}\n')

    fin.close()
    if autopush==True:
        dropb.push_database(base)
    else:
        ...
def getbase(base):
    open(f'{base}.txt', 'a+')
    f = lambda A, n=2: [A[i:i + n] for i in range(0, len(A), n)]
    A = (open(f'{base}.txt','r').read()).split()
    a= ((f(A)))
    d = dict(a)
    return d
def addmoney(base,name,key,money,autopush=True):
    open(f'{base}.txt', 'a+')
    dic=getbase(base)

    money1=int(dic[name])
    if key=='+':
        dic[name]=str(int(money1)+int(money))
    else:
        dic[name]=str(int(money1)-int(money))
    dic=((list(dic.items())))
    ab=[]
    for i in range(len(dic)):
        ab.append(' '.join(list(dic[i])))
    dic='\n'.join(ab)
    f = open(f'{base}.txt', 'w')
    f.write(dic)
    f.close()
    if autopush==True:
        dropb.push_database(base)
    else:
        ...
def checkbase(base,name):
    open(f'{base}.txt', 'a+')

    dic = getbase(base)

    money1 = int(dic[name])
    return money1

def removeuser(base,name,autopush=True):
    open(f'{base}.txt', 'a+')
    text = open(f'{base}.txt', 'r').read()
    text = text.replace(f'{name} {str(checkbase(base, name))}', '', 1)
    f = open(f'{base}.txt', 'w')
    f.write(text)
    f.close()
    if autopush==True:
        dropb.push_database(base)
    else:
        ...
#Чтобы загрузить базу с сервера, используй функцию:
#get_database(Название базы)