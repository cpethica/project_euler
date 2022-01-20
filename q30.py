#  question 30

output = []

for i in range(1000,1000000):
    x = [int(i) for i in list(str(i))]
    if i == sum([x**5 for x in x]):
        print(i)
        output.append(i)
        
print(f'Total : {sum(output)}')