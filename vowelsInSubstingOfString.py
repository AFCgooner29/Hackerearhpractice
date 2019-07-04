'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def findSubs(Str,n):
    i=0
    j=i
    strs = ''
    prvcount = 0
    finalcount = 0
    count = 0
    vowel = ['a','e','i','o','u','A','E','I','O','U']
    while(i<n):
        strs = Str[i:j]
        if(Str[j] in vowel):
            count+=1
            prvcount+= count
        else:
            prvcount+=count
        if(j<n-1):
            j+=1
        elif(i<=n-1):
            i+=1
            j=i
            finalcount+=prvcount
            prvcount = 0
            count = 0
    return finalcount

tot = input()
tot = int(tot)
count = 0
for i in range(tot):
   temp = input()
   print(findSubs(temp,len(temp)))


            
