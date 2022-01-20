#!/usr/bin/env python

#Question 12

def factors(num):
    fac = []
    count = 0
    for i in range(1,int((num+1)**0.5)):
        if num%i == 0:
            count+=2
            fac.append(i)
            fac.append(num/i)
        else:
            continue

    return count

def tri_divs(target):
    counter = 1
    x = 0
    divs = 0
    
    while divs < target:
        if counter == 1:
            x=1
            counter+=1
        else:
            x+=counter
            counter+=1   
    
        divs = factors(x)

        if divs >= target:
            print(f'{x} has {divs} divisors')
        else:
            pass

#Question 15
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

(factorial(40)/factorial(20))/factorial(20)


#Question 16

x = 2**1000
def split(word):
    return [char for char in word]

y=[int(i) for i in split(str(x))]
print(sum(y))

#Question 18

# read file line by line into list and remove /n and whitespaces
with open("q18.txt") as file_in:
    lines = []
    for line in file_in:
        lines.append(line.rstrip())
# split space delimited numbers
lines2 = [i.split() for i in lines]
# convert all numbers to int from string
nums = [[int(j) for j in i] for i in lines2]

#number of options is number of rows n factorial (n!)


#Question 20

def factorial(num):
    x=1
    for i in range(2,num+1):
        x=x*i
    return x

x=factorial(100)
x=str(x)

def split(word):
    return [char for char in word]

digits = split(x)

digits=[(int(x)) for x in digits]

print(sum(digits))

#Question 21

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


#Question 25

def fibo(digits):
    fibo = [1,1]
    counter = 1
    while len(str(fibo[-1])) < digits:
        fibo.append(fibo[counter]+fibo[counter-1])
        counter+=1
    print(f'Index is {len(fibo)} and number is {fibo[-1]}')

fibo(1000)


#Question 26
#Prime number generator

def primes (n):
    prime_bool = [True for i in range(n)]
    for i in range(2, int(n**0.5)):       # start from index 2  
        if prime_bool[i] == True:
            for j in range(2*i,n,i):       # increment by i (the current multiple)
                prime_bool[j] = False          # mark multiples as false (ie not prime)
    
    p_nums = []
    for k in range(2,len(prime_bool)):
        if prime_bool[k] == True:
            p_nums.append(k)
    return p_nums
p_nums = primes(1000)

# use 10**k = 1 % p
def reptend_check(prime):
    reptend = 0
    if (10**(prime-1)) % prime == 1:
        for i in range(2,prime):
            if (10**(prime-i)) % prime != 1:
                if i==prime-1:
                    #print(f'{prime} is a full reptend prime')
                    reptend = prime
            else:
                #print(f'{prime} is not a full reptend prime')
                break
    else:
        print(f'{prime} is not a full reptend prime')    
    return reptend   

p_nums = primes(1000)
reptends = []
for i in p_nums:
    reptends.append(reptend_check(i))

max(reptends)

#Question 69


import math

def factors(num):
    fac = []
    for i in range(1,int(num**0.5)+1):
        if num%i == 0:
            fac.append(i)
            fac.append(num//i)
            fac.sort()
        else:
            continue

    return fac

factor_array = [factors(x) for x in range(1,1000001)]


coprimes = []
count = 1                                # start at 1 as 1 is always relatively prime
for j in range(1,len(factor_array)):
    for i in range(1,j):
        if list(set(factor_array[j]) & set(factor_array[i])) == [1]:
            count+=1
        else:
            pass
    
    coprimes.append(count)
    count = 1                            # reset counter to 1