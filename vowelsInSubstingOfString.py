def findSubs(Str,n):
    strsall = []
    counter = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    for i in range (n):
        for j in range(i,n):
            strs = ''
            for k in range(i,j+1):
                strs = strs + Str[k]
            strsall.append(strs)
    for i in strsall:
        for j in i:
            if (j in vowel):
                counter = counter +1
    return counter


tot = input()
tot = int(tot)
count = 0
for i in range(tot):
    temp = input()
    print(findSubs(temp,len(temp)))
