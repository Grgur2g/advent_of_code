INPUT = "input//"
with open(INPUT + '1.txt') as f:
    lines = f.readlines()
suma = 0


for index, line in enumerate(lines):
    line = line.strip()
    seq2 = line.split(":")
    seq1 = seq2[1].split("|")
    left, right = [], []

    seq1[0] = seq1[0].strip()
    left = seq1[0].split(" ")


    seq1[1] = seq1[1].strip()
    right = seq1[1].split(" ")

    left = [x for x in left if x != '']
    right = [x for x in right if x != '']


    potencija = -1
    for numb in left:
        if  numb in right:
            potencija +=1

    if potencija >= 0:
        suma += 2**potencija
print(suma)

