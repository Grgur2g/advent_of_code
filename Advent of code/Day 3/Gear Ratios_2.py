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


def check(engage, start, end, niz):
    for x in range(engage,engage+3):
        for z in range(start,end+1):
            # print(niz[x][z]," --> ", lista)
            if niz[x][z] == '*': 
                return x,z
    # print("false")
    return -100,-100

def calc(nums_all):
    broj = 0
    for num in nums_all:
        broj = broj * 10 + int(num)
    return broj


INPUT = "input//"
with open(INPUT + '1.txt') as f:
    lines = f.readlines()
    suma = 0
    dict_ = {}

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
            x,y = check(i-1,r[0]-1,r[-1]+1,niz)
            if x != -100:
                #suma += calc(nums_all)
                broj = 0
                broj = calc(nums_all[index])
                if str(x)+','+str(y) not in dict_:
                    dict_[str(x)+','+str(y)]= [broj]
                else:
                    dict_[str(x)+','+str(y)].append(broj)

for key,value in dict_.items():
    if len(value) > 1:
        broj = 1
        for v in value:
            broj = broj * v
        suma+=broj
print(suma)

