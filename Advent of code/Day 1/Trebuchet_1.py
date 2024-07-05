INPUT = "input//"
with open(INPUT + '1.txt') as f:
    lines = f.readlines()
suma = 0
#print(lines)
for line in lines:
    nums = []
    num = 0
    for s in line:
        try:
            a = int(s)
            nums.append(a)
            #print(a,nums)
        except:
            pass
    num = nums[0] * 10 + nums[-1]
    #print(num)
    suma += num
print(suma)