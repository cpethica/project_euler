# check if all digits are present in a number

def pandigit(num):
    for i in '123456789':
        if str(num).count(i) ==1 and '0' not in str(num):
            pass
        else:
            return False
    print(f'{num} is pandigital')
    return int(num)

output = []
product = []

for i in range(1,100000):
    for j in range(1,100000):
        if pandigit(str(i*j)+str(i)+str(j)) != False:
            output.append(str(i*j)+str(i)+str(j))
            product.append(str(i*j))

# unique value indices
indexes = [product.index(x) for x in set(product)]

unique = []

for i in indexes:
    unique.append(str(output[i]))

x=list(map(int, unique))
print(sum(x))