from main import fetch_lines

lines = fetch_lines('d1.txt')
res = 0
aa = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
for line in lines:
    #print(line)
    for i, c in enumerate(line):
        aaaa = False
        for x in aa:
            if x in line[:i+1]:
                res += 10 * aa[x]
                #print(aa[x])
                aaaa = True
                break
        if aaaa:
            break

        if '0' <= c <= '9':
            res += 10 * int(c)
            #print(int(c))
            break
    for i, c in enumerate(line[::-1]):
        aaaa = False
        for x in aa:
            #print(line[len(line)-i-1:])
            if x in line[len(line)-i-1:]:
                res += aa[x]
                #print(aa[x])
                aaaa = True
                break
        if aaaa:
            break

        if '0' <= c <= '9':
            res += int(c)
            #print(int(c))
            break

    #print()
print(res)
