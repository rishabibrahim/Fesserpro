l1=[1,34,33,44,5]
print(l1)
print(l1[2:4])

l1.append(98)
l1.append(98)
print(l1)
l1.remove(33)
l1.pop(0)
l1.insert(0,65)
print(l1)

l1.sort()
i=l1.index(65)
print(i)
print(l1)
a1=[1,2,3]
a2=[5,6]
a1.extend(a2)
print(a1)
s1="hello world"
w=s1.split(' ')
print(w)

s2="amzn--tsla--goog--nifty"
s=s2.split(",")
print(s)

k="@".join(s)
print(k)

s3="amzn--tsla--goog--nifty"
l4=s3.split("--")
# last=l4.pop(-1)
# first=l4.pop(0)
# l4.insert(0,last)
# l4.append(first)
# print(l4)

last=l4[-1]
first=l4[0]
l4[-1]=first
l4[0]=last
print(l4)

# diff between list and tuple
# list is muttableand tuple is not
# list uses [] and tuple ()

# Dictionary

stock_prices={"tesla":100,"amzn":900}
# accesing a new element
print(stock_prices["tesla"])
# adding a new element is dictinary
stock_prices.update({"nifty":500})
print(stock_prices)
# Update value of existing key
stock_prices={"tesla":100,"amzn":900}
stock_prices.update({"amzn":800})
print(stock_prices)

# remove
stock_prices.pop("tesla")
print(stock_prices)

# get function
print(stock_prices.get("amzn1","no value"))
stock_prices.update({"appl":400})

print(stock_prices.keys())
print(stock_prices.values())
print(stock_prices.items())

set={1,2,3}
print(set)