import re
fname = input('Enter File Name : ')
if len(fname) < 1 : fname = "assignment11.txt"

fh = open(fname)

total = 0

for line in fh:
        temp = line.rstrip()
        temp = re.findall('[0-9]+', temp)
        #print(temp)
        #print('\n')
        if len(temp) > 0:
            for w in temp:
                # wd += 1
                total += int(w)

print(total)
