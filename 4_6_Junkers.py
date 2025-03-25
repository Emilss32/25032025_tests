import random
N = 15
l = []
for i in range(N):
    l.append(random.randint(-200, 200))

rez = [1, 2, 3, 4, 5, 6, 7] #uzdevumi d-i un 2h jo index

rez[0] = sum(1 for x in l if x < l[-1])
rez[1] = sum(1 for x in l if min(l[0], l[-1]) < x < max(l[0], l[-1]))
rez[2] = sum(1 for x in l if x > 2 * (sum(l) / N))
g_psk = [x for x in l if x % 2 == 0]
if g_psk: rez[3] = sum(g_psk) / len(g_psk)
else: rez[3] = 0
rez[4] = max(l)
rez[5] = l.index(rez[4])
id7 = [x for x in l if x % 7 == 0]
if id7: rez[6] = max(id7)
else: rez[6] = 0

print(l)
print(rez)

