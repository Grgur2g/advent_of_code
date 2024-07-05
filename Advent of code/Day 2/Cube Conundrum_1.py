INPUT = "input//"
with open(INPUT + '1.txt') as f:
    lines = f.readlines()
suma = 0
curr = 0
dict_ = {'red' : 12, 'green' : 13, 'blue' : 14}

#only 12 red cubes, 13 green cubes, and 14 blue cubes
for index, line in enumerate(lines):
    line = line.strip()
    filler = {'red' : 0, 'green' : 0, 'blue' : 0}
    seq3 = line.split(":")
    seq2 = seq3[1].split(";")
    for i in range(len(seq2)):
        seq1 = seq2[i].split(",")
        for j in range(len(seq1)):
            seq = seq1[j].split(" ")
            #print(seq[1],seq[2],filler[seq[2]],"\t ovo je sekv ",seq2[i])
            if int(filler[seq[2]]) < int(seq[1]):
               filler[seq[2]] = seq[1]
    curr += index+1
    for key,value in dict_.items():
        if int(filler[key]) > int(dict_[key]):
            #print(index)
            suma += index+1
            break
    
print(curr-suma)