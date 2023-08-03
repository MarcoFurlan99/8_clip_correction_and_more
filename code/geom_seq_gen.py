start = 24
end = 128
n = 7

step = (end/start)**(1/(n-1))

l = []

for i in range(n):
    l.append(round(start*step**i))

print(l)