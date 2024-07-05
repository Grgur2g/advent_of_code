INPUT = "input//"
with open(INPUT + '1.txt') as f:
    lines = f.readlines()

dict_ = {'one': 'o1ne',
         'two': 't2wo',
         'three': 'th3ree',
         'four': 'fo4ur',
         'five': 'fi5ve',
         'six': 's6ix',
         'seven': 's7even',
         'eight': 'e8ight',
         'nine': 'n9ine',
         }

suma = 0

for line in lines:
    for index,value in dict_.items():
        line = line.replace(index, str(value))

    nums = []
    num = 0

    for s in line:
        try:
            a = int(s)
            nums.append(a)
        except:
            pass
        
    num = nums[0] * 10 + nums[-1]
    suma += num

print(suma)
            