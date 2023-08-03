start = 16
end = 128
n = 5

step = (end/start)**(1/(n-1))

for i in range(n):
    print(round(start*step**i))