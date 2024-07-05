def convert(row):
    nums_all=[]
    nums = []
    redni = []
    redni_all = []
    #print(row)
    for index,s in enumerate(row):
        try:
            a = int(s)
            nums.append(a)
            redni.append(index)
        except:
            if len(nums)>=1:
                nums_all.append(nums)
                redni_all.append(redni)
            nums = []
            redni = []
    #print(nums_all,redni_all)
    return nums_all, redni_all

lista = ["0","1","2","3","4","5","6","7","8","9","."]
#lista = [0,1,2,3,4,5,6,7,8,9,"."]

def check(engage, start, end, niz):
    for x in range(engage,engage+3):
        for z in range(start,end+1):
            # print(niz[x][z]," --> ", lista)
            if niz[x][z] not in lista: 
                return True
    # print("false")
    return False

def calc(nums_all):
    broj = 0
    for num in nums_all:
        broj = broj * 10 + int(num)
    return broj


INPUT = "input//"
with open(INPUT + '1.txt') as f:
    lines = f.readlines()
    suma = 0

    niz = []
    n = (len(lines[0])+1)
    #niz.append([0])
    niz.append("."*n) 
    for line in lines:
        line = line.strip()
        niz.append('.'+line+'.')
    niz.append("."*n)
    for i in range(1,len(niz)-1):
        nums_all, redni_all = convert(niz[i])
        for index, r in enumerate(redni_all):
            fact = False
            fact = check(i-1,r[0]-1,r[-1]+1,niz)
            if fact:
                #suma += calc(nums_all)
                broj=0
                broj = calc(nums_all[index])
                suma+=broj
print(suma)

