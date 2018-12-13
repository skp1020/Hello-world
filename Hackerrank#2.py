#Ordered Dictionary problem from Hackerrank

from collections import OrderedDict

n=int(input("Enter no.of inputs"))
d=OrderedDict()
            
for _ in range(n):
    line = input().split()
    item_name, net_price = ' '.join(line[:-1]), int(line[-1])
    if item_name in d: d[item_name] += net_price
    else: d[item_name] = net_price

for item in d:
    print(item, d[item])
