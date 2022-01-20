def factors(num):
    i=1
    fac = []
    while 2*i <= num:
        if num%i == 0:
            fac.append(i)
            i += 1
        else:
            i += 1

    return fac

test = [sum(factors(i)) for i in range(10000)]

x=[]
y=[]
z=[]

#get d(a) = b where d(b) = a
for i in range(1,10000):
    if test[i] < 10000:
        if i == test[test[i]]:
            y.append(i)
            x.append(test.index(i))

# remove instances where a != b
for i in range(0,len(y)):
    if y[i]!=x[i]:
        z.append(y[i])
        
print(sum(z))




def all_perms(s):
    if len(s) <= 1: 
        yield s
    else:
        for i in range(len(s)):
            for p in permutations(s[:i] + s[i+1:]):
                yield s[i] + p
                

def evens(num):
    #print(num/2)
    return num/2

def odds(num):
    #print(3*num + 1)
    return 3*num + 1

def steps(x):
    counter = 1    # start at one - first term is counted
    while x != 1:   # count steps until sequence reaches 1
        if x%2 == 0:
            x=evens(x)
            counter+=1
        else:
            x=odds(x)
            counter+=1
    return counter
        
x = [steps(i) for i in range(1,1000000)]
x.index(max(x))

x = [i for i in range(1,100)]



# corners: 1,3,5,7,9,13,17,21,25,31,37,43,49,57,65,73,81,101,111,121,131

series = []
series.append(1)      # initial value 1 for centre of spiral
i=2    # start by incrementing by 2 for first 4 corners
n=0    # start counter so we know when we;ve done all the corners

while series[-1] < 1001*1001:
    if n<4:
        series.append(series[-1] + i)
        n+=1
    else:
        n=0     # reset corner counter
        i+=2    # add 2 to account for increasing distance between corners

# 62

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def descending(num):
    return int("".join(sorted(str(num), reverse=True)))


cubes = [descending(i**3) for i in range(1,9000)]

counter=[0 for i in range(0,len(cubes))]
indices = [[] for i in range(0,len(cubes))]

for j in range(0, len(cubes)):
    for i in cubes:
        if i == cubes[j]:
            indices[j].append(j)
            counter[j]+=1
            if counter[j] == 5:
                print(indices[j])
                break
        else:
            continue
        
        
        
